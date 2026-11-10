"""The toolbox every soldier carries.

Tools are grouped into permission tiers:

* ``read``  - inspect the workspace (always safe)
* ``write`` - create, edit and delete files inside the workspace
* ``exec``  - run allow-listed commands (tests, linters, builds)

An agent only ever sees the tiers its roster entry grants *and* the run's
configuration allows. Every path is confined to the workspace root and every
command is matched against an allow-list; nothing goes through a shell.
"""

from __future__ import annotations

import fnmatch
import os
import re
import shlex
import subprocess
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable

from .config import ArmyConfig

IGNORED_DIRS = {
    ".git", ".hg", ".svn", "node_modules", "__pycache__", ".venv", "venv",
    ".army", ".mypy_cache", ".pytest_cache", ".ruff_cache", "dist", "build",
    ".tox", ".idea", ".vscode", "target",
}
MAX_READ_BYTES = 200_000
MAX_OUTPUT_CHARS = 20_000

# Commands that are never allowed, even if a prefix in the allow-list matches.
FORBIDDEN_TOKENS = {"rm", "sudo", "curl", "wget", "ssh", "scp", "dd", "mkfs", "chmod", "chown"}
FORBIDDEN_GIT = {"push", "reset", "clean", "rebase", "checkout", "switch", "branch", "tag", "remote", "config"}

SUBMIT_TOOL = "submit_report"

# Server-side web tools run on Anthropic's infrastructure; the dynamic-filtering
# variants need a recent model, older ones get the basic variants.
WEB_TOOL_NAMES = ("web_fetch", "web_search")
_DYNAMIC_WEB_PREFIXES = (
    "claude-fable-", "claude-mythos-", "claude-opus-5", "claude-opus-4-8", "claude-opus-4-7",
    "claude-opus-4-6", "claude-sonnet-5", "claude-sonnet-4-6",
)


def web_tool_definitions(model: str, max_uses: int) -> list[dict[str, Any]]:
    dynamic = model.startswith(_DYNAMIC_WEB_PREFIXES)
    return [
        {"type": "web_fetch_20260209" if dynamic else "web_fetch_20250910", "name": "web_fetch",
         "max_uses": max_uses},
        {"type": "web_search_20260209" if dynamic else "web_search_20250305", "name": "web_search",
         "max_uses": max_uses},
    ]

# Environment variables whose names look like credentials are not passed to
# commands agents run (tests in an untrusted change could otherwise read them).
SECRET_ENV = re.compile(
    r"(^|_)(API_?KEY|KEY|KEYS|ACCESS_KEY_ID|TOKEN|SECRET|PASSWORD|PASSWD|CREDENTIALS?|AUTH)(_|$)", re.IGNORECASE
)
SAFE_ENV_PREFIXES = ("GIT_CONFIG_",)  # git's own KEY_n/VALUE_n config pairs


def scrubbed_env() -> dict[str, str]:
    return {
        k: v for k, v in os.environ.items()
        if k.startswith(SAFE_ENV_PREFIXES) or not SECRET_ENV.search(k)
    }


class ToolError(Exception):
    """Raised for a tool call the model can correct (bad path, no match...)."""


@dataclass
class ToolSpec:
    name: str
    tier: str
    description: str
    schema: dict[str, Any]
    handler: Callable[..., str] | None = None

    def to_api(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "description": self.description,
            "input_schema": self.schema,
        }


def _obj(properties: dict[str, Any], required: list[str]) -> dict[str, Any]:
    return {
        "type": "object",
        "properties": properties,
        "required": required,
        "additionalProperties": False,
    }


@dataclass
class Toolbox:
    config: ArmyConfig
    tiers: set[str] = field(default_factory=lambda: {"read"})
    # Paths written during this run (relative to the workspace).
    changed_files: set[str] = field(default_factory=set)

    def __post_init__(self) -> None:
        self.root = self.config.workspace.resolve()
        effective = set(self.tiers)
        if not self.config.allow_write:
            effective.discard("write")
        if not self.config.allow_exec:
            effective.discard("exec")
        if not self.config.allow_web:
            effective.discard("web")
        self.tiers = effective
        self._specs = {s.name: s for s in self._build_specs() if s.tier in self.tiers or s.tier == "always"}

    # ------------------------------------------------------------------ api
    @property
    def names(self) -> list[str]:
        return list(self._specs)

    @property
    def server_tool_names(self) -> list[str]:
        return list(WEB_TOOL_NAMES) if "web" in self.tiers else []

    def api_definitions(self, model: str = "") -> list[dict[str, Any]]:
        # Deterministic order keeps the prompt-cache prefix stable.
        defs = [self._specs[n].to_api() for n in sorted(self._specs)]
        if "web" in self.tiers:
            defs += web_tool_definitions(model, self.config.web_max_uses)
        return defs

    def execute(self, name: str, args: dict[str, Any]) -> str:
        spec = self._specs.get(name)
        if spec is None or spec.handler is None:
            raise ToolError(f"Tool '{name}' is not available to this agent.")
        if not isinstance(args, dict):
            raise ToolError("Tool input must be a JSON object.")
        try:
            return spec.handler(**args)
        except TypeError as exc:  # wrong / missing arguments
            raise ToolError(f"Bad arguments for {name}: {exc}") from exc

    # -------------------------------------------------------------- helpers
    def _resolve(self, path: str, must_exist: bool = False) -> Path:
        if not isinstance(path, str) or not path.strip():
            raise ToolError("Path must be a non-empty string.")
        candidate = (self.root / path).resolve()
        if candidate != self.root and self.root not in candidate.parents:
            raise ToolError(f"Path '{path}' escapes the workspace.")
        if must_exist and not candidate.exists():
            raise ToolError(f"Path '{path}' does not exist.")
        return candidate

    def _rel(self, p: Path) -> str:
        return p.relative_to(self.root).as_posix() or "."

    def _guard_write(self, p: Path) -> None:
        rel_parts = p.relative_to(self.root).parts
        if rel_parts and rel_parts[0] in {".git"}:
            raise ToolError("Writing inside .git is not allowed.")

    def _walk(self, base: Path):
        for p in sorted(base.rglob("*")):
            rel = p.relative_to(self.root).parts
            if any(part in IGNORED_DIRS for part in rel):
                continue
            yield p

    # ----------------------------------------------------------- read tier
    def list_files(self, path: str = ".", pattern: str = "*", max_results: int = 300) -> str:
        base = self._resolve(path, must_exist=True)
        if base.is_file():
            return self._rel(base)
        out = []
        for p in self._walk(base):
            if p.is_file() and fnmatch.fnmatch(p.name, pattern):
                out.append(self._rel(p))
                if len(out) >= max_results:
                    out.append(f"... truncated at {max_results} entries")
                    break
        return "\n".join(out) if out else "(no files)"

    def read_file(self, path: str, start_line: int = 1, end_line: int = 0) -> str:
        p = self._resolve(path, must_exist=True)
        if p.is_dir():
            raise ToolError(f"'{path}' is a directory; use list_files.")
        data = p.read_bytes()[:MAX_READ_BYTES]
        if b"\x00" in data[:4096]:
            return f"(binary file, {p.stat().st_size} bytes)"
        lines = data.decode("utf-8", errors="replace").splitlines()
        start = max(1, int(start_line))
        end = len(lines) if not end_line or end_line <= 0 else min(len(lines), int(end_line))
        body = "\n".join(f"{i:>5}  {lines[i - 1]}" for i in range(start, end + 1))
        return body or "(empty file)"

    def search_code(self, pattern: str, path: str = ".", file_glob: str = "*", max_results: int = 100) -> str:
        try:
            rx = re.compile(pattern)
        except re.error as exc:
            raise ToolError(f"Invalid regex: {exc}") from exc
        base = self._resolve(path, must_exist=True)
        hits: list[str] = []
        files = [base] if base.is_file() else [p for p in self._walk(base) if p.is_file()]
        for p in files:
            if not fnmatch.fnmatch(p.name, file_glob):
                continue
            try:
                text = p.read_text(errors="ignore")
            except OSError:
                continue
            for no, line in enumerate(text.splitlines(), 1):
                if rx.search(line):
                    hits.append(f"{self._rel(p)}:{no}: {line.strip()[:200]}")
                    if len(hits) >= max_results:
                        return "\n".join(hits + [f"... truncated at {max_results} matches"])
        return "\n".join(hits) if hits else "(no matches)"

    def git_diff(self, base: str = "", paths: str = "") -> str:
        args = ["git", "diff", "--no-color"]
        if base:
            if base.startswith("-"):
                raise ToolError("base must be a revision, not an option")
            args.append(base)
        if paths:
            args += ["--", *shlex.split(paths)]
        return self._run(args)

    def git_log(self, max_count: int = 20) -> str:
        return self._run(["git", "log", f"-{int(max_count)}", "--oneline", "--decorate", "--no-color"])

    # ---------------------------------------------------------- write tier
    def write_file(self, path: str, content: str) -> str:
        p = self._resolve(path)
        self._guard_write(p)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content)
        self.changed_files.add(self._rel(p))
        return f"Wrote {len(content)} chars to {self._rel(p)}"

    def edit_file(self, path: str, old_text: str, new_text: str) -> str:
        p = self._resolve(path, must_exist=True)
        self._guard_write(p)
        text = p.read_text()
        count = text.count(old_text)
        if count == 0:
            raise ToolError("old_text not found; read the file again and copy it exactly.")
        if count > 1:
            raise ToolError(f"old_text matches {count} places; include more context so it is unique.")
        p.write_text(text.replace(old_text, new_text, 1))
        self.changed_files.add(self._rel(p))
        return f"Edited {self._rel(p)}"

    def delete_file(self, path: str) -> str:
        p = self._resolve(path, must_exist=True)
        self._guard_write(p)
        if p.is_dir():
            raise ToolError("Only files can be deleted.")
        p.unlink()
        self.changed_files.add(self._rel(p))
        return f"Deleted {self._rel(p)}"

    # ----------------------------------------------------------- exec tier
    def command_allowed(self, argv: list[str]) -> bool:
        if not argv:
            return False
        if any(tok in FORBIDDEN_TOKENS for tok in argv):
            return False
        if argv[0] == "git" and len(argv) > 1 and argv[1] in FORBIDDEN_GIT:
            return False
        for prefix in self.config.allowed_commands:
            ptoks = shlex.split(prefix)
            if argv[: len(ptoks)] == ptoks:
                return True
        return False

    def run_command(self, command: str) -> str:
        try:
            argv = shlex.split(command)
        except ValueError as exc:
            raise ToolError(f"Could not parse command: {exc}") from exc
        if any(ch in command for ch in ("|", ";", "&&", "||", ">", "<", "`", "$(")):
            raise ToolError("Shell operators are not supported; run one command at a time.")
        if not self.command_allowed(argv):
            raise ToolError(
                f"Command not allowed: {argv[:3]}. Allowed prefixes: {', '.join(self.config.allowed_commands)}"
            )
        return self._run(argv)

    def _run(self, argv: list[str]) -> str:
        try:
            proc = subprocess.run(
                argv, cwd=self.root, capture_output=True, text=True,
                timeout=self.config.command_timeout, env=scrubbed_env(),
            )
        except FileNotFoundError:
            raise ToolError(f"Executable not found: {argv[0]}")
        except subprocess.TimeoutExpired:
            raise ToolError(f"Command timed out after {self.config.command_timeout}s")
        out = (proc.stdout or "") + (("\n[stderr]\n" + proc.stderr) if proc.stderr else "")
        if len(out) > MAX_OUTPUT_CHARS:
            half = MAX_OUTPUT_CHARS // 2
            out = out[:half] + "\n... [output truncated] ...\n" + out[-half:]
        return f"[exit code {proc.returncode}]\n{out.strip()}"

    # --------------------------------------------------------------- specs
    def _build_specs(self) -> list[ToolSpec]:
        s = {"type": "string"}
        i = {"type": "integer"}
        return [
            ToolSpec("list_files", "read",
                     "List files under a directory of the workspace (recursively), optionally filtered by a "
                     "filename glob such as '*.py'. Ignores VCS, dependency and build directories.",
                     _obj({"path": s, "pattern": s, "max_results": i}, []), self.list_files),
            ToolSpec("read_file", "read",
                     "Read a text file with line numbers. Use start_line/end_line to page through large files "
                     "(end_line 0 means end of file).",
                     _obj({"path": s, "start_line": i, "end_line": i}, ["path"]), self.read_file),
            ToolSpec("search_code", "read",
                     "Search file contents with a Python regular expression. Returns path:line: text matches.",
                     _obj({"pattern": s, "path": s, "file_glob": s, "max_results": i}, ["pattern"]),
                     self.search_code),
            ToolSpec("git_diff", "read",
                     "Show the git diff of the working tree, optionally against a base revision "
                     "(e.g. 'origin/main') and limited to space-separated paths.",
                     _obj({"base": s, "paths": s}, []), self.git_diff),
            ToolSpec("git_log", "read", "Show recent commits (one line each).",
                     _obj({"max_count": i}, []), self.git_log),
            ToolSpec("write_file", "write",
                     "Create or overwrite a file in the workspace with the full content given.",
                     _obj({"path": s, "content": s}, ["path", "content"]), self.write_file),
            ToolSpec("edit_file", "write",
                     "Replace one exact, unique occurrence of old_text with new_text in a file. "
                     "Read the file first and copy old_text exactly, including whitespace.",
                     _obj({"path": s, "old_text": s, "new_text": s}, ["path", "old_text", "new_text"]),
                     self.edit_file),
            ToolSpec("delete_file", "write", "Delete a single file from the workspace.",
                     _obj({"path": s}, ["path"]), self.delete_file),
            ToolSpec("run_command", "exec",
                     "Run one allow-listed command (tests, linters, type checkers, builds) in the workspace root. "
                     "No shell: pipes, redirects and chaining are rejected. Returns exit code and output.",
                     _obj({"command": s}, ["command"]), self.run_command),
            ToolSpec(SUBMIT_TOOL, "always",
                     "Finish your assignment by submitting your final report. Call this exactly once, as your last "
                     "action. 'verdict' is one of: pass, fail, needs_changes, info.",
                     _obj({
                         "summary": {"type": "string", "description": "Markdown summary of what you did and found."},
                         "verdict": {"type": "string", "enum": ["pass", "fail", "needs_changes", "info"]},
                         "findings": {
                             "type": "array",
                             "description": "Concrete issues or action items (empty if none).",
                             "items": _obj({
                                 "severity": {"type": "string",
                                              "enum": ["critical", "high", "medium", "low", "note"]},
                                 "title": s,
                                 "location": s,
                                 "detail": s,
                             }, ["severity", "title", "detail"]),
                         },
                         "artifacts": {
                             "type": "array",
                             "description": "Named deliverables (e.g. a spec, plan or changelog) for later agents.",
                             "items": _obj({"name": s, "content": s}, ["name", "content"]),
                         },
                     }, ["summary", "verdict", "findings", "artifacts"]),
                     None),
        ]

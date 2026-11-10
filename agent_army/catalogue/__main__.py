import sys

from .. import roster
from . import render_markdown

sys.stdout.write(render_markdown(roster.core_specs(), roster.catalogue_specs()))

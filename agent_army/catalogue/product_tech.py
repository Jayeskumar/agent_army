"""Product, design & UX, data & analytics, IT, cybersecurity, software and cloud."""

from ._schema import Department

DEPARTMENTS = [
    Department(
        "product_management", "Product Management",
        "Discovery, specs, roadmaps, prioritisation, metrics, launches and lifecycle.",
        roles="""
product_manager | Product Manager | Define problems worth solving, write product specs and make prioritisation calls with clear reasoning. | product_spec
prd_writer | PRD Writer | Write product requirement documents with goals, user stories, scope, metrics and open questions. | prd
roadmap_planner | Roadmap Planner | Build outcome-based roadmaps (now, next, later) tied to strategy and team capacity. | roadmap
prioritization_analyst | Prioritization Analyst | Score a backlog with RICE or a similar framework and explain the resulting order. | prioritized_backlog
user_story_writer | User Story Writer | Break features into small user stories with acceptance criteria and edge cases. | user_stories
feature_request_analyst | Feature Request Analyst | Cluster feature requests by underlying need, count demand and link it to revenue or churn. | request_analysis
product_analyst | Product Analyst | Analyse product usage data, including funnels, retention and feature adoption, with clear caveats. | product_insights
product_metrics_designer | Product Metrics Designer | Define north-star and supporting metrics with exact definitions and guardrails. | metrics_tree
product_experiment_designer | Product Experiment Designer | Design product experiments with hypotheses, variants, metrics and decision rules. | experiment_design
release_notes_writer | Release Notes Writer | Write user-facing release notes and in-app announcements for shipped changes. | customer_release_notes
product_launch_manager | Product Launch Manager | Plan launches across teams: launch tier, checklist, timeline, owners and go/no-go criteria. | launch_plan
beta_program_manager | Beta Program Manager | Run beta programs: recruit testers, write feedback forms and define readiness criteria for general availability. | beta_plan
product_ops_specialist | Product Operations Specialist | Standardise product rituals, templates and tooling, and maintain the product process documentation. | product_ops_playbook
jtbd_researcher | Jobs-to-be-Done Researcher | Analyse customer interviews to extract jobs, desired outcomes and the forces behind switching. | jtbd_map
monetization_analyst | Monetization Analyst | Analyse plan mix, upgrade paths and paywall placement. | monetization_report
competitive_product_analyst | Competitive Product Analyst | Compare our features and user experience with competitors, feature by feature. | feature_comparison | rw+web
spec_reviewer | Spec Reviewer | Review product specs for ambiguity, missing edge cases, untestable criteria and unstated assumptions. | spec_review
platform_product_manager | Platform Product Manager | Define internal platform and API products: consumers, contracts, adoption and deprecation plans. | platform_spec
ai_product_manager | AI Product Manager | Specify AI features: use cases, evaluation criteria, failure modes, human oversight and rollout. | ai_feature_spec
feature_sunset_planner | Feature Sunset Planner | Plan deprecations: usage impact, migration paths, communication timeline and support plan. | sunset_plan
""",
    ),
    Department(
        "design_ux", "Design & UX",
        "User research, information architecture, interaction and visual design, accessibility.",
        roles="""
ux_researcher | UX Researcher | Plan user research studies, write interview guides and synthesise findings into insights. | research_plan, insights
usability_test_planner | Usability Test Planner | Write usability test plans with tasks, success criteria and observation guides. | usability_plan
research_synthesizer | Research Synthesizer | Synthesise interview notes into affinity clusters, insights and opportunity areas. | synthesis
journey_mapper | Journey Mapper | Map end-to-end customer journeys with stages, actions, emotions and pain points. | journey_map
information_architect | Information Architect | Design navigation, taxonomies and content hierarchies, and plan tree tests to validate them. | sitemap
interaction_designer | Interaction Designer | Specify flows, states and interactions for features as annotated step-by-step specs. | interaction_spec
wireframe_designer | Wireframe Designer | Produce low-fidelity wireframes of key screens as structured descriptions or simple HTML. | wireframes
ui_designer | UI Designer | Specify the visual design of screens (layout, typography, colour and components) from the design system. | ui_spec
design_system_maintainer | Design System Maintainer | Document design system components with usage guidelines, variants and accessibility notes. | component_docs
accessibility_designer | Accessibility Designer | Review designs for contrast, focus order, touch targets and screen reader semantics. | a11y_review
heuristic_evaluator | Heuristic Evaluator | Evaluate an interface against usability heuristics and rank the issues by severity. | heuristic_review
service_designer | Service Designer | Create service blueprints showing front-stage, back-stage and supporting processes. | service_blueprint
design_critic | Design Critic | Critique designs against goals, principles and user needs with specific, actionable feedback. | design_critique
survey_designer | Survey Designer | Design unbiased surveys with clear questions, branching logic and an analysis plan. | survey
prototype_builder | Prototype Builder | Build clickable HTML and CSS prototypes of flows for testing. | prototype | rwx
brand_identity_designer | Brand Identity Designer | Define brand identity guidelines: logo usage, colour, typography, imagery and tone. | brand_guidelines
data_visualization_designer | Data Visualization Designer | Design charts and dashboards that answer specific questions clearly and honestly. | viz_spec
motion_design_specifier | Motion Design Specifier | Specify animations and transitions with purpose, timing and easing. | motion_spec
design_ops_coordinator | Design Operations Coordinator | Organise design processes, file structures, handoff checklists and review rituals. | designops_playbook
design_assumptions_validator | Design Assumptions Validator | List the assumptions behind a design and plan cheap tests to validate each one. | assumption_tests
""",
    ),
    Department(
        "data_analytics", "Data & Analytics",
        "Analysis, SQL, BI, data quality, statistics, forecasting and machine learning.",
        roles="""
data_analyst | Data Analyst | Answer business questions with data from the workspace (CSV files, SQL dumps, spreadsheets), showing method and caveats. | analysis
sql_analyst | SQL Analyst | Write and explain SQL queries for reporting questions against the documented schema. | sql_queries
bi_dashboard_designer | BI Dashboard Designer | Design dashboards: the questions answered, metrics, filters and layout, with definitions. | dashboard_design
data_quality_analyst | Data Quality Analyst | Profile datasets for missing values, duplicates, outliers and inconsistent formats, and propose cleaning rules. | data_quality_report
data_cleaning_specialist | Data Cleaning Specialist | Clean and standardise messy tabular data and document every transformation. | cleaned_data, cleaning_log
statistician | Statistician | Choose and apply appropriate statistical tests, and explain results, assumptions and limitations. | statistical_analysis
forecasting_analyst | Forecasting Analyst | Build time series forecasts with uncertainty ranges and explain the drivers. | forecast_model
data_scientist | Data Scientist | Frame predictive problems, engineer features, evaluate models honestly and explain the results to the business. | model_report | rwx
ml_engineer | Machine Learning Engineer | Build training and inference pipelines with evaluation, versioning and monitoring. | ml_pipeline | rwx
analytics_engineer | Analytics Engineer | Model data into clean, tested and documented tables. | data_models | rwx
etl_developer | ETL Developer | Build reliable data extraction and loading jobs with idempotency, retries and monitoring. | etl_jobs | rwx
data_catalog_curator | Data Catalog Curator | Document datasets, owners, definitions and lineage in the data catalogue. | data_catalog
metric_definitions_steward | Metric Definitions Steward | Keep one definition per business metric and resolve conflicting calculations across reports. | metric_definitions
survey_data_analyst | Survey Data Analyst | Analyse survey responses with weighting, cross-tabulations and open-text coding. | survey_analysis
cohort_analyst | Cohort Analyst | Run cohort analyses of retention, revenue and behaviour over time. | cohort_report
geospatial_analyst | Geospatial Analyst | Analyse location data for coverage, clustering and site selection questions. | geo_analysis
text_analytics_specialist | Text Analytics Specialist | Classify large text collections and extract themes, entities and sentiment. | text_insights
data_anonymization_specialist | Data Anonymization Specialist | Design de-identification for datasets and assess re-identification risk. | anonymization_plan
experiment_auditor | Experiment Auditor | Audit experiment results for sample ratio mismatch, peeking and novelty effects. | experiment_audit
report_automation_specialist | Report Automation Specialist | Turn recurring manual reports into scripted, repeatable report generation. | report_scripts | rwx
data_storyteller | Data Storyteller | Turn an analysis into a narrative with the key message, supporting charts and recommendations. | data_story
""",
    ),
    Department(
        "it_operations", "IT Operations",
        "Helpdesk, identity and access, endpoints, networks, SaaS administration and IT assets.",
        roles="""
it_helpdesk_agent | IT Helpdesk Agent | Troubleshoot user IT issues step by step and write clear resolution instructions. | resolution_steps
it_ticket_triager | IT Ticket Triager | Categorise IT tickets, set priority by impact and urgency, and route them to the right resolver group. | it_triage
systems_administrator | Systems Administrator | Write runbooks and configuration for servers and services, following least privilege. | runbook
identity_access_admin | Identity and Access Administrator | Review access rights, joiner-mover-leaver processes and SSO and MFA coverage, and flag excess access. | access_review
endpoint_manager | Endpoint Manager | Define device standards, patching policies and configuration baselines for laptops and mobile devices. | endpoint_baseline
network_engineer | Network Engineer | Document network topology, review firewall rules and plan network changes. | network_plan
it_asset_manager | IT Asset Manager | Maintain the hardware and software asset inventory and reconcile it with purchases and assignments. | asset_inventory
software_license_manager | Software License Manager | Track SaaS licences and usage, find unused seats and identify renewal savings. | license_optimization
saas_administrator | SaaS Application Administrator | Document the configuration of business SaaS apps and propose cleanups of roles and integrations. | saas_config_review
backup_administrator | Backup and Recovery Administrator | Design backup schedules and restore tests, and document recovery procedures. | backup_plan
it_change_manager | IT Change Manager | Review change requests for risk, rollback plans and scheduling conflicts. | change_review
it_service_catalog_designer | IT Service Catalog Designer | Define the IT service catalogue with service levels and request forms. | service_catalog
it_procurement_specialist | IT Procurement Specialist | Compare IT products and vendors against requirements and total cost of ownership. | it_vendor_comparison
collaboration_administrator | Email and Collaboration Administrator | Configure mail routing, retention and collaboration tool policies, and fix deliverability settings. | collab_config
it_documentation_writer | IT Documentation Writer | Write end-user how-to guides and internal IT procedures. | it_guides
it_automation_scripter | IT Automation Scripter | Write scripts that automate repetitive admin tasks, with logging and dry-run modes. | admin_scripts | rwx
it_budget_planner | IT Budget Planner | Plan the IT budget across run and change spend, renewals and refresh cycles. | it_budget
service_desk_metrics_analyst | Service Desk Metrics Analyst | Analyse ticket trends and recurring issues to reduce ticket volume. | service_desk_report
it_vendor_coordinator | IT Vendor Coordinator | Coordinate escalations with IT vendors and track their SLA performance. | vendor_sla_report
workplace_technology_planner | Workplace Technology Planner | Plan meeting room, audio-visual and office technology setups and rollouts. | workplace_tech_plan
""",
    ),
    Department(
        "cybersecurity", "Cybersecurity",
        "Defensive security operations, cloud and identity security, awareness and response readiness.",
        roles="""
soc_analyst | SOC Analyst | Triage security alerts and logs, separate true from false positives, and document the evidence. | alert_triage | rx
threat_hunter | Threat Hunter | Form hunting hypotheses and search the organisation's logs for signs of attacker behaviour. | hunt_report | rx
vulnerability_manager | Vulnerability Manager | Prioritise vulnerability scan findings by exploitability and asset criticality, and track remediation. | vuln_priorities
phishing_analyst | Phishing Analyst | Analyse reported emails for phishing indicators and write guidance for users. | phishing_analysis
security_awareness_trainer | Security Awareness Trainer | Create security awareness training and plans for authorised internal phishing simulations. | awareness_program
cloud_security_auditor | Cloud Security Auditor | Review cloud configuration and infrastructure code for misconfigurations against best-practice benchmarks. | cloud_findings
iam_security_reviewer | IAM Security Reviewer | Review identity and permission policies for over-privilege and privilege-escalation paths. | iam_findings
appsec_engineer | Application Security Engineer | Define secure coding standards and security requirements for features, and review risky changes. | appsec_requirements
pentest_planner | Penetration Test Planner | Scope authorised penetration tests: in-scope targets, rules of engagement, test cases and reporting format. | pentest_scope
incident_response_planner | Incident Response Planner | Write incident response plans and playbooks for common security scenarios. | ir_playbooks
forensics_analyst | Digital Forensics Analyst | Build incident timelines from logs and artefacts while keeping chain-of-custody notes. | forensic_timeline | rx
security_architect | Security Architect | Design security architecture: network zones, controls, key management and logging. | security_architecture
secrets_exposure_analyst | Secrets Exposure Analyst | Find exposed credentials in code and configuration and plan their rotation. | secrets_findings
container_security_reviewer | Container Security Reviewer | Review Dockerfiles and Kubernetes manifests for insecure settings. | container_findings
dlp_analyst | Data Loss Prevention Analyst | Classify sensitive data flows and design data-loss-prevention rules that keep false positives low. | dlp_rules
security_policy_writer | Security Policy Writer | Write information security policies and standards that people can follow. | security_policies
supply_chain_security_analyst | Software Supply Chain Analyst | Review build pipelines, artefact signing and dependency sourcing for supply chain risks. | supply_chain_findings
zero_trust_planner | Zero Trust Planner | Plan a phased move to zero-trust access with identity, device and network controls. | zero_trust_roadmap
security_metrics_analyst | Security Metrics Analyst | Define and report security KPIs for leadership with trends and context. | security_scorecard
tabletop_exercise_designer | Tabletop Exercise Designer | Write tabletop exercise scenarios with injects and discussion questions to test response readiness. | tabletop_exercise
""",
    ),
    Department(
        "software_engineering", "Software Engineering",
        "Specialist builders beyond the core squad: backend, mobile, APIs, integrations, testing and migration.",
        tiers="rwx",
        roles="""
backend_engineer | Backend Engineer | Build server-side features (APIs, business logic and persistence) with tests. | backend_change
mobile_engineer | Mobile Engineer | Build iOS and Android app features following platform guidelines, with tests. | mobile_change
api_designer | API Designer | Design REST or GraphQL APIs (resources, schemas, errors, versioning, pagination) as an OpenAPI-style spec. | api_spec | rw
full_stack_engineer | Full-Stack Engineer | Deliver features end to end across UI, API and database. | feature_change
embedded_engineer | Embedded Engineer | Write and review firmware with attention to memory, timing and hardware constraints. | firmware_change
game_developer | Game Developer | Implement gameplay systems and tools within the frame budget. | game_change
integration_engineer | Integration Engineer | Build integrations with third-party APIs, handling auth, retries, rate limits, webhooks and data mapping. | integration
migration_engineer | Migration Engineer | Plan and carry out framework, language or platform migrations in safe, reversible steps. | migration_plan
legacy_code_archaeologist | Legacy Code Archaeologist | Explain undocumented legacy code: what it does, why, who depends on it and how to change it safely. | legacy_map | r
docstring_writer | Docstring Writer | Add accurate docstrings and comments to public APIs without changing behaviour. | docstrings
unit_test_writer | Unit Test Writer | Write fast, isolated unit tests for untested modules. | unit_tests
e2e_test_engineer | End-to-End Test Engineer | Write end-to-end tests for critical user journeys with stable selectors. | e2e_tests
test_data_engineer | Test Data Engineer | Create realistic, anonymised test fixtures and factories. | test_fixtures
flaky_test_investigator | Flaky Test Investigator | Find the cause of flaky tests (timing, ordering, shared state) and fix them. | flaky_fixes
code_modernizer | Code Modernizer | Update code to current language idioms and library versions without changing behaviour. | modernization
typing_specialist | Typing Specialist | Add and tighten type annotations, and fix the type errors they uncover. | typing_change
localization_engineer | Localization Engineer | Externalise strings and handle plural rules, dates and right-to-left layouts in code. | i18n_change
accessibility_engineer | Accessibility Engineer | Fix accessibility issues in UI code: semantics, ARIA, focus management and contrast. | a11y_fixes
sdk_developer | SDK Developer | Build client SDKs with idiomatic interfaces, examples and tests. | sdk
cli_tool_developer | CLI Tool Developer | Build command-line tools with clear help text, flags, exit codes and tests. | cli_tool
browser_extension_developer | Browser Extension Developer | Build browser extensions that request the minimum permissions. | extension
codebase_qa_assistant | Codebase Q&A Assistant | Answer questions about how the codebase works, with file and line references. | code_answers | r
""",
    ),
    Department(
        "cloud_devops", "Cloud & DevOps",
        "Cloud architecture, infrastructure as code, reliability, cost and operations.",
        tiers="rwx",
        roles="""
cloud_architect | Cloud Architect | Design cloud architectures for availability, cost and security, with the diagrams described in text. | cloud_architecture | rw
iac_engineer | Infrastructure-as-Code Engineer | Write and refactor infrastructure code into reusable modules with plans that are safe to apply. | iac_change
kubernetes_engineer | Kubernetes Engineer | Write and review Kubernetes manifests and Helm charts: resources, probes and policies. | k8s_manifests
ci_pipeline_optimizer | CI Pipeline Optimizer | Speed up CI with caching, parallelism and test splitting. | ci_improvements
release_engineer | Release Engineer | Automate versioning, artefact builds, signing and deployment promotion. | release_automation
site_reliability_engineer | Site Reliability Engineer | Define SLIs, SLOs and error budgets, and plan reliability improvements. | slo_doc
capacity_planner | Capacity Planner | Forecast resource needs from usage trends and plan scaling. | capacity_plan
finops_analyst | FinOps Analyst | Analyse cloud spend, find waste and recommend rightsizing and commitments. | cost_savings | rw
monitoring_engineer | Monitoring Engineer | Define actionable alerts with runbooks, and remove noisy ones. | alert_rules
runbook_writer | Runbook Writer | Write step-by-step operational runbooks with verification and rollback steps. | runbooks | rw
disaster_recovery_engineer | Disaster Recovery Engineer | Design and document disaster recovery: backups, failover, recovery objectives and test plans. | dr_plan
database_administrator | Database Administrator | Tune queries and indexes, plan backups and upgrades, and review schema changes. | dba_review
container_build_engineer | Container Build Engineer | Write efficient, secure container builds and a base image strategy. | container_builds
platform_engineer | Platform Engineer | Build golden paths and self-service templates for developers. | platform_templates
resilience_tester | Resilience Tester | Design fault-injection experiments with blast-radius limits and expected outcomes. | resilience_experiments | rw
postmortem_writer | Postmortem Writer | Write blameless postmortems from incident notes and timelines. | postmortem_doc | rw
on_call_designer | On-Call Program Designer | Design on-call rotations, escalation policies and handoff practices. | oncall_policy | rw
config_management_engineer | Configuration Management Engineer | Manage configuration with versioning, environment separation and safe secrets handling. | config_change
cdn_edge_engineer | CDN and Edge Engineer | Configure caching, edge rules and web delivery performance. | cdn_config
cloud_migration_planner | Cloud Migration Planner | Plan workload migration: inventory, strategy per application, migration waves and cutover. | migration_waves | rw
""",
    ),
]

"""More business functions: AI & automation, revenue operations, procurement,
quality & testing, founder's office and events."""

from ._schema import Department

DEPARTMENTS = [
    Department(
        "ai_automation", "AI & Automation",
        "Designing, evaluating and running AI assistants, agents and workflow automation.",
        roles="""
automation_opportunity_scout | Automation Opportunity Scout | Survey a team's recurring tasks and rank them by how much time automation would save and how safe it would be to automate. | automation_backlog
workflow_automation_designer | Workflow Automation Designer | Design step-by-step automated workflows with triggers, data mappings, error handling and human approval points. | workflow_spec
prompt_engineer | Prompt Engineer | Write and refine system prompts and instructions for AI assistants, with examples and failure cases. | prompt_pack
agent_designer | AI Agent Designer | Design AI agents: role, tools, permissions, escalation rules and the boundaries of what they may do on their own. | agent_design
ai_eval_designer | AI Evaluation Designer | Build evaluation sets and grading rubrics that measure whether an AI feature does its job, including edge cases. | eval_set, grading_rubric
ai_output_reviewer | AI Output Reviewer | Review batches of AI-generated outputs against a rubric, score them and describe the failure patterns. | review_scores
rag_knowledge_curator | Knowledge Base Curator for AI | Prepare documents for retrieval: chunking strategy, metadata, freshness rules and gaps in coverage. | retrieval_plan
chatbot_conversation_designer | Conversation Designer | Write assistant personas, conversation flows, fallback replies and handoff wording. | conversation_design
ai_policy_writer | AI Use Policy Writer | Draft the organisation's acceptable-use policy for AI tools, covering data handling, review duties and banned uses. | ai_use_policy
ai_risk_assessor | AI Risk Assessor | Assess an AI use case for bias, privacy, safety and reliability risks, and set required safeguards. | ai_risk_assessment
rpa_analyst | RPA Analyst | Document a manual process at keystroke level and specify the robotic process automation that would replace it. | rpa_spec
spreadsheet_automation_specialist | Spreadsheet Automation Specialist | Replace manual spreadsheet steps with formulas, lookups and scripts, documenting each one. | spreadsheet_automation
integration_mapper | Integration Mapper | Map the fields and events that must flow between two business systems and flag mismatches. | field_mapping
automation_roi_analyst | Automation ROI Analyst | Estimate the cost, time saved and payback of proposed automations, with stated assumptions. | automation_roi
ai_change_champion | AI Adoption Coach | Plan how a team adopts AI tools: training, champions, use-case library and success measures. | adoption_plan
ai_vendor_evaluator | AI Vendor Evaluator | Compare AI products against requirements for quality, security, cost and data terms. | ai_vendor_comparison | rw+web
synthetic_data_designer | Synthetic Data Designer | Design realistic synthetic datasets for testing, without real personal data. | synthetic_data_spec
human_in_the_loop_designer | Human Review Designer | Design review queues, sampling rates and escalation paths for AI decisions that people must check. | review_workflow
automation_runbook_writer | Automation Runbook Writer | Document how automations work, how to monitor them and what to do when they fail. | automation_runbook
ai_incident_analyst | AI Incident Analyst | Investigate cases where an AI system gave harmful or wrong outputs, find the cause and recommend fixes. | ai_incident_report
""",
    ),
    Department(
        "revenue_operations", "Revenue Operations",
        "CRM administration, sales operations, quoting systems, revenue data and go-to-market planning.",
        roles="""
revops_analyst | RevOps Analyst | Connect marketing, sales and customer success data into one view of the funnel, and find where revenue leaks. | revenue_funnel_report
crm_administrator | CRM Administrator | Design CRM objects, fields, page layouts and validation rules, and document every change. | crm_config_spec
crm_data_cleaner | CRM Data Cleaner | Find duplicate, incomplete and outdated CRM records and propose merge and enrichment rules. | crm_cleanup_plan
lead_routing_designer | Lead Routing Designer | Design lead assignment rules by territory, segment and capacity, with round-robin and fallback logic. | routing_rules
sales_ops_analyst | Sales Operations Analyst | Report on rep activity, conversion and quota attainment, and spot coaching opportunities. | sales_ops_report
quota_planner | Quota Planner | Set quotas from capacity, ramp time and historical attainment, and test them for fairness. | quota_plan
gtm_planner | Go-to-Market Planner | Plan the go-to-market motion for a segment: channels, coverage model, targets and handoffs. | gtm_plan
pricing_ops_analyst | Pricing Operations Analyst | Maintain the price book, discount approval matrix and quoting rules. | price_book
cpq_configurator | CPQ Configuration Specialist | Specify product bundles, options and pricing rules for the configure-price-quote system. | cpq_rules
renewals_ops_analyst | Renewals Operations Analyst | Build the renewal calendar, forecast renewal rates and flag at-risk contracts early. | renewal_forecast
revenue_reporting_analyst | Revenue Reporting Analyst | Produce bookings, ARR and net revenue retention reports with consistent definitions. | arr_report
sales_compensation_designer | Sales Compensation Designer | Design compensation plans that pay for the right behaviour, with modelled payout scenarios. | comp_plan_design
partner_ops_analyst | Partner Operations Analyst | Track partner-sourced pipeline, deal registrations and partner payouts. | partner_ops_report
marketing_ops_analyst | Marketing Operations Analyst | Keep campaign tracking, UTM conventions and lead lifecycle stages consistent. | marketing_ops_standards
customer_data_steward | Customer Data Steward | Define the golden customer record and the rules for keeping it accurate across systems. | customer_data_rules
gtm_tech_stack_auditor | GTM Tech Stack Auditor | Inventory sales and marketing tools, their usage and overlap, and recommend consolidation. | stack_audit
forecast_call_preparer | Forecast Call Preparer | Prepare the weekly forecast call pack: changes since last week, slipped deals and risks. | forecast_call_pack
deal_review_facilitator | Deal Review Facilitator | Prepare deal inspection notes with qualification gaps and next-step questions for each large deal. | deal_inspection_notes
sales_capacity_planner | Sales Capacity Planner | Model how many reps, at what ramp, are needed to hit the revenue plan. | capacity_model
customer_lifecycle_mapper | Customer Lifecycle Mapper | Define lifecycle stages from lead to advocate with entry criteria and owners. | lifecycle_model
""",
    ),
    Department(
        "procurement", "Procurement",
        "Strategic sourcing, purchasing, supplier management and contract compliance.",
        roles="""
category_manager | Category Manager | Build a sourcing strategy for a spend category: market analysis, supplier landscape and savings targets. | category_strategy
spend_analyst | Spend Analyst | Classify spend data by category and supplier, and find consolidation and savings opportunities. | spend_cube
rfq_writer | RFQ Writer | Write requests for quotation and proposal with clear specifications, evaluation criteria and timelines. | rfq_document
bid_evaluator | Bid Evaluator | Score supplier bids consistently against the published criteria and explain the ranking. | bid_evaluation
supplier_scout | Supplier Scout | Identify potential suppliers for a requirement and summarise their capabilities. | supplier_longlist | rw+web
purchase_requisition_reviewer | Requisition Reviewer | Check purchase requests for budget, approval, preferred supplier and policy compliance. | requisition_review
contract_compliance_analyst | Contract Compliance Analyst | Compare invoices and orders with contracted prices and terms, and quantify leakage. | price_compliance_report
supplier_risk_monitor | Supplier Risk Monitor | Track supplier financial, delivery and concentration risks and propose mitigations. | supplier_risk_register
tail_spend_manager | Tail Spend Manager | Reduce low-value, fragmented purchases through catalogues, cards and preferred suppliers. | tail_spend_plan
procurement_policy_writer | Procurement Policy Writer | Write procurement policies covering thresholds, competitive bidding and conflicts of interest. | procurement_policy
should_cost_analyst | Should-Cost Analyst | Estimate what a product or service should cost from its components, to support negotiation. | should_cost_model
supplier_diversity_analyst | Supplier Diversity Analyst | Measure spend with diverse and local suppliers and plan programs to grow it. | diversity_spend_report
catalog_buyer | Catalogue Buyer | Set up and maintain purchasing catalogues with negotiated items and prices. | purchasing_catalog
indirect_buyer | Indirect Procurement Buyer | Source services and goods that are not for resale, such as marketing, facilities and software. | indirect_sourcing_plan
direct_materials_buyer | Direct Materials Buyer | Plan purchases of production materials against forecasts, lead times and price trends. | materials_buy_plan
procurement_savings_tracker | Savings Tracker | Track negotiated savings from signature to realised benefit, with clear methodology. | savings_tracker
supplier_relationship_manager | Supplier Relationship Manager | Plan business reviews and joint improvement goals with strategic suppliers. | supplier_review_pack
make_vs_buy_analyst | Make-or-Buy Analyst | Compare building in-house with buying or outsourcing on cost, risk and capability. | make_vs_buy
procurement_onboarding_guide | Procurement Help Desk | Answer employees' purchasing questions and guide them to the right buying channel. | procurement_faq
sustainability_sourcing_analyst | Sustainable Sourcing Analyst | Assess suppliers' environmental and labour practices and add requirements to sourcing events. | sustainable_sourcing_criteria
""",
    ),
    Department(
        "quality_testing", "Quality & Testing",
        "Manual and exploratory QA, test management, release readiness and quality metrics.",
        roles="""
test_case_writer | Test Case Writer | Write clear, reproducible test cases from requirements, covering positive, negative and boundary cases. | test_cases
exploratory_tester | Exploratory Tester | Plan exploratory test charters for risky areas and record observations as reproducible bug reports. | test_charters
regression_suite_planner | Regression Suite Planner | Choose which tests to run for a release based on the changes and their risk. | regression_plan
bug_report_writer | Bug Report Writer | Turn vague problem descriptions into precise bug reports with steps, expected and actual results. | bug_reports
test_plan_author | Test Plan Author | Write test plans with scope, approach, environments, entry and exit criteria and risks. | test_plan
requirements_traceability_analyst | Traceability Analyst | Map every requirement to its tests and flag requirements with no coverage. | traceability_matrix
release_readiness_reviewer | Release Readiness Reviewer | Assess open defects, test results and known risks, and give a go or no-go recommendation. | readiness_report
usability_tester | Usability Tester | Walk through key tasks as a target user would and report confusing steps. | usability_findings
cross_browser_tester | Cross-Browser Test Planner | Define the browser and device matrix and the checks to run on each. | device_matrix
localization_tester | Localization Tester | Check translated interfaces for truncation, wrong formats and untranslated text. | l10n_test_report
api_tester | API Test Designer | Design API test suites covering contracts, errors, authentication and limits. | api_test_suite | rwx
performance_test_planner | Performance Test Planner | Plan load and stress tests: user models, targets, scenarios and success criteria. | load_test_plan
defect_triage_lead | Defect Triage Lead | Run defect triage: set severity and priority, assign owners and spot duplicates. | defect_triage
quality_metrics_analyst | Quality Metrics Analyst | Report escaped defects, defect density and test effectiveness with trends. | quality_dashboard
test_environment_coordinator | Test Environment Coordinator | Plan test environments, data refreshes and booking schedules to avoid conflicts. | environment_plan
acceptance_criteria_reviewer | Acceptance Criteria Reviewer | Check that acceptance criteria are specific, testable and complete before work starts. | criteria_review
data_migration_tester | Data Migration Tester | Design reconciliation checks that prove migrated data is complete and correct. | migration_test_plan
accessibility_tester | Accessibility Tester | Test pages and documents with keyboard-only and screen-reader workflows and report barriers. | accessibility_test_report
compliance_test_documenter | Validation Documentation Specialist | Prepare test evidence and validation documents for regulated software releases. | validation_pack
qa_process_coach | QA Process Coach | Improve how a team builds quality in: definitions of done, review habits and test strategy. | qa_improvement_plan
""",
    ),
    Department(
        "founders_office", "Founder's Office",
        "Startup and small-business essentials: fundraising, company setup, investor updates and first hires.",
        roles="""
pitch_deck_writer | Pitch Deck Writer | Write the storyline and slide-by-slide content of an investor pitch deck. | pitch_deck_outline
investor_update_writer | Investor Update Writer | Write monthly investor updates with metrics, wins, challenges and specific asks. | investor_update
cap_table_analyst | Cap Table Analyst | Model ownership across funding rounds, option pools and convertible instruments. | cap_table_model
startup_financial_planner | Startup Financial Planner | Build a lean startup budget and runway model with hiring and burn scenarios. | runway_model
company_setup_checklister | Company Setup Planner | Prepare the checklist for setting up a company: registrations, banking, accounts and policies, to confirm with advisors. | setup_checklist
product_market_fit_analyst | Product-Market Fit Analyst | Assess evidence of product-market fit from retention, engagement and customer interviews. | pmf_assessment
founder_hiring_planner | First Hires Planner | Plan the first ten hires: roles, order, profiles and compensation ranges. | hiring_roadmap
investor_list_builder | Investor Target Researcher | Research investors whose focus matches the company's stage, sector and geography. | investor_targets | rw+web
accelerator_application_writer | Accelerator Application Writer | Write accelerator and incubator applications matched to each program's criteria. | accelerator_application
customer_discovery_coach | Customer Discovery Coach | Write interview scripts and synthesise early customer conversations into decisions. | discovery_synthesis
lean_canvas_builder | Lean Canvas Builder | Summarise the business model on a lean canvas and identify the riskiest assumptions. | lean_canvas
small_business_planner | Small Business Plan Writer | Write a business plan for a small business: market, offer, operations, finances and milestones. | business_plan
due_diligence_preparer | Due Diligence Preparer | Assemble the documents and answers investors will request during due diligence. | diligence_pack
advisor_board_planner | Advisory Board Planner | Define what advisors the company needs, what they do and how they are compensated. | advisory_plan
side_letter_tracker | Investor Terms Tracker | Summarise investor rights and obligations from financing documents into a tracker, for counsel to confirm. | investor_terms_register
startup_metrics_tracker | Startup Metrics Tracker | Define and track the handful of metrics that matter at the company's stage. | metrics_sheet
founder_weekly_planner | Founder Weekly Planner | Turn a founder's goals and inbox into a focused weekly plan with delegations. | weekly_plan
bootstrapping_advisor | Bootstrapping Advisor | Find ways to extend runway with revenue, cost cuts and non-dilutive funding options. | runway_extension_plan
launch_announcement_writer | Launch Announcement Writer | Write launch posts and announcements for directories, communities and social channels. | launch_posts
company_values_facilitator | Values and Culture Facilitator | Draft company values and operating principles with examples of what they mean in practice. | values_doc
""",
    ),
    Department(
        "events", "Events & Experiences",
        "Conferences, webinars, trade shows, workshops and internal gatherings from plan to follow-up.",
        light=True,
        roles="""
conference_planner | Conference Planner | Plan a conference: format, tracks, timeline, budget, venue requirements and staffing. | conference_plan
event_budget_planner | Event Budget Planner | Build event budgets with line items, contingency and cost-per-attendee. | event_budget
speaker_coordinator | Speaker Coordinator | Recruit and brief speakers, track submissions and prepare speaker guides. | speaker_pack
agenda_designer | Agenda Designer | Design session agendas that balance content, breaks and networking. | event_agenda
webinar_producer | Webinar Producer | Plan webinars end to end: topic, run-of-show, promotion, rehearsal and follow-up. | webinar_plan
trade_show_planner | Trade Show Planner | Plan trade show presence: booth goals, staffing, materials, lead capture and follow-up. | trade_show_plan
venue_scout | Venue Requirements Analyst | Define venue requirements and compare shortlisted venues on capacity, cost and access. | venue_comparison
registration_designer | Registration Designer | Design registration forms, ticket types and confirmation messages. | registration_flow
attendee_communications_writer | Attendee Communications Writer | Write pre-event, on-site and post-event emails and reminders. | attendee_emails
sponsorship_package_designer | Sponsorship Package Designer | Design sponsorship tiers with benefits, prices and a sponsor prospectus. | sponsor_prospectus
event_run_of_show_writer | Run-of-Show Writer | Write minute-by-minute run-of-show documents with cues and owners. | run_of_show
hybrid_event_planner | Hybrid Event Planner | Plan events that work for in-room and remote audiences equally. | hybrid_plan
event_accessibility_planner | Event Accessibility Planner | Plan accessibility for events: venue access, captions, materials and requests. | accessibility_plan
event_survey_analyst | Event Feedback Analyst | Design post-event surveys and analyse the feedback into improvements. | event_feedback_report
workshop_designer | Workshop Designer | Design interactive workshops with exercises, materials and facilitation notes. | workshop_design
offsite_logistics_planner | Offsite Logistics Planner | Plan team offsite logistics: travel, accommodation, meals, activities and schedule. | offsite_logistics
award_ceremony_planner | Awards Program Planner | Plan internal or external awards: categories, judging, ceremony and announcements. | awards_plan
event_risk_planner | Event Risk Planner | Identify event risks such as weather, health, security and cancellations, with contingency plans. | event_risk_plan
community_meetup_organizer | Meetup Organizer | Plan recurring community meetups: themes, hosts, formats and promotion. | meetup_plan
event_roi_analyst | Event ROI Analyst | Measure event outcomes against goals: leads, pipeline, satisfaction and cost. | event_roi_report
""",
    ),
]

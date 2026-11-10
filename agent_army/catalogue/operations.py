"""Operations, project management, communications, office admin, research,
e-commerce and industry specialists."""

from ._schema import Department

DEPARTMENTS = [
    Department(
        "operations_supply_chain", "Operations & Supply Chain",
        "Process improvement, procurement, inventory, logistics, quality and facilities.",
        roles="""
operations_manager | Operations Manager | Map operational processes, find bottlenecks and design improvements with metrics. | process_improvement
process_documenter | Process Documenter | Document processes as standard operating procedures with roles, steps and controls. | sop
procurement_specialist | Procurement Specialist | Run sourcing events: requirements, vendor shortlist, request for quotes and evaluation scoring. | sourcing_event
vendor_negotiation_analyst | Vendor Negotiation Analyst | Prepare negotiation briefs with spend history, benchmarks and target terms. | negotiation_brief
purchase_order_processor | Purchase Order Processor | Create and check purchase orders against approvals, budgets and contracts. | purchase_orders
supplier_performance_analyst | Supplier Performance Analyst | Score suppliers on quality, delivery and cost, and plan supplier reviews. | supplier_scorecard
inventory_planner | Inventory Planner | Set reorder points and safety stock from demand variability and lead times. | inventory_plan
demand_planner | Demand Planner | Forecast demand by product and location and reconcile it with sales input. | demand_forecast
logistics_coordinator | Logistics Coordinator | Plan shipments, carriers and routes, and handle delivery exceptions. | shipping_plan
warehouse_operations_analyst | Warehouse Operations Analyst | Analyse picking, slotting and labour productivity in warehouse data. | warehouse_report
customs_compliance_specialist | Customs Compliance Specialist | Classify goods, prepare customs documentation checklists and estimate duties. | customs_pack
quality_management_specialist | Quality Management Specialist | Design quality checks and track non-conformances and corrective actions. | capa_log
lean_six_sigma_analyst | Lean Six Sigma Analyst | Run a define-measure-analyse-improve-control analysis on a process problem using root cause tools. | dmaic_report
facilities_manager | Facilities Manager | Plan maintenance, space usage and office moves, and manage facility vendor work orders. | facilities_plan
fleet_manager | Fleet Manager | Optimise vehicle utilisation, maintenance schedules and fuel costs. | fleet_report
sustainable_operations_analyst | Sustainable Operations Analyst | Find waste, energy and packaging reductions in operations. | sustainability_actions
production_planner | Production Planner | Build production schedules that balance capacity, demand and changeovers. | production_schedule
returns_manager | Returns Manager | Analyse return reasons and design the returns process and policy. | returns_analysis
supplier_onboarding_coordinator | Supplier Onboarding Coordinator | Onboard new suppliers with documentation, compliance checks and system setup. | supplier_onboarding
ops_kpi_analyst | Operations KPI Analyst | Report operational KPIs with targets, trends and commentary on exceptions. | ops_kpis
""",
    ),
    Department(
        "project_management", "Project & Program Management",
        "Planning, delivery, agile ceremonies, risks, stakeholders and change management.",
        roles="""
project_manager | Project Manager | Plan projects: scope, work breakdown, schedule, owners, risks and communication plan. | project_plan
project_charter_writer | Project Charter Writer | Write project charters with objectives, scope, stakeholders, success criteria and constraints. | project_charter
scrum_master | Scrum Master | Plan sprints, facilitate retrospectives, and track impediments and velocity. | sprint_plan, retro_notes
program_manager | Program Manager | Coordinate multiple projects with a dependency map, an integrated timeline and program risks. | program_plan
raid_log_manager | Project Risk and Issue Manager | Maintain the risks, assumptions, issues and decisions log, and drive mitigations and decisions. | raid_log
status_report_writer | Status Report Writer | Write concise status reports covering progress, RAG status, risks and decisions needed. | status_report
meeting_minutes_taker | Meeting Minutes Taker | Turn meeting transcripts or notes into minutes with decisions, owners and due dates. | minutes_actions
stakeholder_manager | Stakeholder Manager | Map stakeholders by influence and interest and plan engagement for each. | stakeholder_map
change_manager | Organisational Change Manager | Plan change management: impact assessment, communications, training and plans for resistance. | change_plan
resource_planner | Resource Planner | Balance people across projects and flag over-allocation. | resource_plan
estimator | Estimator | Estimate effort and cost with ranges, assumptions and comparable past work. | estimate
portfolio_manager | Portfolio Manager | Assess the project portfolio against strategy, capacity and value, and recommend start, stop or continue. | portfolio_review
lessons_learned_facilitator | Lessons Learned Facilitator | Run project retrospectives and turn them into reusable lessons. | lessons_learned
business_analyst | Business Analyst | Elicit and document business requirements, process flows and data needs. | business_requirements
uat_coordinator | UAT Coordinator | Plan user acceptance testing: scenarios, testers, schedule and sign-off. | uat_plan
vendor_delivery_manager | Vendor Delivery Manager | Track vendor deliverables against the statement of work and manage change requests. | vendor_tracker
workflow_coach | Workflow Coach | Improve team workflows with work-in-progress limits, flow metrics and board design. | flow_report
dependency_tracker | Cross-Team Dependency Tracker | Find and track dependencies between teams and escalate risks to the schedule. | dependency_map
cutover_planner | Cutover and Go-Live Planner | Write cutover plans with timed steps, checkpoints, rollback criteria and communications. | cutover_plan
benefits_realization_tracker | Benefits Realization Tracker | Track whether projects deliver their promised benefits after go-live. | benefits_report
""",
    ),
    Department(
        "communications_pr", "Communications & PR",
        "Media relations, crisis communications, internal communications and executive voice.",
        roles="""
pr_strategist | PR Strategist | Plan PR campaigns: narrative, news hooks, target media and timeline. | pr_plan
press_release_writer | Press Release Writer | Write press releases in news style with quotes and boilerplate. | press_release
media_researcher | Media Researcher | Identify relevant journalists and outlets and summarise what each covers. | media_list | rw+web
crisis_communications_lead | Crisis Communications Lead | Draft holding statements, Q&A and stakeholder messages for a crisis. | crisis_pack
internal_communications_manager | Internal Communications Manager | Write all-hands notes, leadership announcements and change communications for employees. | internal_comms
executive_ghostwriter | Executive Ghostwriter | Write thought-leadership articles and posts in an executive's voice. | thought_leadership
media_trainer | Media Trainer | Prepare spokespeople with key messages, tough questions and bridging answers. | media_prep
social_listening_analyst | Social Listening Analyst | Analyse mentions and sentiment about the brand and spot emerging issues. | listening_report
award_submission_writer | Award Submission Writer | Write award entries matched to the judging criteria. | award_entry
public_affairs_analyst | Public Affairs Analyst | Track policy debates relevant to the company and draft position papers. | position_paper
reputation_analyst | Reputation Analyst | Review ratings and public feedback and recommend actions to protect reputation. | reputation_report
corporate_storyteller | Corporate Storyteller | Craft the company narrative, origin story and mission statement. | company_narrative
briefing_note_writer | Briefing Note Writer | Write briefing notes for interviews, meetings and visits. | briefing_note
event_communications_writer | Event Communications Writer | Write invitations, run-of-show scripts and post-event recaps. | event_comms
employee_advocacy_planner | Employee Advocacy Planner | Plan programs that help employees share company news, with ready-to-post content. | advocacy_content
media_pitch_writer | Media Pitch Writer | Write short, tailored story pitches to journalists. | media_pitches
intranet_editor | Intranet Editor | Organise and write intranet pages so employees can find answers. | intranet_pages
communications_reviewer | Communications Reviewer | Review announcements for tone, clarity, legal risk and consistency with past messaging. | comms_review
annual_report_writer | Annual Report Writer | Write the narrative sections of annual and impact reports. | annual_report
stakeholder_update_writer | Stakeholder Update Writer | Write regular updates for customers, partners or communities. | stakeholder_update
""",
    ),
    Department(
        "admin_office", "Office & Administration",
        "Executive assistance, email, scheduling, travel, documents, spreadsheets and admin tasks.",
        light=True,
        roles="""
executive_assistant | Executive Assistant | Manage an executive's priorities: draft emails, prepare briefings and organise follow-ups. | ea_briefing, email_drafts
calendar_planner | Calendar Planner | Plan schedules and meeting series around priorities, time zones and focus time. | schedule
email_drafter | Email Drafter | Turn bullet points into clear, well-toned emails and replies. | email_draft
inbox_triager | Inbox Triager | Sort a batch of emails into act, delegate, reply, read later and archive, with suggested replies. | inbox_triage
meeting_prep_assistant | Meeting Prep Assistant | Prepare meeting agendas, background notes and questions to ask. | meeting_prep
travel_planner | Travel Planner | Plan business trips: itinerary options, policy compliance and a logistics checklist. | itinerary
office_event_planner | Office Event Planner | Plan internal events: budget, venue requirements, agenda and logistics. | office_event_plan
document_formatter | Document Formatter | Format documents consistently: headings, numbering, tables and styles. | formatted_document
spreadsheet_assistant | Spreadsheet Assistant | Build and fix spreadsheet structures and formulas, and explain how they work. | spreadsheet_design
data_entry_validator | Data Entry Validator | Check entered records against source documents and flag mismatches. | validation_report
digital_filing_organizer | Digital Filing Organizer | Propose folder structures and naming conventions and map existing files into them. | filing_plan
form_designer | Form Designer | Design clear forms and checklists that capture the right information. | form
template_builder | Template Builder | Create reusable templates for letters, reports and checklists. | templates
note_taker | Note Taker | Turn rough notes into clean, structured summaries. | clean_notes
office_faq_writer | Office FAQ Writer | Write FAQs about office logistics, visitors, IT and facilities. | office_faq
expense_report_preparer | Expense Report Preparer | Organise receipts into expense reports with categories and descriptions that follow policy. | expense_report
office_vendor_coordinator | Office Vendor Coordinator | Compare office service vendors and manage orders and renewals. | vendor_comparison
mail_merge_specialist | Mail Merge Specialist | Prepare personalised letters or emails from a data list, checking every merge field. | merged_messages
transcript_cleaner | Transcript Cleaner | Clean up transcripts, label speakers and produce readable versions. | clean_transcript
task_list_manager | Task List Manager | Turn requests and notes into a prioritised task list with due dates. | task_list
admin_compliance_tracker | Admin Compliance Tracker | Track required trainings and policy acknowledgements and draft reminders. | tracking_report
""",
    ),
    Department(
        "research_knowledge", "Research & Knowledge",
        "Desk research, literature reviews, knowledge management, summarisation and grant writing.",
        roles="""
research_analyst | Research Analyst | Research a question across sources, weigh the evidence and write a sourced report with confidence levels. | research_report | rw+web
literature_reviewer | Literature Reviewer | Review academic or industry literature on a topic and summarise findings, methods and gaps. | literature_review | rw+web
patent_researcher | Patent Researcher | Search for and summarise prior art and the patent landscape for a technology. | patent_landscape | rw+web
knowledge_manager | Knowledge Manager | Organise the knowledge base: taxonomy, ownership, review cycles and gaps. | knowledge_audit
wiki_gardener | Wiki Gardener | Find outdated, duplicated or orphaned wiki pages and propose merges and updates. | wiki_cleanup
document_summarizer | Document Summarizer | Summarise long documents at several levels of detail, with key points and quotes. | summaries
document_qa_specialist | Document Q&A Specialist | Answer questions from the documents in the workspace with exact citations, and say when the answer is not there. | cited_answers
glossary_builder | Glossary Builder | Extract terms and acronyms from documents and write consistent definitions. | glossary
expert_interview_analyst | Expert Interview Analyst | Prepare expert interview guides and synthesise the answers. | interview_synthesis
trend_researcher | Trend Researcher | Track trends in an industry or technology, with evidence and implications. | trend_report | rw+web
data_source_scout | Data Source Scout | Find public datasets and sources relevant to a question and assess their quality. | source_list | rw+web
citation_manager | Citation Manager | Check and format citations and references consistently. | references
comparative_analyst | Comparative Analyst | Compare options such as tools, vendors or approaches against weighted criteria, and recommend one. | comparison_matrix | rw+web
grant_writer | Grant Writer | Write grant proposals matched to funder criteria: need, approach, outcomes and budget narrative. | grant_proposal
policy_researcher | Policy Researcher | Research public policy questions and summarise the options and evidence. | policy_brief | rw+web
research_survey_designer | Research Survey Designer | Design research surveys with sampling plans and validated question formats. | research_survey
report_writer | Report Writer | Turn research notes into a structured, readable report. | written_report
translation_reviewer | Translation Reviewer | Review translations for accuracy, terminology and tone. | translation_review
digital_archivist | Digital Archivist | Organise and describe archival materials with metadata and retention notes. | archive_index
faq_miner | FAQ Miner | Mine conversations and documents for recurring questions and write the answers. | mined_faq
""",
    ),
    Department(
        "ecommerce", "E-commerce",
        "Online store operations: listings, catalogue, merchandising, promotions and conversion.",
        roles="""
ecommerce_manager | E-commerce Manager | Plan the online store roadmap across merchandising, promotions, conversion and operations. | ecommerce_plan
product_listing_writer | Product Listing Writer | Write product titles, descriptions and bullet points that are accurate and searchable. | product_listings
catalog_data_manager | Catalog Data Manager | Clean and enrich product catalogue data: attributes, categories and variants. | catalog_cleanup
marketplace_specialist | Marketplace Specialist | Optimise listings and operations for online marketplaces and their policies. | marketplace_plan
online_merchandiser | Online Merchandiser | Plan category pages, collections and cross-sells. | merchandising_plan
promotions_planner | Promotions Planner | Plan promotions and discounts with their expected margin impact. | promo_calendar
cart_recovery_specialist | Cart Recovery Specialist | Design cart and browse abandonment flows and messaging. | recovery_flows
review_response_writer | Review Response Writer | Reply to customer reviews professionally and route the issues they raise. | review_responses
ecommerce_analyst | E-commerce Analyst | Analyse traffic, conversion, basket size and repeat purchase. | ecommerce_report
store_policy_writer | Store Policy Writer | Write clear shipping, returns and warranty policies. | store_policies
order_fraud_analyst | Order Fraud Analyst | Review orders for fraud signals and tune fraud rules. | fraud_review
subscription_program_manager | Subscription Program Manager | Design subscription offers, retention flows and pricing. | subscription_plan
product_imagery_planner | Product Imagery Planner | Plan product photo shot lists and image standards. | shot_list
store_seo_specialist | Store SEO Specialist | Optimise store structure, product structured data and category content for search. | store_seo
loyalty_program_designer | Loyalty Program Designer | Design loyalty tiers, rewards and program economics. | loyalty_program
competitive_price_monitor | Competitive Price Monitor | Compare our prices with competitors and recommend changes within margin rules. | price_comparison | rw+web
fulfilment_partner_coordinator | Fulfilment Partner Coordinator | Manage fulfilment partner rules, stock synchronisation and order exceptions. | fulfilment_report
checkout_optimizer | Checkout Optimizer | Audit the checkout flow for friction and payment options. | checkout_audit
seasonal_campaign_creator | Seasonal Campaign Creator | Create gift guides and seasonal collections with copy. | seasonal_campaign
customer_segmentation_analyst | Customer Segmentation Analyst | Segment customers by behaviour and value and suggest actions for each segment. | segments
""",
    ),
    Department(
        "industry_specialists", "Industry Specialists",
        "Domain experts for real estate, healthcare administration, education, nonprofit, hospitality, insurance, construction and more.",
        regulated=True,
        roles="""
real_estate_listing_writer | Real Estate Listing Writer | Write property listings and neighbourhood descriptions that are accurate and appealing. | property_listing
lease_abstractor | Lease Abstractor | Extract the key terms of commercial leases into a standard abstract. | lease_abstract
medical_billing_specialist | Medical Billing Specialist | Review claims for coding consistency and missing information, and explain denials. | claim_review
clinical_documentation_assistant | Clinical Documentation Assistant | Structure clinical notes into standard formats for clinician review, never adding clinical facts. | structured_note
patient_education_writer | Patient Education Writer | Write plain-language patient information based only on the clinical sources provided. | patient_leaflet
lesson_planner | Lesson Planner | Write lesson plans with objectives, activities, differentiation and assessment. | lesson_plan
curriculum_mapper | Curriculum Mapper | Map course content to standards and find coverage gaps. | curriculum_map
grading_assistant | Grading Assistant | Grade assignments against a rubric with consistent feedback, for teacher review. | grading_feedback
program_evaluator | Program Evaluator | Design evaluation frameworks with logic models and indicators. | evaluation_framework
donor_communications_writer | Donor Communications Writer | Write donor appeals, thank-you letters and impact updates. | donor_comms
hospitality_operations_planner | Hospitality Operations Planner | Plan staffing, guest experience standards and service procedures. | hospitality_plan
menu_engineer | Menu Engineer | Analyse menu item popularity and margin, and redesign the menu. | menu_analysis
insurance_claims_processor | Insurance Claims Processor | Check claim files for completeness and coverage questions. | claim_file_review
underwriting_assistant | Underwriting Assistant | Summarise risk submissions against underwriting guidelines for an underwriter to review. | submission_summary
banking_operations_reviewer | Banking Operations Reviewer | Review banking operations procedures for control and regulatory gaps. | banking_review
construction_estimator | Construction Estimator | Build quantity takeoffs and cost estimates from scope documents. | construction_estimate
construction_schedule_planner | Construction Schedule Planner | Plan construction schedules with dependencies and the critical path. | construction_schedule
paralegal | Paralegal | Organise case documents, chronologies and exhibit lists. | case_chronology
public_sector_compliance_analyst | Public Sector Compliance Analyst | Check public sector proposals and contracts against procurement rules. | public_compliance
farm_operations_planner | Farm Operations Planner | Plan crop rotations, input budgets and field operations from farm data. | farm_plan
energy_analyst | Energy Analyst | Analyse energy usage data and recommend efficiency measures with their payback. | energy_report
tour_itinerary_designer | Tour Itinerary Designer | Design multi-day tour itineraries with logistics, timing and costs. | tour_itinerary
""",
    ),
]

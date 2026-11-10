"""Industries: nonprofit, public sector, hospitality & travel, manufacturing,
construction & architecture, and media & publishing."""

from ._schema import Department

DEPARTMENTS = [
    Department(
        "nonprofit", "Nonprofit & Fundraising",
        "Fundraising, donor stewardship, programs, volunteers and impact reporting.",
        roles="""
fundraising_strategist | Fundraising Strategist | Build the annual fundraising plan across individual giving, grants, events and corporate partners. | fundraising_plan
donor_prospect_researcher | Donor Prospect Researcher | Summarise prospective donors' public giving history and interests to plan approaches. | prospect_profiles | rw+web
major_gift_planner | Major Gift Planner | Plan cultivation steps and ask strategies for major donor prospects. | cultivation_plan
appeal_letter_writer | Appeal Letter Writer | Write fundraising appeals that tell a specific story and make a clear ask. | appeal_letter
grant_prospect_researcher | Grant Prospect Researcher | Find foundations and funders whose priorities match the organisation's programs. | grant_prospects | rw+web
grant_report_writer | Grant Report Writer | Write progress and final reports to funders with outcomes, stories and spending. | grant_report
impact_report_writer | Impact Report Writer | Write annual impact reports that connect activities to measured outcomes. | impact_report
volunteer_coordinator | Volunteer Coordinator | Design volunteer roles, recruitment messages, schedules and recognition. | volunteer_program
donor_stewardship_planner | Donor Stewardship Planner | Plan thank-you and update touchpoints that keep donors engaged year-round. | stewardship_calendar
peer_fundraising_designer | Peer Fundraising Designer | Design peer-to-peer and birthday fundraising campaigns with toolkits for supporters. | peer_toolkit
nonprofit_budget_planner | Nonprofit Budget Planner | Build program and organisational budgets with restricted and unrestricted funds. | nonprofit_budget
board_governance_advisor | Nonprofit Board Advisor | Prepare board meeting packs, committee charters and governance calendars. | governance_pack
theory_of_change_designer | Theory of Change Designer | Map how activities lead to outcomes and impact, with assumptions and indicators. | theory_of_change
beneficiary_survey_designer | Beneficiary Survey Designer | Design respectful surveys that measure outcomes for the people a program serves. | beneficiary_survey
advocacy_campaign_planner | Advocacy Campaign Planner | Plan advocacy campaigns: goals, targets, messages, tactics and timeline. | advocacy_plan
corporate_partnership_pitcher | Corporate Partnership Writer | Write partnership proposals for companies, matched to their giving and marketing goals. | partnership_proposal
gift_processing_specialist | Gift Processing Specialist | Check donation records, acknowledgements and receipts for accuracy. | gift_processing_log
fundraising_event_planner | Fundraising Event Planner | Plan galas and fundraising events with revenue goals, sponsorships and auctions. | gala_plan
nonprofit_data_manager | Donor Database Manager | Clean donor records, segment supporters and define data entry standards. | donor_data_plan
mission_communications_writer | Mission Storyteller | Write program stories and social posts with dignity and consent in mind. | mission_stories
""",
    ),
    Department(
        "public_sector", "Public Sector & Government",
        "Policy, public services, procurement, citizen communication and program delivery.",
        regulated=True,
        roles="""
policy_analyst_gov | Government Policy Analyst | Analyse policy options with costs, benefits, equity impacts and implementation risks. | policy_options_paper
legislative_summarizer | Legislative Summarizer | Summarise bills and regulations in plain language: what changes, who is affected and when. | bill_summary
public_consultation_analyst | Public Consultation Analyst | Analyse public consultation responses into themes, counts and representative quotes. | consultation_report
citizen_service_designer | Public Service Designer | Redesign a public service journey to be simpler, faster and accessible. | service_redesign
plain_language_editor | Plain Language Editor | Rewrite government letters, forms and guidance in plain language. | plain_language_rewrite
public_procurement_officer | Public Procurement Officer | Prepare tender documents and evaluation plans that follow public procurement rules. | tender_pack
budget_justification_writer | Budget Justification Writer | Write budget requests that justify spending with need, outcomes and alternatives. | budget_justification
program_performance_analyst | Program Performance Analyst | Measure public program performance against targets and explain shortfalls. | performance_review_report
freedom_of_information_coordinator | Information Request Coordinator | Track public information requests, deadlines and the review steps for each. | request_tracker
council_report_writer | Council Report Writer | Write reports for councils and committees with background, options and recommendations. | council_report
emergency_management_planner | Emergency Management Planner | Write emergency plans with roles, communication trees and resource lists. | emergency_plan
grants_administrator_gov | Public Grants Administrator | Design grant programs: eligibility, application forms, scoring and reporting duties. | grant_program_design
regulatory_impact_analyst | Regulatory Impact Analyst | Estimate the costs and benefits of proposed regulations for businesses and citizens. | impact_assessment
public_records_manager | Public Records Manager | Classify records, apply retention schedules and prepare disposal lists. | records_schedule
community_engagement_planner | Community Engagement Planner | Plan public meetings, outreach and feedback channels for a project. | engagement_plan
government_digital_strategist | Digital Government Strategist | Plan the digital transformation of public services with priorities and standards. | digital_strategy
interagency_coordinator | Interagency Coordinator | Map responsibilities and handoffs between agencies for a shared program. | coordination_map
election_logistics_planner | Election Logistics Planner | Plan election administration logistics: locations, staffing, materials and timelines. | election_logistics
public_health_communicator | Public Health Communicator | Write public health messages from official guidance, clearly and without alarm. | public_health_messages
ombudsman_case_reviewer | Complaint Case Reviewer | Review citizen complaints against service standards and recommend remedies. | case_findings
""",
    ),
    Department(
        "hospitality_travel", "Hospitality & Travel",
        "Hotels, restaurants, tourism and travel management operations and guest experience.",
        roles="""
guest_experience_manager | Guest Experience Manager | Map the guest journey and design service standards that make each stay memorable. | service_standards
hotel_revenue_manager | Hotel Revenue Analyst | Analyse occupancy, rates and booking pace and recommend pricing by date and channel. | rate_recommendations
front_desk_procedures_writer | Front Desk Procedures Writer | Write check-in, check-out and guest request procedures with scripts. | front_desk_sop
housekeeping_planner | Housekeeping Planner | Plan room cleaning schedules, staffing and quality checks. | housekeeping_schedule
restaurant_operations_manager | Restaurant Operations Manager | Write opening, closing and service procedures and station checklists. | restaurant_sop
recipe_costing_analyst | Recipe Costing Analyst | Cost recipes from ingredient prices and portions and suggest menu prices. | recipe_costs
food_safety_planner | Food Safety Plan Writer | Write food safety procedures, temperature logs and cleaning schedules. | food_safety_plan
guest_review_analyst | Guest Review Analyst | Analyse online guest reviews by theme and draft management responses. | review_insights
booking_channel_manager | Booking Channel Manager | Compare booking channels on cost and volume and set allocation rules. | channel_strategy
tour_operator_planner | Tour Package Designer | Design tour packages with inclusions, suppliers, pricing and terms. | tour_package
corporate_travel_manager | Corporate Travel Policy Manager | Write travel policies and analyse travel spend for savings. | travel_policy
destination_content_writer | Destination Content Writer | Write destination guides and itineraries for travellers. | destination_guide | rw+web
banquet_event_planner | Banquet Event Planner | Prepare banquet event orders with menus, room setups, timings and staffing. | event_orders
hospitality_staff_trainer | Hospitality Staff Trainer | Write training for service staff: greetings, upselling, complaints and safety. | service_training
loyalty_guest_marketer | Guest Loyalty Marketer | Design guest loyalty offers and personalised pre-arrival messages. | guest_offers
inventory_par_planner | Par Level Planner | Set par levels for food, beverage and supplies from usage data. | par_levels
travel_disruption_coordinator | Travel Disruption Coordinator | Plan responses to cancellations, delays and lost bookings for travellers. | disruption_playbook
spa_wellness_program_designer | Spa and Wellness Program Designer | Design spa and wellness menus, packages and scheduling rules. | wellness_menu
visa_travel_requirements_researcher | Travel Requirements Researcher | Research entry, visa and health requirements for a trip and summarise them. | travel_requirements | rw+web
hospitality_kpi_analyst | Hospitality KPI Analyst | Report occupancy, average rate, revenue per room and guest scores with commentary. | hospitality_kpis
""",
    ),
    Department(
        "manufacturing", "Manufacturing & Engineering",
        "Production engineering, maintenance, quality, safety and continuous improvement.",
        roles="""
manufacturing_engineer | Manufacturing Engineer | Document production processes, cycle times and improvements to throughput and quality. | process_sheet
work_instruction_writer | Work Instruction Writer | Write step-by-step work instructions with safety notes, tools and quality checks. | work_instructions
bill_of_materials_analyst | Bill of Materials Analyst | Check bills of materials for errors, missing parts and cost changes. | bom_review
preventive_maintenance_planner | Preventive Maintenance Planner | Plan maintenance tasks and intervals from equipment data and failure history. | pm_schedule
root_cause_analyst | Root Cause Analyst | Run root cause analysis on defects or downtime using structured methods. | rca_report
fmea_facilitator | FMEA Facilitator | Lead failure mode and effects analysis: failure modes, effects, causes and risk ratings. | fmea
ehs_officer | Health and Safety Officer | Write safety procedures, risk assessments and incident reports for the workplace. | safety_assessment
oee_analyst | OEE Analyst | Calculate overall equipment effectiveness and break down losses by cause. | oee_report
spc_analyst | Statistical Process Control Analyst | Analyse process data with control charts and capability indices. | spc_report
supplier_quality_engineer | Supplier Quality Engineer | Review supplier quality data and write corrective action requests. | supplier_car
engineering_change_coordinator | Engineering Change Coordinator | Manage engineering change requests: impact, approvals and implementation dates. | change_notice
product_compliance_specialist | Product Compliance Specialist | Track product certifications and material declarations required for each market. | compliance_matrix
cost_reduction_engineer | Cost Reduction Engineer | Find design and process changes that cut unit cost without hurting quality. | cost_reduction_ideas
shift_handover_writer | Shift Handover Writer | Turn shift notes into clear handover reports with open issues and actions. | handover_report
kaizen_facilitator | Kaizen Event Facilitator | Plan improvement events: scope, team, data, schedule and follow-up actions. | kaizen_plan
tooling_inventory_manager | Tooling Inventory Manager | Track tools, fixtures and calibration due dates. | tooling_register
technical_datasheet_writer | Technical Datasheet Writer | Write product datasheets and specification sheets from engineering data. | datasheet
packaging_engineer | Packaging Specification Writer | Specify packaging for protection, cost, sustainability and labelling. | packaging_spec
plant_kpi_reporter | Plant KPI Reporter | Report safety, quality, delivery and cost metrics for a plant. | plant_scorecard
industrial_iot_analyst | Machine Data Analyst | Analyse machine sensor and alarm data for patterns that predict failures. | machine_data_report
""",
    ),
    Department(
        "construction_architecture", "Construction & Architecture",
        "Design documentation, project controls, site administration and building compliance.",
        roles="""
architectural_brief_writer | Architectural Brief Writer | Turn client needs into an architectural brief: spaces, sizes, adjacencies and budget. | design_brief
building_code_researcher | Building Code Researcher | Research building code requirements for a project type and list the provisions to check. | code_checklist | rw+web
specification_writer | Construction Specification Writer | Write construction specifications by section, with materials, standards and execution. | specifications
rfi_manager | RFI Manager | Draft requests for information, log responses and track impact on schedule and cost. | rfi_log
submittal_reviewer | Submittal Coordinator | Track submittals against the specification and flag missing or non-compliant items. | submittal_log
change_order_analyst | Change Order Analyst | Review change orders for scope, pricing and schedule impact and recommend a response. | change_order_review
site_diary_writer | Site Report Writer | Turn site notes and photos into daily reports with progress, issues and weather. | site_report
punch_list_coordinator | Punch List Coordinator | Organise snagging items by area and trade and track closure. | punch_list
construction_safety_planner | Site Safety Planner | Write site safety plans, method statements and toolbox talks. | site_safety_plan
bid_package_preparer | Bid Package Preparer | Assemble subcontractor bid packages with scopes, drawings lists and forms. | bid_package
bid_leveler | Bid Leveling Analyst | Compare subcontractor bids line by line and normalise for scope gaps. | bid_leveling
project_controls_analyst | Project Controls Analyst | Track construction cost and schedule against baseline and forecast at completion. | controls_report
closeout_documentation_specialist | Closeout Documentation Specialist | Assemble operation manuals, warranties and as-built records for handover. | closeout_pack
permit_coordinator | Permit Coordinator | List required permits and inspections and track applications and approvals. | permit_tracker
sustainability_certification_advisor | Green Building Advisor | Track credits and evidence for green building certification. | certification_tracker
facility_condition_assessor | Facility Condition Report Writer | Write condition assessment reports with remaining life and capital plans. | condition_report
quantity_surveyor | Quantity Surveyor | Prepare cost plans and interim valuations from measured quantities. | cost_plan
design_review_coordinator | Design Review Coordinator | Collect design review comments from disciplines, resolve conflicts and track responses. | design_review_log
contractor_prequalification_reviewer | Contractor Prequalification Reviewer | Review contractor qualification questionnaires for capacity, safety and finances. | prequalification_review
construction_claims_analyst | Construction Claims Analyst | Analyse delay and disruption events against the contract and records. | claim_analysis
""",
    ),
    Department(
        "media_publishing", "Media & Publishing",
        "Newsrooms, publishing houses, studios and creators: editorial, production, rights and audience.",
        roles="""
managing_editor | Managing Editor | Plan the editorial calendar, assign stories and track deadlines and edits. | editorial_calendar
news_writer | News Writer | Write accurate news stories from source material with attribution. | news_story
copy_desk_editor | Copy Editor | Edit for house style, grammar, headlines and captions. | copyedits
headline_writer | Headline Writer | Write headline and subheading options for clarity and search. | headlines
manuscript_reviewer | Manuscript Reviewer | Assess manuscripts for market fit, structure and editorial needs. | manuscript_report
developmental_editor | Developmental Editor | Give big-picture editorial feedback on structure, argument, pacing and character. | editorial_letter
book_proposal_writer | Book Proposal Writer | Write non-fiction book proposals with overview, market, chapter outline and author platform. | book_proposal
rights_permissions_coordinator | Rights and Permissions Coordinator | Track rights for images, quotes and music, and draft permission requests. | permissions_log
production_editor | Production Editor | Manage manuscripts through typesetting, proofs and printing with a schedule. | production_schedule
audience_growth_analyst | Audience Growth Analyst | Analyse readership and subscriber data and recommend growth tactics. | audience_report
subscription_marketer | Subscription Marketer | Design subscription offers, paywall messaging and retention emails. | subscription_campaign
show_notes_writer | Show Notes Writer | Write episode descriptions, chapter markers and highlight clips lists. | show_notes
screenplay_reader | Script Reader | Write coverage of screenplays with logline, synopsis and assessment. | script_coverage
video_production_planner | Video Production Planner | Plan shoots with call sheets, shot lists, locations and budgets. | call_sheet
content_licensing_analyst | Content Licensing Analyst | Summarise licensing deals, territories, windows and restrictions. | licensing_summary
metadata_specialist | Media Metadata Specialist | Write and check metadata, keywords and descriptions for media catalogues. | metadata_records
corrections_editor | Corrections Editor | Investigate reported errors, verify the facts and draft corrections notes. | corrections
style_guide_keeper | Style Guide Editor | Maintain the house style guide with rulings and examples. | style_guide
newsletter_curator | Newsletter Curator | Curate links and write short summaries for a curated newsletter. | curated_issue | rw+web
creator_brand_deal_manager | Creator Partnerships Manager | Evaluate brand deal offers for creators and draft rate cards and briefs. | rate_card
""",
    ),
]

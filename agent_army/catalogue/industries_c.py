"""Industries: law firm operations, retail, logistics & transport, energy &
utilities, and agriculture & food."""

from ._schema import Department

DEPARTMENTS = [
    Department(
        "law_firm_operations", "Law Firm Operations",
        "Practice support for law firms: intake, docketing, discovery, billing and client service.",
        regulated=True,
        roles="""
client_intake_specialist | Client Intake Specialist | Structure new client enquiries into intake memos with parties, issues and deadlines. | intake_memo
conflict_check_preparer | Conflict Check Preparer | List all parties and related entities in a new matter for the conflict check. | conflict_list
docketing_clerk | Docketing Clerk | Extract deadlines from court orders and rules and build the matter calendar for attorney confirmation. | deadline_calendar
discovery_reviewer | Document Review Assistant | Tag documents for relevance and privilege according to the review protocol, for attorney review. | review_tags
privilege_log_preparer | Privilege Log Preparer | Prepare privilege log entries from tagged documents. | privilege_log
deposition_summarizer | Deposition Summarizer | Summarise deposition transcripts by topic with page and line references. | deposition_summary
legal_brief_cite_checker | Citation Checker | Check that citations in a brief are formatted consistently and match the quoted sources provided. | cite_check_report
legal_billing_reviewer | Legal Billing Reviewer | Review time entries for billing guideline compliance and clear descriptions. | billing_review
engagement_letter_drafter | Engagement Letter Drafter | Draft engagement letters with scope, fees and terms from the matter intake. | engagement_letter
matter_budget_planner | Matter Budget Planner | Estimate matter budgets by phase and track actuals against them. | matter_budget
legal_knowledge_librarian | Legal Knowledge Librarian | Organise precedents, templates and know-how notes so lawyers can find them. | precedent_index
client_update_writer | Client Update Writer | Write client alerts and matter status updates in plain language. | client_update
exhibit_list_builder | Exhibit and Bundle Preparer | Build exhibit lists and court bundles with consistent numbering and indexes. | exhibit_index
legal_project_manager | Legal Project Manager | Plan matters with phases, tasks, staffing and milestones. | matter_plan
court_filing_preparer | Court Filing Checklist Preparer | Prepare filing checklists for format, service and procedural requirements, for attorney confirmation. | filing_checklist
legal_translation_coordinator | Legal Translation Coordinator | Plan translations of legal documents with terminology lists and certification needs. | translation_plan
contract_comparison_specialist | Contract Comparison Specialist | Compare two versions of an agreement and explain every substantive change. | change_summary
law_firm_marketing_writer | Law Firm Marketing Writer | Write practice area pages, attorney bios and award submissions that follow professional rules. | firm_marketing_copy
pro_bono_coordinator | Pro Bono Coordinator | Match pro bono opportunities to lawyers and track hours and outcomes. | pro_bono_tracker
legal_ops_analyst | Legal Operations Analyst | Analyse legal spend, matter cycle times and outside counsel performance. | legal_ops_report
""",
    ),
    Department(
        "retail", "Retail & Stores",
        "Store operations, merchandising, planning, staffing and in-store customer experience.",
        roles="""
store_operations_manager | Store Operations Manager | Write store procedures for opening, closing, cash handling and stock receiving. | store_procedures
visual_merchandiser | Visual Merchandising Planner | Plan window and floor displays with layouts, props and change dates. | display_plan
planogram_designer | Planogram Designer | Lay out shelf placements by sales, margin and adjacency rules. | planogram
assortment_planner | Assortment Planner | Plan product ranges by store cluster from sales data and trends. | assortment_plan
markdown_optimizer | Markdown Planner | Plan clearance markdowns to sell through stock while protecting margin. | markdown_plan
store_staffing_planner | Store Staffing Planner | Build staff rosters from footfall patterns and labour budgets. | staff_roster
retail_sales_analyst | Retail Sales Analyst | Analyse sales by store, category and week and explain the drivers. | sales_analysis
shrink_analyst | Shrink Analyst | Analyse stock loss data by store and category and recommend controls. | shrink_report
loss_prevention_planner | Loss Prevention Planner | Write loss prevention procedures and staff guidance. | lp_procedures
store_audit_designer | Store Audit Designer | Design store visit checklists and score results across stores. | store_audit
retail_customer_service_trainer | Retail Service Trainer | Write customer service training for store staff with scenarios. | store_service_training
clienteling_planner | Clienteling Planner | Plan personal shopping and customer follow-up programs. | clienteling_program
new_store_opening_planner | New Store Opening Planner | Plan store openings with timelines, hiring, fit-out and launch events. | store_opening_plan
retail_buyer | Retail Buyer | Prepare buying plans with quantities, sizes, margins and supplier terms. | buying_plan
open_to_buy_planner | Open-to-Buy Planner | Calculate open-to-buy budgets from sales, stock and purchase plans. | otb_plan
price_label_auditor | Price Accuracy Auditor | Check shelf prices against the system and promotions and list fixes. | price_audit
omnichannel_planner | Omnichannel Planner | Plan click-and-collect, ship-from-store and returns-in-store processes. | omnichannel_plan
retail_promotion_analyst | Retail Promotion Analyst | Measure promotion uplift, cannibalisation and margin impact. | promo_analysis
franchise_operations_writer | Franchise Operations Writer | Write franchise operations manuals and brand standards. | franchise_manual
retail_kpi_reporter | Retail KPI Reporter | Report sales per square foot, conversion, basket size and stock turns. | retail_kpis
""",
    ),
    Department(
        "logistics_transport", "Logistics & Transport",
        "Freight, transport planning, routing, carrier management and delivery operations.",
        roles="""
freight_quote_analyst | Freight Quote Analyst | Compare freight quotes by mode, transit time and total landed cost. | freight_comparison
route_planner | Route Planner | Plan delivery routes and stop sequences from order and location data. | route_plan
carrier_performance_analyst | Carrier Performance Analyst | Score carriers on on-time delivery, damage and cost and plan reviews. | carrier_scorecard
load_planner | Load Planner | Plan truck and container loads for weight, volume and unloading order. | load_plan
dispatch_coordinator | Dispatch Coordinator | Prepare daily dispatch plans and handle exceptions such as breakdowns and delays. | dispatch_plan
freight_audit_specialist | Freight Invoice Auditor | Audit freight invoices against rates and shipments and list overcharges. | freight_audit
shipping_documentation_specialist | Shipping Documents Specialist | Prepare bills of lading, packing lists and commercial invoices from order data. | shipping_documents
last_mile_planner | Last-Mile Delivery Planner | Design last-mile delivery options, time windows and customer notifications. | last_mile_plan
transport_safety_coordinator | Transport Safety Coordinator | Write driver safety procedures and review incident reports. | driver_safety_program
driver_hours_planner | Driver Schedule Planner | Plan driver schedules within working-time rules and rest requirements. | driver_schedule
network_design_analyst | Distribution Network Analyst | Model warehouse locations and flows to balance cost and service. | network_model
cold_chain_planner | Cold Chain Planner | Plan temperature-controlled shipping with monitoring and contingency steps. | cold_chain_plan
freight_claims_handler | Freight Claims Handler | Prepare claims for lost or damaged freight with evidence and values. | freight_claims
shipment_tracking_communicator | Shipment Updates Writer | Write proactive shipment status updates for customers when delays happen. | shipment_updates
logistics_rfp_manager | Logistics Tender Manager | Run carrier and logistics provider tenders: lanes, volumes, scoring and awards. | logistics_tender
yard_management_planner | Yard and Dock Planner | Schedule dock appointments and yard moves to cut waiting time. | dock_schedule
reverse_logistics_planner | Reverse Logistics Planner | Design flows for returns, repairs and recycling. | reverse_flow
transport_emissions_analyst | Transport Emissions Analyst | Estimate transport emissions by lane and mode and find reductions. | transport_emissions
public_transit_planner | Transit Service Planner | Analyse ridership and propose timetable and route adjustments. | transit_plan
logistics_kpi_reporter | Logistics KPI Reporter | Report on-time-in-full, cost per shipment and capacity use with commentary. | logistics_kpis
""",
    ),
    Department(
        "energy_utilities", "Energy & Utilities",
        "Utility operations, customer programs, energy markets, renewables and grid planning support.",
        roles="""
utility_billing_analyst | Utility Billing Analyst | Investigate billing exceptions and high-bill complaints from meter and rate data. | billing_exceptions_report
rate_tariff_explainer | Tariff Explainer | Explain utility rate structures and estimate customer bills under each option. | tariff_comparison
outage_communications_writer | Outage Communications Writer | Write outage notices and restoration updates for customers. | outage_messages
energy_efficiency_program_designer | Efficiency Program Designer | Design customer energy efficiency programs with eligibility, incentives and measurement. | efficiency_program
renewable_project_analyst | Renewable Project Analyst | Model renewable project yields, costs and returns from site data. | project_economics
energy_market_analyst | Energy Market Analyst | Summarise energy price trends and their drivers for procurement decisions. | market_brief | rw+web
energy_procurement_advisor | Energy Procurement Advisor | Compare energy supply contracts and hedging options for a business. | energy_procurement_options
asset_inspection_summarizer | Asset Inspection Summarizer | Summarise inspection findings for poles, lines or pipes into prioritised work. | inspection_priorities
field_work_order_planner | Field Work Planner | Bundle field work orders by location and skill to cut travel time. | work_bundles
grid_interconnection_coordinator | Interconnection Application Coordinator | Prepare interconnection application checklists and track study milestones. | interconnection_tracker
utility_regulatory_writer | Utility Regulatory Filing Writer | Draft sections of rate cases and regulatory filings from supporting data. | filing_draft
meter_data_analyst | Meter Data Analyst | Analyse interval meter data for usage patterns, anomalies and theft indicators. | meter_insights
demand_response_planner | Demand Response Planner | Design demand response events, customer enrolment and settlement rules. | demand_response_program
water_conservation_planner | Water Conservation Planner | Plan water conservation programs and customer messages. | conservation_plan
utility_safety_communicator | Public Safety Communicator | Write safety messages about gas, electricity and digging near utilities. | safety_campaign
ev_charging_planner | EV Charging Planner | Plan electric vehicle charging sites with demand, power and cost estimates. | charging_plan
solar_proposal_writer | Solar Proposal Writer | Write customer solar proposals with system size, savings and payback from site data. | solar_proposal
energy_audit_reporter | Energy Audit Reporter | Turn audit site notes into energy audit reports with measures and savings. | energy_audit
emissions_reporting_analyst | Utility Emissions Reporter | Compile emissions and fuel mix data into required disclosures. | emissions_disclosure
utility_customer_program_analyst | Customer Program Analyst | Evaluate participation and savings of customer programs against targets. | program_evaluation
""",
    ),
    Department(
        "agriculture_food", "Agriculture & Food",
        "Farm business, food production, food safety, traceability and agrifood markets.",
        roles="""
crop_planner | Crop Planner | Plan planting schedules, varieties and inputs from field history and goals. | crop_plan
farm_budget_analyst | Farm Budget Analyst | Build enterprise budgets per crop or herd with yields, prices and costs. | enterprise_budget
livestock_records_manager | Livestock Records Manager | Organise herd records for health, breeding and movements. | herd_records
farm_grant_researcher | Farm Funding Researcher | Find agricultural grants and subsidy schemes that fit the farm and summarise rules. | funding_options | rw+web
food_safety_auditor | Food Safety Auditor | Audit food handling procedures against a hazard analysis plan and list gaps. | food_safety_audit
haccp_plan_writer | HACCP Plan Writer | Write hazard analysis and critical control point plans for a food process. | haccp_plan
traceability_specialist | Traceability Specialist | Design lot tracking from supplier to customer and plan mock recalls. | traceability_plan
recall_coordinator | Recall Coordinator | Write recall procedures with contact lists, notices and reconciliation steps. | recall_plan
food_label_reviewer | Food Label Reviewer | Check food labels for ingredients, allergens and nutrition panel consistency with the recipe. | label_review
nutrition_facts_calculator | Nutrition Analyst | Estimate nutrition information from recipes using stated reference data. | nutrition_panel
commodity_market_analyst | Commodity Market Analyst | Summarise commodity price trends and selling or buying options. | commodity_brief | rw+web
farm_equipment_planner | Farm Machinery Planner | Plan machinery use, maintenance and replacement with cost comparisons. | machinery_plan
irrigation_planner | Irrigation Planner | Plan irrigation schedules from crop needs, soil and weather data. | irrigation_schedule
sustainable_farming_advisor | Sustainable Farming Advisor | Recommend soil health, biodiversity and input-reduction practices with costs. | sustainability_plan
food_product_developer | Food Product Developer | Plan new food product development: concept, recipe trials, costing and shelf-life tests. | product_brief
farm_to_market_planner | Direct Sales Planner | Plan farm shop, market and box-scheme sales with pricing and logistics. | direct_sales_plan
food_supplier_approval_specialist | Supplier Approval Specialist | Assess food suppliers' certificates, audits and specifications. | supplier_approval
agronomy_report_writer | Agronomy Report Writer | Turn field scouting notes into agronomy reports with recommendations. | agronomy_report
cooperative_member_communicator | Cooperative Communications Writer | Write updates, meeting notices and reports for cooperative members. | member_updates
food_waste_analyst | Food Waste Analyst | Measure food waste by stage and recommend reductions. | food_waste_report
""",
    ),
]

"""Industries: healthcare administration, pharma & life sciences, education,
real estate, insurance, and banking & fintech."""

from ._schema import Department

DEPARTMENTS = [
    Department(
        "healthcare_admin", "Healthcare Administration",
        "Non-clinical work in clinics and hospitals: scheduling, revenue cycle, credentialing and patient communication.",
        regulated=True,
        roles="""
patient_scheduling_coordinator | Patient Scheduling Coordinator | Design appointment templates and scheduling rules that reduce wait times and no-shows. | scheduling_rules
prior_authorization_specialist | Prior Authorization Specialist | Assemble prior authorization requests from the documentation provided and track their status. | prior_auth_packet
medical_coding_reviewer | Medical Coding Reviewer | Check coded encounters against the documentation for consistency and flag queries for coders. | coding_review
denial_management_analyst | Denial Management Analyst | Analyse claim denials by reason and payer, and draft appeal letters from the record. | denial_report, appeal_letters
revenue_cycle_analyst | Revenue Cycle Analyst | Track days in receivables, clean claim rate and collections, and find process fixes. | revenue_cycle_report
provider_credentialing_specialist | Credentialing Specialist | Prepare provider credentialing and re-credentialing files and track expiring documents. | credentialing_tracker
patient_intake_designer | Patient Intake Designer | Design intake forms and workflows that collect complete, accurate information once. | intake_forms
patient_communications_writer | Patient Communications Writer | Write appointment reminders, preparation instructions and billing notices in plain language. | patient_messages
clinic_operations_analyst | Clinic Operations Analyst | Analyse patient flow, room utilisation and staffing against demand. | clinic_ops_report
health_records_release_coordinator | Records Release Coordinator | Check records requests for valid authorisation and prepare the release checklist. | release_checklist
care_coordination_planner | Care Coordination Planner | Organise referrals, follow-ups and handoffs between providers into a tracked plan. | care_coordination_plan
telehealth_program_designer | Telehealth Program Designer | Design virtual care workflows: eligibility, scheduling, technology checks and documentation steps. | telehealth_workflow
healthcare_quality_reporter | Healthcare Quality Reporter | Compile quality measure data and prepare submissions and improvement summaries. | quality_measures_report
patient_experience_analyst | Patient Experience Analyst | Analyse patient satisfaction feedback and recommend service improvements. | patient_experience_report
charge_capture_auditor | Charge Capture Auditor | Compare services documented with charges billed and flag missed or duplicate charges. | charge_audit
payer_contract_analyst | Payer Contract Analyst | Summarise payer contract rates and terms and model reimbursement under each. | payer_contract_summary
healthcare_compliance_trainer | Healthcare Compliance Trainer | Write staff training on privacy, documentation and billing compliance. | compliance_training_module
medical_office_manager | Medical Office Manager | Write office procedures for front desk, phones, supplies and opening and closing. | office_procedures
population_health_analyst | Population Health Analyst | Analyse de-identified patient population data for care gaps and outreach priorities. | care_gap_report
healthcare_policy_explainer | Healthcare Policy Explainer | Explain changes in healthcare rules and payment policies and what they mean for operations. | policy_explainer | rw+web
""",
    ),
    Department(
        "pharma_life_sciences", "Pharma & Life Sciences",
        "Regulatory documents, clinical operations, medical writing and quality systems support.",
        regulated=True,
        roles="""
regulatory_affairs_writer | Regulatory Affairs Writer | Draft sections of regulatory submissions from source data, following the required structure. | submission_draft
clinical_protocol_writer | Clinical Protocol Writer | Draft clinical study protocols with objectives, endpoints, eligibility and schedule of assessments. | protocol_draft
informed_consent_writer | Informed Consent Writer | Write participant consent forms in plain language that match the protocol. | consent_form
clinical_trial_coordinator | Clinical Trial Operations Planner | Plan study start-up: site activation steps, documents, timelines and owners. | startup_plan
trial_master_file_auditor | Trial Master File Auditor | Check the trial master file index for missing, outdated or misfiled documents. | tmf_audit
medical_writer | Medical Writer | Write clinical study reports and summaries from tables and listings, without overstating results. | study_report_draft
scientific_literature_monitor | Scientific Literature Monitor | Monitor published literature on a product or topic and summarise new findings. | literature_digest | rw+web
pharmacovigilance_case_processor | Safety Case Processor | Structure adverse event reports into case narratives for safety review. | case_narratives
gxp_document_controller | GxP Document Controller | Manage controlled documents: versions, review cycles, training links and obsolete copies. | document_control_log
deviation_investigator | Deviation Investigator | Document deviations, investigate root cause and propose corrective and preventive actions. | deviation_report
sop_writer_regulated | Regulated SOP Writer | Write standard operating procedures that meet good-practice documentation expectations. | regulated_sop
validation_protocol_writer | Validation Protocol Writer | Write installation, operational and performance qualification protocols for equipment or systems. | validation_protocol
medical_affairs_writer | Medical Affairs Writer | Prepare medical information responses and scientific slide content from approved sources. | medical_info_response
labeling_specialist | Labeling Specialist | Compare product labeling across versions and markets and track required changes. | labeling_comparison
lab_operations_planner | Lab Operations Planner | Plan lab schedules, inventory of reagents and equipment maintenance. | lab_ops_plan
grant_scientific_writer | Scientific Grant Writer | Write research grant proposals with specific aims, significance and approach. | research_grant_proposal
biostatistics_reviewer | Biostatistics Reviewer | Review statistical analysis plans for consistency with the protocol and clear analysis methods. | sap_review
market_access_analyst | Market Access Analyst | Summarise evidence and value arguments for pricing and reimbursement discussions. | value_dossier_outline
clinical_data_reviewer | Clinical Data Reviewer | Review clinical data listings for inconsistencies and raise data queries. | data_queries
quality_auditor_life_sciences | Quality Systems Auditor | Audit quality system processes against procedures and report observations. | quality_audit_report
""",
    ),
    Department(
        "education", "Education",
        "Teaching support, school administration, student services and education programs.",
        roles="""
unit_planner | Unit Planner | Plan multi-week teaching units with goals, sequence, assessments and resources. | unit_plan
rubric_designer | Rubric Designer | Write clear grading rubrics with levels and descriptors aligned to learning goals. | rubric
differentiation_specialist | Differentiation Specialist | Adapt lessons and materials for different reading levels, needs and languages. | differentiated_materials
exam_writer | Exam Writer | Write exams and practice tests that sample the syllabus fairly, with answer keys. | exam
parent_communications_writer | Family Communications Writer | Write newsletters, notices and conference notes for students' families. | family_letters
student_feedback_writer | Student Feedback Writer | Turn rubric scores and notes into specific, encouraging feedback for each student. | student_feedback
school_timetable_planner | Timetable Planner | Build class timetables balancing rooms, teachers and requirements. | timetable
admissions_officer | Admissions Reviewer | Review applications against published criteria consistently and summarise each file. | admissions_summaries
student_success_advisor | Student Success Advisor | Identify students who may need support from attendance and grades, and plan interventions. | support_plan
course_catalog_editor | Course Catalogue Editor | Keep course descriptions, prerequisites and credits accurate and consistent. | course_catalog
accreditation_report_writer | Accreditation Report Writer | Compile evidence and write self-study reports against accreditation standards. | self_study
online_course_builder | Online Course Builder | Structure online courses with modules, readings, activities and discussion prompts. | online_course
tutor_session_planner | Tutoring Session Planner | Plan tutoring sessions around a student's gaps, with practice problems and checks. | tutoring_plan
study_guide_writer | Study Guide Writer | Write study guides and revision notes that summarise key concepts and practice. | study_guide
special_education_plan_assistant | Learning Support Plan Assistant | Draft individual learning support plans from assessments, for the specialist team to finalise. | support_plan_draft
scholarship_coordinator | Scholarship Coordinator | Design scholarship criteria, application forms and scoring, and summarise applicants. | scholarship_program
education_data_analyst | Education Data Analyst | Analyse assessment and attendance data for trends across classes and groups. | education_data_report
academic_integrity_advisor | Academic Integrity Advisor | Write academic integrity guidance and assessment designs that discourage misconduct. | integrity_guidance
classroom_resource_creator | Classroom Resource Creator | Create worksheets, activities and visual aids for a lesson. | classroom_resources
school_policy_writer | School Policy Writer | Draft school policies on attendance, behaviour, technology and safety. | school_policy
""",
    ),
    Department(
        "real_estate", "Real Estate & Property",
        "Property marketing, leasing, property management, transactions and portfolio analysis.",
        roles="""
property_manager | Property Manager | Write property management procedures for rent collection, maintenance requests and inspections. | property_procedures
tenant_communications_writer | Tenant Communications Writer | Write notices to tenants about maintenance, rules, renewals and rent changes. | tenant_notices
leasing_agent | Leasing Assistant | Draft responses to rental enquiries and prepare showing schedules and application checklists. | leasing_responses
rent_roll_analyst | Rent Roll Analyst | Analyse rent rolls for vacancies, expiries, arrears and below-market rents. | rent_roll_analysis
comparable_sales_analyst | Comparables Analyst | Compare a property with recent sales or leases and explain the adjustments. | comps_analysis
real_estate_investment_analyst | Property Investment Analyst | Model property cash flows, cap rates and returns under different scenarios. | property_model
transaction_coordinator | Transaction Coordinator | Track every step of a property transaction from offer to closing, with deadlines and documents. | transaction_timeline
property_inspection_summarizer | Inspection Report Summarizer | Summarise inspection reports into prioritised repair lists with rough cost categories. | repair_list
maintenance_planner | Maintenance Planner | Plan preventive maintenance schedules and budget for building systems. | maintenance_schedule
hoa_communications_writer | Owners' Association Writer | Write owners' association notices, meeting minutes and rule summaries. | association_comms
commercial_lease_analyst | Commercial Lease Analyst | Compare commercial lease proposals on effective rent, incentives and obligations. | lease_comparison
property_marketing_planner | Property Marketing Planner | Plan the marketing of a listing: channels, photos, open houses and timeline. | listing_marketing_plan
tenant_screening_reviewer | Tenant Screening Reviewer | Check rental applications against written, lawful criteria consistently. | screening_summary
portfolio_performance_analyst | Portfolio Performance Analyst | Report occupancy, income, expenses and value trends across a property portfolio. | portfolio_report
space_planner | Space Planner | Plan office or retail layouts for headcount, adjacency and growth. | space_plan
property_tax_reviewer | Property Tax Reviewer | Review property tax assessments for errors and prepare appeal evidence summaries. | assessment_review
building_sustainability_analyst | Building Sustainability Analyst | Analyse building energy and water use and recommend upgrades with payback. | building_upgrade_plan
move_coordinator | Relocation Coordinator | Plan office or home relocations with timelines, vendors and checklists. | move_plan
real_estate_market_researcher | Real Estate Market Researcher | Research local market trends in prices, rents, supply and demand. | market_report | rw+web
landlord_reporting_specialist | Owner Reporting Specialist | Prepare monthly owner statements and commentary for property owners. | owner_statement
""",
    ),
    Department(
        "insurance", "Insurance",
        "Underwriting support, claims, policy administration, agency operations and risk analysis.",
        regulated=True,
        roles="""
policy_summary_writer | Policy Summary Writer | Summarise insurance policies in plain language: what is covered, excluded and required. | policy_summary
quote_comparison_analyst | Quote Comparison Analyst | Compare insurance quotes side by side on coverage, limits, deductibles and price. | quote_comparison
claims_intake_specialist | Claims Intake Specialist | Structure first notice of loss into a complete claim file and list missing items. | claim_intake
claims_letter_writer | Claims Correspondence Writer | Draft acknowledgement, information request and decision letters for claims. | claim_letters
subrogation_analyst | Subrogation Analyst | Identify claims with recovery potential from third parties and summarise the basis. | subrogation_review
loss_run_analyst | Loss Run Analyst | Analyse loss histories for frequency, severity and trends by cause. | loss_analysis
risk_survey_writer | Risk Survey Writer | Turn site survey notes into risk survey reports with recommendations. | risk_survey
renewal_preparer | Renewal Preparer | Prepare renewal submissions with exposure updates, loss history and changes. | renewal_submission
agency_operations_analyst | Agency Operations Analyst | Analyse agency book of business, retention and producer performance. | agency_report
policy_administration_specialist | Policy Administration Specialist | Process endorsements and policy changes accurately and document each one. | endorsement_log
reinsurance_analyst | Reinsurance Analyst | Summarise reinsurance treaty terms and model ceded and retained losses. | treaty_summary
fraud_indicator_reviewer | Claims Fraud Reviewer | Screen claims for fraud indicators and refer suspicious ones with reasons. | fraud_referrals
insurance_product_designer | Insurance Product Designer | Design coverage options, eligibility rules and endorsements for a new product. | product_design
actuarial_data_preparer | Actuarial Data Preparer | Clean and summarise exposure and claims data for actuarial analysis. | actuarial_dataset
certificate_of_insurance_reviewer | Certificate Reviewer | Check certificates of insurance from vendors against contract requirements. | certificate_review
customer_policy_advisor | Policyholder Service Advisor | Answer policyholder questions from policy documents and explain next steps. | policyholder_answers
catastrophe_exposure_analyst | Catastrophe Exposure Analyst | Map insured locations against natural hazard zones and summarise accumulation. | exposure_map
broker_submission_writer | Broker Submission Writer | Write broker submissions that present a risk clearly to underwriters. | broker_submission
insurance_regulatory_filer | Rate and Form Filing Assistant | Prepare filing checklists and explanatory memoranda for rates and forms. | filing_pack
claims_reserve_reviewer | Claims Reserve Reviewer | Review open claim files for reserve adequacy based on the documented facts. | reserve_review
""",
    ),
    Department(
        "banking_fintech", "Banking & Fintech",
        "Lending operations, payments, financial products, customer onboarding and banking risk.",
        regulated=True,
        roles="""
loan_application_reviewer | Loan Application Reviewer | Check loan applications for completeness and summarise them against credit policy. | application_summary
loan_document_checker | Loan Documentation Checker | Check loan documents for missing signatures, inconsistent terms and conditions not yet met. | doc_exceptions
payments_operations_analyst | Payments Operations Analyst | Investigate failed, returned and duplicate payments and document resolutions. | payments_exceptions
chargeback_specialist | Chargeback Specialist | Assemble evidence and responses for card chargebacks by reason code. | chargeback_responses
fintech_product_manager | Fintech Product Manager | Specify financial product features with compliance, risk and customer experience requirements. | fintech_spec
account_opening_designer | Account Opening Designer | Design digital account opening flows that are compliant and low-friction. | onboarding_flow
transaction_monitoring_tuner | Transaction Monitoring Tuner | Review monitoring alert outcomes and propose rule tuning to cut false positives. | rule_tuning_report
sanctions_screening_reviewer | Sanctions Screening Reviewer | Review screening matches, document dispositions and escalate true matches. | screening_dispositions
collections_strategy_designer | Collections Strategy Designer | Design fair, compliant collections contact strategies by risk segment. | collections_strategy
interest_rate_risk_analyst | Interest Rate Risk Analyst | Summarise balance sheet repricing gaps and sensitivity to rate changes. | rate_sensitivity
financial_product_disclosure_writer | Disclosure Writer | Draft clear disclosures and fee schedules for financial products. | disclosures
bank_reconciliation_ops | Settlement Reconciliation Analyst | Reconcile settlement files between processors, banks and the ledger. | settlement_recon
fraud_strategy_analyst | Fraud Strategy Analyst | Analyse fraud losses by type and recommend controls that balance customer friction. | fraud_strategy
credit_policy_writer | Credit Policy Writer | Draft credit policies with criteria, limits, exceptions and approval authorities. | credit_policy
wealth_client_reporter | Client Portfolio Reporter | Prepare client portfolio reports with performance, allocation and commentary. | portfolio_statement
open_banking_integration_planner | Open Banking Integration Planner | Plan account data and payment initiation integrations, including consent flows. | integration_plan
regulatory_reporting_analyst | Regulatory Reporting Analyst | Prepare regulatory report schedules from ledger data and document reconciliations. | regulatory_schedules
complaints_handling_specialist | Financial Complaints Specialist | Investigate customer complaints and draft fair, rule-compliant final responses. | complaint_responses
treasury_operations_planner | Bank Treasury Operations Planner | Plan liquidity monitoring, funding and cash positioning processes. | liquidity_procedures
financial_literacy_writer | Financial Literacy Writer | Write plain-language guides that help customers understand financial products. | customer_guides
""",
    ),
]

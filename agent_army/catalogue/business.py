"""Executive strategy, finance, accounting, legal, and compliance & risk."""

from ._schema import Department

DEPARTMENTS = [
    Department(
        "executive_strategy", "Executive & Strategy",
        "Leadership support, corporate strategy, planning and board-level communication.",
        roles="""
okr_planner | OKR Planner | Turn company or team goals into objectives and measurable key results, check alignment across teams, and flag key results that are activities rather than outcomes. | okrs, alignment_gaps
competitive_intelligence_analyst | Competitive Intelligence Analyst | Profile competitors' products, pricing, positioning and recent moves, and spell out where we win, where we lose and where we are exposed. | competitor_profiles, battle_summary | rw+web
market_sizing_analyst | Market Sizing Analyst | Estimate TAM, SAM and SOM with both top-down and bottom-up methods, showing every assumption and where it came from. | market_model, assumptions | rw+web
business_case_writer | Business Case Writer | Build the business case for an investment: problem, options, costs, benefits, payback period, risks and a recommendation. | business_case
swot_analyst | SWOT Analyst | Produce an evidence-backed SWOT analysis and translate it into concrete strategic options. | swot, strategic_options
scenario_planner | Scenario Planner | Build three or four plausible future scenarios from the key uncertainties, with signposts to watch and no-regret moves. | scenarios, signposts
board_pack_writer | Board Pack Writer | Assemble a board or investor update: highlights, KPIs against plan, risks, asks of the board and a supporting appendix. | board_pack
executive_briefer | Executive Briefer | Condense long documents, threads or reports into a one-page brief with the bottom line first, decisions needed, risks and context. | executive_brief
decision_memo_writer | Decision Memo Writer | Frame a decision as a memo with the question, options considered, criteria, trade-offs and a clear recommendation. | decision_memo
mna_screening_analyst | M&A Screening Analyst | Screen acquisition or partnership targets against strategic-fit criteria and summarise synergies, risks and diligence questions. | target_screen, diligence_questions | rw+web
pricing_strategist | Pricing Strategist | Design pricing and packaging: value metric, tiers, price points, discount policy and expected revenue impact. | pricing_proposal
partnership_strategist | Partnership Strategist | Identify and evaluate partnership opportunities and draft the partner value proposition and deal outline. | partner_map, partner_pitch
offsite_facilitator | Offsite Facilitator | Design a strategy offsite: agenda, pre-reads, exercises, discussion questions and a template for capturing decisions. | offsite_agenda, pre_reads
operating_model_designer | Operating Model Designer | Design or rework an operating model: structure, decision rights, governance forums and the interfaces between teams. | operating_model
transformation_program_lead | Transformation Program Lead | Plan a multi-quarter transformation with workstreams, milestones, dependencies, benefits tracking and change risks. | transformation_roadmap
investor_relations_writer | Investor Relations Writer | Draft shareholder letters, earnings talking points and investor FAQs that are consistent with the reported numbers. | ir_draft, investor_faq
chief_of_staff | Chief of Staff | Run the leadership cadence: prepare meeting agendas, track decisions and action items, and chase owners of overdue commitments. | leadership_agenda, action_tracker
benchmarking_analyst | Benchmarking Analyst | Benchmark our metrics, costs or practices against industry peers and explain the gaps that matter. | benchmark_report | rw+web
horizon_scanner | Horizon Scanner | Scan for emerging trends, regulations and technologies that could affect the business and rate each by timing and impact. | horizon_scan | rw+web
annual_planning_coordinator | Annual Planning Coordinator | Coordinate the annual plan: collect team inputs, reconcile them with targets, and highlight conflicts and unfunded asks. | annual_plan, plan_conflicts
""",
    ),
    Department(
        "finance", "Finance",
        "FP&A, treasury, tax, modelling, valuation and financial decision support.",
        regulated=True,
        roles="""
fpa_analyst | FP&A Analyst | Build budgets and forecasts from historical data and business drivers, and explain variances to plan line by line. | forecast, variance_analysis
cost_center_analyst | Cost Center Analyst | Review departmental spend against budget, find overspends and savings opportunities, and draft notes for budget owners. | spend_review
cash_flow_forecaster | Cash Flow Forecaster | Produce a 13-week cash flow forecast from receivables, payables and payroll timing, and flag liquidity pinch points. | cash_forecast
treasury_analyst | Treasury Analyst | Monitor cash positions, propose investment of surplus cash within policy, and summarise bank and currency exposure. | treasury_report
fx_risk_analyst | FX Risk Analyst | Quantify currency exposure across contracts and balances and set out hedging options with their costs. | fx_exposure
tax_research_analyst | Tax Research Analyst | Research the tax treatment of a transaction or situation, cite the rules found, and list the points to confirm with a licensed advisor. | tax_memo | rw+web
sales_tax_specialist | Sales Tax Specialist | Work out where sales tax or VAT obligations arise from sales data and summarise registration and filing needs. | nexus_summary
transfer_pricing_analyst | Transfer Pricing Analyst | Document intercompany transactions and the pricing method used, and flag arrangements that lack support. | tp_documentation
unit_economics_analyst | Unit Economics Analyst | Calculate CAC, LTV, payback, contribution margin and cohort economics, and explain which levers move them most. | unit_economics
financial_modeler | Financial Modeler | Build three-statement financial models with clear driver tables, scenarios and sanity checks, written as CSV or spreadsheet-ready tables. | financial_model
valuation_analyst | Valuation Analyst | Value a business or project using discounted cash flow and comparables, showing sensitivity to the key assumptions. | valuation
capex_reviewer | Capex Reviewer | Review capital expenditure requests for completeness, ROI logic and strategic fit, and recommend approve, revise or reject. | capex_review
profitability_analyst | Profitability Analyst | Analyse margin by product, customer and channel, and identify unprofitable segments and their root causes. | profitability_report
fundraising_analyst | Fundraising Analyst | Prepare the data room index, financial summaries and investor Q&A for a fundraising round. | data_room_index, investor_qa
grant_finance_specialist | Grant Finance Specialist | Track restricted funds and grant budgets, and prepare financial reports in the format each funder requires. | grant_financial_report
insurance_analyst | Insurance Analyst | Review insurance policies against the company's risks, summarise coverage, exclusions and gaps, and prepare renewal briefs. | coverage_summary
credit_analyst | Credit Analyst | Assess customer or counterparty creditworthiness from financial statements and payment history, and recommend credit limits. | credit_assessment
investment_memo_writer | Investment Memo Writer | Write investment memos covering thesis, market, team, financials, risks and terms. | investment_memo
finance_kpi_designer | Finance KPI Designer | Define the finance KPI set with exact formulas and data sources, and lay out the monthly reporting dashboard. | kpi_definitions, dashboard_spec
finance_policy_writer | Finance Policy Writer | Draft finance policies for expenses, approvals, procurement thresholds and travel that are clear and enforceable. | finance_policy
""",
    ),
    Department(
        "accounting", "Accounting",
        "Bookkeeping, payables, receivables, close, reconciliations, reporting and audit.",
        regulated=True,
        roles="""
accounts_payable_clerk | Accounts Payable Clerk | Three-way match invoices against purchase orders and receipts, flag discrepancies and duplicates, and prepare the payment run. | payment_run, ap_exceptions
accounts_receivable_clerk | Accounts Receivable Clerk | Age receivables, prioritise collections, and draft polite but escalating reminder messages for each customer. | ar_aging, dunning_drafts
bank_reconciler | Bank Reconciliation Specialist | Reconcile bank statements to the ledger, explain every reconciling item and propose correcting entries. | reconciliation
general_ledger_accountant | General Ledger Accountant | Prepare supported journal entries, review the trial balance for anomalies and keep the chart of accounts tidy. | journal_entries, tb_review
month_end_close_coordinator | Month-End Close Coordinator | Run the close checklist, track task owners and deadlines, and report what is blocking the close. | close_checklist, close_status
accruals_accountant | Accruals Accountant | Identify unbilled costs and earned but uninvoiced revenue, and calculate accruals and prepayments with support. | accruals_schedule
revenue_recognition_specialist | Revenue Recognition Specialist | Apply revenue recognition rules to contracts: identify performance obligations, allocate the price and build the schedule. | revrec_schedule
fixed_asset_accountant | Fixed Asset Accountant | Maintain the fixed asset register, compute depreciation, and flag assets to impair or dispose of. | asset_register
payroll_accountant | Payroll Accountant | Reconcile payroll registers to the ledger and benefit providers, and flag anomalies in pay, deductions or headcount. | payroll_reconciliation
expense_auditor | Expense Report Auditor | Audit expense claims against policy, flag out-of-policy, duplicate or suspicious items, and summarise by employee. | expense_audit
intercompany_accountant | Intercompany Accountant | Reconcile intercompany balances, prepare eliminations and chase mismatches between entities. | intercompany_recon
financial_statement_preparer | Financial Statement Preparer | Prepare the income statement, balance sheet and cash flow statement with notes from the trial balance. | financial_statements
audit_readiness_specialist | Audit Readiness Specialist | Prepare for external audit: the request list, supporting schedules, and a memo on areas likely to draw auditor questions. | pbc_list, audit_memo
internal_auditor | Internal Auditor | Test the controls in a process, document exceptions with evidence and recommend remediation with owners. | audit_findings
inventory_accountant | Inventory Accountant | Value inventory, reconcile counts to records, and calculate shrinkage and obsolescence reserves. | inventory_valuation
vendor_master_auditor | Vendor Master Data Auditor | Clean the vendor master file: duplicates, missing tax IDs, stale vendors and bank detail changes that need verification. | vendor_cleanup
billing_specialist | Billing Specialist | Prepare customer invoices from contracts and usage data, checking rates, discounts and tax before issue. | invoices, billing_exceptions
lease_accountant | Lease Accountant | Build lease schedules, right-of-use assets and liabilities, and the journal entries for each lease. | lease_schedules
cost_accountant | Cost Accountant | Calculate product and service costs, allocate overheads using a stated method, and explain cost variances. | cost_report
bookkeeper | Small Business Bookkeeper | Categorise transactions, keep the books current and produce a simple monthly profit and loss summary for the owner. | categorised_ledger, monthly_pnl
""",
    ),
    Department(
        "legal", "Legal",
        "Contracts, corporate, IP, privacy, employment and disputes support.",
        regulated=True,
        roles="""
contract_reviewer | Contract Reviewer | Review contracts clause by clause against our playbook, flag risky or non-standard terms, and propose redlines with fallback positions. | contract_review, redlines
nda_specialist | NDA Specialist | Draft and review mutual or one-way NDAs, flagging scope, term and residuals clauses that deviate from standard. | nda
contract_drafter | Contract Drafter | Draft commercial agreements such as services, licensing and reseller contracts from a term sheet, with clear defined terms. | contract_draft
terms_of_service_writer | Terms of Service Writer | Draft website or product terms of service and acceptable-use policies in plain language. | terms_of_service
privacy_policy_writer | Privacy Policy Writer | Write privacy notices that accurately describe data collected, purposes, sharing, retention and user rights, based on how the product actually works. | privacy_notice
dpa_reviewer | Data Processing Agreement Reviewer | Review data processing agreements for processor obligations, subprocessors, international transfers, breach notice and audit rights. | dpa_review
legal_researcher | Legal Researcher | Research a legal question and summarise the relevant laws, regulations and cases found with citations, noting jurisdictional limits. | research_memo | rw+web
litigation_hold_coordinator | Litigation Hold Coordinator | Draft legal hold notices, identify custodians and data sources, and track acknowledgements. | hold_notice, custodian_list
ip_portfolio_manager | IP Portfolio Manager | Inventory patents, trademarks and copyrights, track renewal deadlines, and flag key assets that are unprotected. | ip_inventory
trademark_screener | Trademark Screener | Run a preliminary screen of a proposed name or mark for conflicts and descriptiveness, and recommend next steps. | trademark_screen | rw+web
open_source_license_reviewer | Open Source License Reviewer | Inventory the open source licences in a codebase and flag obligations or incompatibilities with how we distribute it. | license_report
corporate_secretary | Corporate Secretary | Prepare board resolutions, minutes and written consents, and maintain the corporate records index. | resolutions, minutes
employment_law_advisor | Employment Law Advisor | Review employment documents and HR situations for legal risk and outline compliant options, noting when local counsel is needed. | employment_memo
regulatory_change_tracker | Regulatory Change Tracker | Track new and upcoming regulations relevant to the business and summarise what changes, when, and for whom. | regulatory_digest | rw+web
contract_obligations_manager | Contract Obligations Manager | Extract key dates, renewal terms, obligations and notice periods from contracts into a tracker. | obligations_register
dispute_letter_drafter | Dispute Correspondence Drafter | Draft demand, response and settlement letters that are firm, accurate and preserve our position. | letter_draft
claims_analyst | Claims Analyst | Assess incoming legal claims or complaints for merit and exposure, and recommend a handling strategy. | claims_assessment
legal_intake_triager | Legal Intake Triager | Triage legal requests from the business by type, urgency and risk, and answer or route standard questions. | intake_triage
clause_library_curator | Clause Library Curator | Maintain the approved clause library with preferred, fallback and walk-away positions and usage notes. | clause_library
export_controls_screener | Export Controls Screener | Screen products, customers and destinations for export control and sanctions concerns, and flag cases for specialist review. | screening_report
""",
    ),
    Department(
        "compliance_risk", "Compliance & Risk",
        "Regulatory compliance, privacy programs, certifications, enterprise risk and ESG.",
        regulated=True,
        roles="""
compliance_officer | Compliance Officer | Map the obligations that apply to a business process and check whether current practice meets each one. | obligations_map, gap_report
gdpr_specialist | GDPR Specialist | Assess processing activities for lawful basis, data minimisation, retention and data subject rights, and maintain the record of processing. | ropa, gdpr_gaps
dpia_author | DPIA Author | Write data protection impact assessments: description of processing, necessity, risks to individuals and mitigations. | dpia
soc2_readiness_specialist | SOC 2 Readiness Specialist | Map existing controls to the trust services criteria, identify gaps and plan the evidence to collect. | control_matrix, evidence_plan
iso27001_specialist | ISO 27001 Specialist | Build or review the information security management system: scope, risk assessment, statement of applicability and required policies. | soa, isms_gaps
hipaa_compliance_analyst | HIPAA Compliance Analyst | Check the handling of health information against privacy and security rule safeguards and list required fixes. | hipaa_assessment
pci_compliance_analyst | PCI Compliance Analyst | Determine card-data compliance scope from payment flows, find ways to reduce it, and list requirement gaps. | pci_scope
aml_kyc_analyst | AML and KYC Analyst | Design customer due diligence procedures and review flagged transactions or onboarding files for red flags. | kyc_procedure, case_review
enterprise_risk_manager | Enterprise Risk Manager | Maintain the risk register: identify risks, score likelihood and impact, assign owners and track mitigations. | risk_register
policy_manager | Policy Manager | Draft, review and harmonise internal policies, keep version history, and flag policies overdue for review. | policy_draft, policy_inventory
vendor_risk_assessor | Vendor Risk Assessor | Assess third-party vendors from questionnaires and documents, rate their risk and set the controls they must meet. | vendor_assessment
security_questionnaire_responder | Security Questionnaire Responder | Answer customer security and compliance questionnaires accurately from existing policies and evidence, flagging questions without support. | questionnaire_answers
business_continuity_planner | Business Continuity Planner | Write business continuity and disaster recovery plans with impact analysis, recovery objectives and test scenarios. | bcp
ethics_case_investigator | Ethics Case Investigator | Structure investigations of reported misconduct: allegations, evidence plan, interview questions and findings report. | investigation_plan
accessibility_compliance_auditor | Accessibility Compliance Auditor | Audit documents and digital content against accessibility standards and produce prioritised fixes. | accessibility_audit
esg_reporting_analyst | ESG Reporting Analyst | Collect and structure environmental, social and governance metrics and draft disclosures in a chosen framework. | esg_report
carbon_accountant | Carbon Accountant | Estimate scope 1, 2 and 3 emissions from activity data with stated emission factors, and identify reduction levers. | emissions_inventory
control_tester | Control Tester | Test a sample of control executions against their design, document results and rate control effectiveness. | control_test_results
records_retention_specialist | Records Retention Specialist | Build the records retention schedule and flag data held past its retention period. | retention_schedule
speak_up_program_designer | Speak-Up Program Designer | Design a confidential reporting program: channels, triage, non-retaliation protections and reporting metrics. | speakup_program
""",
    ),
]

"""Marketing, content & creative, sales, and customer success & support."""

from ._schema import Department

DEPARTMENTS = [
    Department(
        "marketing", "Marketing",
        "Strategy, campaigns, SEO, paid media, lifecycle, analytics and product marketing.",
        roles="""
marketing_strategist | Marketing Strategist | Build the marketing plan: segments, positioning, channels, budget split and goals per quarter. | marketing_plan
campaign_strategist | Campaign Strategist | Design an integrated campaign: objective, audience, message, channel mix, timeline and success metrics. | campaign_brief
market_research_analyst | Market Research Analyst | Research a market or audience from available data and sources, and summarise needs, segments and trends. | market_research | rw+web
persona_researcher | Persona Researcher | Build evidence-based buyer personas with goals, pains, triggers and objections. | personas
positioning_strategist | Positioning Strategist | Craft positioning and messaging frameworks: category, differentiators, proof points and value pillars. | messaging_framework
seo_strategist | SEO Strategist | Research keywords and search intent, audit site content structure and produce a prioritised SEO plan. | seo_plan | rw+web
seo_content_optimizer | SEO Content Optimizer | Optimise existing pages for search intent: titles, headings, internal links and content gaps. | seo_recommendations
paid_search_specialist | Paid Search Specialist | Plan paid search campaigns: keyword groups, ad copy variants, bids and negative keywords. | ppc_plan
paid_social_specialist | Paid Social Specialist | Plan paid social campaigns: audiences, creative concepts, budgets and test plans. | paid_social_plan
email_marketer | Email Marketer | Write email campaigns and lifecycle sequences with subject line variants and segmentation logic. | email_sequence
marketing_automation_specialist | Marketing Automation Specialist | Design nurture workflows, lead scoring rules and trigger logic for marketing automation. | automation_spec
growth_experimenter | Growth Experimenter | Generate and prioritise growth experiments with hypotheses, metrics and required sample sizes. | experiment_backlog
marketing_analyst | Marketing Analyst | Analyse channel performance and attribution and recommend budget shifts. | performance_report
event_marketer | Event Marketer | Plan events and webinars: goals, agenda, promotion plan, logistics checklist and follow-up. | event_plan
product_marketing_manager | Product Marketing Manager | Create launch messaging, sales one-pagers and positioning against alternatives for a product. | launch_kit
brand_guardian | Brand Guardian | Review content against brand voice, visual and messaging guidelines, and request specific fixes. | brand_review
influencer_marketer | Influencer Marketer | Identify suitable creator partnerships and write creator briefs and outreach. | influencer_plan
affiliate_program_manager | Affiliate Program Manager | Design affiliate and referral programs: commission structure, terms and partner materials. | affiliate_program
community_manager | Community Manager | Plan community programs and write engagement posts, moderation guidelines and member spotlights. | community_plan
localization_marketer | Localization Marketer | Adapt campaigns for other markets, noting cultural, legal and language considerations. | localized_campaign
ab_test_analyst | A/B Test Analyst | Design A/B tests, check the significance of results, and explain what can and cannot be concluded. | test_readout
conversion_rate_optimizer | Conversion Rate Optimizer | Audit landing pages and funnels for friction and propose testable improvements. | cro_audit
""",
    ),
    Department(
        "content_creative", "Content & Creative",
        "Copy, long-form content, social, video, editing, fact-checking and translation.",
        roles="""
copywriter | Copywriter | Write persuasive copy for ads, landing pages and product pages in the brand voice, with several variants. | copy_variants
blog_writer | Blog Writer | Research and write long-form blog articles with a clear angle, structure and sources. | blog_post | rw+web
whitepaper_writer | Whitepaper Writer | Write authoritative whitepapers and ebooks with data, structure and citations. | whitepaper | rw+web
case_study_writer | Case Study Writer | Turn customer interviews and results into case studies: challenge, solution, measurable outcomes and approved quotes. | case_study
social_media_manager | Social Media Manager | Plan a social content calendar and write platform-specific posts. | content_calendar, posts
video_scriptwriter | Video Scriptwriter | Write scripts for explainer, ad and tutorial videos, with scene directions and timing. | video_script
podcast_producer | Podcast Producer | Plan podcast episodes: guest research, question outlines, show notes and promotion copy. | episode_plan
newsletter_writer | Newsletter Writer | Write engaging newsletters that curate news, insights and calls to action for a defined audience. | newsletter_issue
editor | Editor | Edit drafts for clarity, structure, tone, grammar and factual consistency, explaining the major changes. | edited_draft
proofreader | Proofreader | Catch typos, grammar errors, inconsistent terminology and formatting problems. | proofread_notes
fact_checker | Fact Checker | Verify the factual claims, numbers and quotes in a piece against sources, and flag anything unsupported. | fact_check | rw+web
content_strategist | Content Strategist | Plan the content strategy: pillars, audience journeys, formats, cadence and measurement. | content_strategy
content_repurposer | Content Repurposer | Turn one asset into many: posts, threads, emails, snippets and slide outlines. | repurposed_content
speechwriter | Speechwriter | Write speeches and talking points tailored to the speaker's voice and the audience. | speech
presentation_writer | Presentation Writer | Structure presentations with a storyline, slide-by-slide content and speaker notes. | slide_outline
ux_writer | UX Writer | Write interface microcopy: buttons, errors, empty states and onboarding flows. | microcopy
naming_specialist | Naming Specialist | Generate and evaluate names for products, features or campaigns, with rationale for each. | name_options
creative_director | Creative Director | Develop creative concepts and briefs, and critique creative work against the brief. | creative_concepts
visual_brief_writer | Visual Brief Writer | Write briefs for designers, illustrators or image generation covering composition, style and references. | visual_brief
translator | Translator | Translate content between languages, preserving meaning, tone and terminology, and note ambiguous passages. | translation
content_auditor | Content Auditor | Inventory existing content, score quality and freshness, and recommend keep, update, merge or retire. | content_audit
""",
    ),
    Department(
        "sales", "Sales",
        "Prospecting, qualification, proposals, RFPs, deal desk, forecasting and enablement.",
        roles="""
sales_development_rep | Sales Development Rep | Research target accounts and write personalised prospecting emails and call openers. | prospecting_sequence
account_researcher | Account Researcher | Build account briefs: company overview, priorities, buying committee, triggers and angles for outreach. | account_brief | rw+web
lead_qualifier | Lead Qualifier | Qualify inbound leads against the ideal customer profile and qualification framework, with next-step recommendations. | lead_scores
discovery_call_planner | Discovery Call Planner | Prepare discovery call plans with hypotheses, questions and what must be learned before the next step. | discovery_plan
demo_script_writer | Demo Script Writer | Write tailored demo scripts that map features to the prospect's stated pains. | demo_script
proposal_writer | Proposal Writer | Write sales proposals: understanding of needs, solution, pricing summary, timeline and terms. | proposal
rfp_analyst | RFP Analyst | Break an RFP into requirements, map each to an answer or a gap, and plan the response. | requirements_matrix
rfp_response_writer | RFP Response Writer | Draft RFP and RFI answers from the knowledge base, marking answers that need expert input. | rfp_answers
objection_handling_coach | Objection Handling Coach | Build objection-handling guides with evidence-based responses. | objection_guide
battlecard_writer | Battlecard Writer | Write competitive battlecards: where we win, questions to ask, landmines and proof points. | battlecards
deal_desk_analyst | Deal Desk Analyst | Review non-standard deals for pricing, discount and term risks, and recommend approval conditions. | deal_review
quote_builder | Quote Builder | Build quotes from the price book and configuration rules, and check discounts against policy. | quote
sales_forecaster | Sales Forecaster | Analyse the pipeline by stage, age and rep history to produce a forecast with a risk-adjusted commit. | sales_forecast
pipeline_hygiene_auditor | Pipeline Hygiene Auditor | Find stale, mis-staged or incomplete opportunities in a CRM export and list fixes per owner. | hygiene_report
territory_planner | Territory Planner | Design balanced sales territories and account assignments from account data. | territory_plan
commission_analyst | Commission Analyst | Calculate commissions from the compensation plan and bookings data, and explain each payout. | commission_statements
sales_playbook_writer | Sales Playbook Writer | Document the sales process stage by stage with exit criteria, plays and templates. | sales_playbook
negotiation_strategist | Negotiation Strategist | Prepare negotiation plans: goals, walk-away points, concessions and counter-arguments. | negotiation_plan
win_loss_analyst | Win/Loss Analyst | Analyse won and lost deals for patterns and recommend changes to product, pricing or sales approach. | win_loss_report
channel_partner_manager | Channel Partner Manager | Plan partner enablement, co-selling motions and partner incentive programs. | channel_plan
strategic_account_planner | Strategic Account Planner | Build plans for key accounts: whitespace, stakeholders, risks and growth plays. | account_plan
""",
    ),
    Department(
        "customer_success", "Customer Success & Support",
        "Support, escalations, knowledge base, onboarding, retention and voice of the customer.",
        roles="""
support_agent | Customer Support Agent | Draft accurate, empathetic replies to customer tickets based on the knowledge base and policies. | ticket_replies
ticket_triager | Ticket Triager | Classify support tickets by topic, urgency and sentiment, and route them to the right queue. | triage_results
escalation_manager | Escalation Manager | Handle escalated cases: timeline, root cause, customer communication plan and internal follow-ups. | escalation_plan
knowledge_base_writer | Knowledge Base Writer | Write help centre articles and FAQs from resolved tickets and product documentation. | kb_articles
support_macro_writer | Support Macro Writer | Write reusable response templates for frequent support issues. | macros
customer_success_manager | Customer Success Manager | Build success plans with goals, milestones and adoption metrics for an account. | success_plan
customer_onboarding_specialist | Customer Onboarding Specialist | Design customer onboarding plans and kickoff materials that get customers to first value quickly. | customer_onboarding_plan
churn_risk_analyst | Churn Risk Analyst | Score accounts for churn risk from usage, support and billing signals, and recommend save actions. | churn_risk_report
renewal_manager | Renewal Manager | Prepare renewal briefs: value delivered, risks, expansion options and proposed terms. | renewal_brief
qbr_preparer | QBR Preparer | Prepare quarterly business reviews: outcomes achieved, usage trends, roadmap and asks. | qbr_deck
voice_of_customer_analyst | Voice of Customer Analyst | Synthesise feedback from tickets, surveys and calls into themes with frequency and impact. | voc_report
satisfaction_survey_analyst | NPS and CSAT Analyst | Analyse satisfaction surveys and comments, and identify what drives promoters and detractors. | satisfaction_report
support_quality_reviewer | Support Quality Reviewer | Score support conversations against a quality rubric and give coaching notes. | qa_scores
support_operations_analyst | Support Operations Analyst | Analyse ticket volume and response and resolution times, and forecast staffing needs. | support_ops_report
community_forum_moderator | Community Forum Moderator | Answer community forum questions and flag posts that need product or support attention. | forum_responses
billing_support_specialist | Billing Support Specialist | Resolve billing disputes and refund requests consistently with policy, and draft the customer reply. | billing_resolutions
customer_advocacy_manager | Customer Advocacy Manager | Identify satisfied customers for references, reviews and case studies, and plan the asks. | advocacy_plan
chatbot_flow_designer | Chatbot Flow Designer | Design support chatbot flows, intents and rules for handing off to human agents. | bot_flows
health_score_designer | Customer Health Score Designer | Define a customer health score with weighted signals and validate it against past churn. | health_score_model
customer_change_communicator | Customer Change Communicator | Explain product changes to customers: what changed, who is affected and what they need to do. | customer_notice
""",
    ),
]

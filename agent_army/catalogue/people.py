"""People & HR, talent acquisition, and learning & development."""

from ._schema import Department

DEPARTMENTS = [
    Department(
        "people_hr", "People & HR",
        "HR operations, compensation, performance, employee relations and workforce planning.",
        regulated=True,
        roles="""
hr_generalist | HR Generalist | Answer employee HR questions from the handbook and policies, and route complex cases with a summary. | hr_answers
employee_handbook_writer | Employee Handbook Writer | Write or update the employee handbook so it is consistent, current and readable. | handbook
compensation_analyst | Compensation Analyst | Build salary bands from market and internal data, find pay outliers and model the cost of adjustments. | salary_bands, pay_review
pay_equity_analyst | Pay Equity Analyst | Analyse pay gaps across groups while controlling for role and level, and recommend remediation with its cost. | pay_equity_report
benefits_administrator | Benefits Administrator | Summarise benefit plans for employees, compare plan options and prepare open-enrolment communications. | benefits_guide
performance_review_coach | Performance Review Coach | Help managers write fair, specific, evidence-based performance reviews. | review_drafts
calibration_facilitator | Calibration Facilitator | Prepare calibration sessions with rating distributions, outliers and questions that test consistency. | calibration_pack
employee_relations_advisor | Employee Relations Advisor | Advise on workplace conflicts and performance issues and draft documented, fair improvement plans. | er_case_notes, pip_draft
onboarding_coordinator | Employee Onboarding Coordinator | Build role-specific 90-day onboarding plans with checklists, buddies and milestones. | onboarding_plan
offboarding_coordinator | Offboarding Coordinator | Run exits with a checklist for access removal, equipment return, final pay and knowledge handover, plus exit interview questions. | offboarding_checklist
engagement_survey_analyst | Engagement Survey Analyst | Analyse employee survey results and comments, find the drivers of engagement and suggest focused actions. | survey_insights
org_design_consultant | Org Design Consultant | Model org structures, spans and layers, and propose reorganisations with their trade-offs. | org_options
workforce_planner | Workforce Planner | Forecast headcount needs from the business plan, attrition and productivity, and plan hiring waves. | headcount_plan
hr_policy_writer | HR Policy Writer | Draft HR policies on leave, remote work, conduct and grievances that are clear and compliant. | hr_policy
people_analytics_analyst | People Analytics Analyst | Analyse attrition, tenure, promotion and representation data and explain trends with caveats. | people_dashboard
recognition_program_designer | Recognition Program Designer | Design recognition and rewards programs that reinforce the company values within budget. | recognition_program
inclusion_program_manager | Inclusion Program Manager | Assess inclusion across the employee lifecycle and design programs with measurable goals. | inclusion_plan
wellbeing_program_designer | Wellbeing Program Designer | Design employee wellbeing initiatives and the communications to launch them. | wellbeing_plan
job_architecture_designer | Job Architecture Designer | Define job families, levels and levelling criteria so titles and expectations are consistent. | job_architecture
immigration_coordinator | Immigration Coordinator | Track visa and work permit timelines for employees and prepare document checklists for each case. | visa_tracker
hr_data_steward | HR Data Steward | Audit HR system data for errors and inconsistencies, and define data standards for each field. | hr_data_audit
""",
    ),
    Department(
        "talent_acquisition", "Talent Acquisition",
        "Recruiting from intake and sourcing through interviews, offers and employer brand.",
        roles="""
job_description_writer | Job Description Writer | Write inclusive, accurate job descriptions focused on outcomes, separating must-haves from nice-to-haves. | job_description
sourcing_specialist | Sourcing Specialist | Define the ideal candidate profile and write boolean search strings and target-company lists for sourcing. | sourcing_plan
candidate_outreach_writer | Candidate Outreach Writer | Write personalised outreach and follow-up sequences for passive candidates. | outreach_sequence
resume_screener | Resume Screener | Screen applications consistently against the job's stated requirements, with a short evidence-based rationale per candidate and no use of protected characteristics. | screening_results
interview_kit_designer | Interview Kit Designer | Design structured interview loops: competencies, questions, scoring rubrics and interviewer assignments. | interview_kit
technical_assessment_designer | Technical Assessment Designer | Create job-relevant work-sample assessments with scoring guides and time limits. | assessment, scoring_guide
interview_scheduler | Interview Scheduler | Plan interview schedules across panel availability and time zones, and draft the candidate itinerary. | interview_schedule
debrief_facilitator | Debrief Facilitator | Consolidate interviewer scorecards, highlight disagreements and structure the hiring decision. | debrief_summary
offer_letter_drafter | Offer Letter Drafter | Draft offer letters and offer summaries from approved compensation and start details. | offer_letter
reference_check_specialist | Reference Check Specialist | Prepare role-specific reference questions and summarise reference feedback. | reference_guide
employer_brand_writer | Employer Brand Writer | Write careers page content, employee stories and recruiting posts that are authentic and specific. | careers_content
recruiting_funnel_analyst | Recruiting Funnel Analyst | Analyse funnel conversion, time to hire and source effectiveness, and find bottlenecks. | funnel_report
campus_recruiting_planner | Campus Recruiting Planner | Plan university recruiting: target schools, events, intern programs and timelines. | campus_plan
candidate_experience_designer | Candidate Experience Designer | Map the candidate journey, find friction points and rewrite candidate communications. | candidate_journey
hiring_manager_intake | Hiring Manager Intake Specialist | Run the role intake: clarify the need, success profile, interview plan and compensation range. | intake_brief
talent_pipeline_manager | Talent Pipeline Manager | Organise pipelines of strong past candidates for future roles and plan nurture touchpoints. | pipeline_plan
recruiting_compliance_checker | Recruiting Compliance Checker | Check job ads and hiring steps for discriminatory language and legally risky practices. | compliance_check
contractor_engagement_specialist | Contractor Engagement Specialist | Prepare statements of work and onboarding steps for contractors and freelancers. | contractor_sow
executive_search_researcher | Executive Search Researcher | Map leaders in target organisations for senior searches and summarise their public professional backgrounds. | talent_map | rw+web
internal_mobility_matcher | Internal Mobility Matcher | Match open roles to internal employees' skills and aspirations, and suggest development gaps to close. | mobility_matches
""",
    ),
    Department(
        "learning_development", "Learning & Development",
        "Training design, enablement, leadership development and knowledge checks.",
        light=True,
        roles="""
instructional_designer | Instructional Designer | Design training courses from learning objectives: module outline, activities, assessments and materials. | course_design
training_content_writer | Training Content Writer | Write clear training materials, job aids and step-by-step guides for a target audience. | training_materials
assessment_builder | Assessment Builder | Write quizzes and knowledge checks that test the learning objectives, with answer keys and explanations. | quiz
onboarding_curriculum_designer | Onboarding Curriculum Designer | Build new-hire learning paths by role, sequencing content over the first months. | learning_path
leadership_program_designer | Leadership Program Designer | Design manager and leadership development programs with cohorts, content and practice assignments. | leadership_program
skills_gap_analyst | Skills Gap Analyst | Compare the skills roles require with the team's current skills and prioritise training needs. | skills_gap_report
microlearning_creator | Microlearning Creator | Turn long material into short, focused lessons of a few minutes each. | microlessons
workshop_guide_writer | Workshop Guide Writer | Write facilitator guides with timings, scripts, exercises and debrief questions. | facilitator_guide
elearning_storyboarder | E-learning Storyboarder | Storyboard interactive e-learning modules screen by screen, with narration and interactions. | storyboard
sales_enablement_trainer | Sales Enablement Trainer | Build sales training covering product knowledge, objection-handling drills and certification. | enablement_course
compliance_training_author | Compliance Training Author | Write mandatory compliance training with realistic scenarios and attestations. | compliance_course
coaching_plan_designer | Coaching Plan Designer | Create individual development plans with goals, practice activities and check-in questions. | development_plan
training_effectiveness_analyst | Training Effectiveness Analyst | Evaluate training impact from assessment and performance data and recommend improvements. | effectiveness_report
mentorship_program_designer | Mentorship Program Designer | Design mentorship programs: matching criteria, structure, and guides for mentors and mentees. | mentorship_program
certification_program_designer | Certification Program Designer | Design internal certification paths with requirements, exams and renewal rules. | certification_program
lms_content_administrator | LMS Content Administrator | Organise the learning catalogue, metadata and enrolment rules, and clean up outdated courses. | catalogue_audit
business_writing_coach | Business Writing Coach | Coach employees on clear business writing with before-and-after examples and exercises. | writing_guide
roleplay_simulation_designer | Role-Play Simulation Designer | Write role-play scenarios for practising difficult conversations or customer situations. | simulations
technical_trainer | Technical Trainer | Turn product or engineering documentation into hands-on training labs. | training_labs
learning_newsletter_editor | Learning Newsletter Editor | Curate and write a regular learning newsletter highlighting courses, tips and success stories. | learning_newsletter
""",
    ),
]

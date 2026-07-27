from agents.resume_parser import parse_resume
from tools.matching import score_against_job_description
from schemas.graph_state import RecruitmentState

def parse_resume_node(state: RecruitmentState) -> RecruitmentState:
    profile = parse_resume(state["resume_text"])
    state["candidate_skills"] = profile.skills
    return state

def match_node(state: RecruitmentState) -> RecruitmentState:
    required_skills = ["Python", "Docker", "AWS"]  # simplified for now
    result = score_against_job_description.invoke({
        "candidate_skills": state["candidate_skills"],
        "required_skills": required_skills,
    })
    state["match_result"] = result
    return state

def decision_node(state: RecruitmentState) -> RecruitmentState:
    score = state["match_result"]["match_score_percent"]
    state["decision"] = "shortlist" if score >= 50 else "reject"
    return state

from agents.candidate_lookup import query_candidates
from agents.resume_parser import parse_resume
from tools.matching import score_against_job_description
from schemas.graph_state import RecruitmentState

def parse_resume_node(state: RecruitmentState) -> RecruitmentState:
    profile = parse_resume(state["resume_text"])
    state["candidate_skills"] = profile.skills
    return state

def match_node(state: RecruitmentState) -> RecruitmentState:
    required_skills = ["Python", "Docker", "AWS"]
    result = score_against_job_description.invoke({
        "candidate_skills": state["candidate_skills"],
        "required_skills": required_skills,
    })
    state["match_result"] = result
    return state

def shortlist_node(state: RecruitmentState) -> RecruitmentState:
    state["decision"] = "shortlisted"
    print(f"✅ Candidate shortlisted. Score: {state['match_result']['match_score_percent']}%")
    return state

def reject_node(state: RecruitmentState) -> RecruitmentState:
    state["decision"] = "rejected"
    print(f"❌ Candidate rejected. Score: {state['match_result']['match_score_percent']}%")
    return state

def review_node(state: RecruitmentState) -> RecruitmentState:
    state["decision"] = "needs_human_review"
    print(f"🔍 Sent for manual review. Score: {state['match_result']['match_score_percent']}%")
    return state
async def lookup_similar_candidates_node(state: RecruitmentState) -> RecruitmentState:
    result = await query_candidates("List all candidates in the database")
    state["similar_candidates"] = result
    return state
from langchain_core.tools import tool

@tool
def score_against_job_description(candidate_skills: list[str], required_skills: list[str]) -> dict:
    """Score how well a candidate's skills match a job's required skills.
    Returns a match percentage and the list of missing skills."""
    candidate_set = set(s.lower() for s in candidate_skills)
    required_set = set(s.lower() for s in required_skills)

    matched = candidate_set & required_set
    missing = required_set - candidate_set
    score = round(len(matched) / len(required_set) * 100, 1) if required_set else 0.0

    return {
        "match_score_percent": score,
        "matched_skills": sorted(matched),
        "missing_skills": sorted(missing),
    }
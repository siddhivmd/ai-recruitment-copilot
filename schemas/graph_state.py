from typing import TypedDict, Optional

class RecruitmentState(TypedDict):
    resume_text: str
    job_description: str
    candidate_skills: list[str]
    match_result: Optional[dict]
    decision: Optional[str]
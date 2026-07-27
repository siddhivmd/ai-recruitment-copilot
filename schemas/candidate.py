
from pydantic import BaseModel, Field
from typing import List

class ResumeProfile(BaseModel):
    name: str = Field(description="Candidate's full name")
    email: str = Field(description="Candidate's email address")
    total_experience_years: float = Field(description="Total years of professional experience")
    skills: List[str] = Field(description="List of technical/professional skills")
    education: str = Field(description="Highest education qualification")
    current_role: str = Field(description="Most recent job title")
    summary: str = Field(description="2-3 sentence professional summary")
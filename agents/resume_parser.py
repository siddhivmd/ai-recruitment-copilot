import os
from langchain_groq import ChatGroq
from schemas.candidate import ResumeProfile
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0)
structured_llm = llm.with_structured_output(ResumeProfile)

def parse_resume(resume_text: str) -> ResumeProfile:
    prompt = f"""Extract structured candidate information from this resume.
Be precise — do not invent information not present in the text.

RESUME:
{resume_text}
"""
    return structured_llm.invoke(prompt)
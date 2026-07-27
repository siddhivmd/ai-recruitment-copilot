import os
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from tools.matching import score_against_job_description
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0)
llm_with_tools = llm.bind_tools([score_against_job_description])

def match_candidate(candidate_skills: list[str], job_description: str):
    prompt = f"""A candidate has these skills: {candidate_skills}
Job description: {job_description}

Extract the required skills from the job description, then use the
score_against_job_description tool to evaluate the match. Then give
a one-sentence hiring recommendation."""

    response = llm_with_tools.invoke([HumanMessage(content=prompt)])

    if response.tool_calls:
        for call in response.tool_calls:
            if call["name"] == "score_against_job_description":
                result = score_against_job_description.invoke(call["args"])
                print("Tool result:", result)
                return result
    return response.content
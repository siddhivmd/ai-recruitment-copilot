import asyncio
from graph.workflow import build_graph

app = build_graph()

strong_candidate = """
Jane Doe | jane.doe@email.com
5 years experience as a Backend Engineer at TechCorp.
Skills: Python, Docker, AWS, Kubernetes.
Education: B.Tech Computer Science, IIT Bombay.
"""

async def main():
    result = await app.ainvoke({
        "resume_text": strong_candidate,
        "job_description": "",
        "candidate_skills": [],
        "match_result": None,
        "decision": None,
        "similar_candidates": None,
    })
    print("Final decision:", result["decision"])
    print("Similar candidates from MCP:", result["similar_candidates"])

if __name__ == "__main__":
    asyncio.run(main())
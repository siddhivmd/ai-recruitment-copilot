from graph.workflow import build_graph

app = build_graph()

initial_state = {
    "resume_text": """
    Jane Doe | jane.doe@email.com
    5 years experience as a Backend Engineer at TechCorp.
    Skills: Python, Django, PostgreSQL, AWS.
    Education: B.Tech Computer Science, IIT Bombay.
    """,
    "job_description": "",
    "candidate_skills": [],
    "match_result": None,
    "decision": None,
}

if __name__ == "__main__":
    result = app.invoke(initial_state)
    print(result)
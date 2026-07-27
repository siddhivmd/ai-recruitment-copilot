from graph.workflow import build_graph

app = build_graph()

strong_candidate = """
Jane Doe | jane.doe@email.com
5 years experience as a Backend Engineer at TechCorp.
Skills: Python, Docker, AWS, Kubernetes.
Education: B.Tech Computer Science, IIT Bombay.
"""

weak_candidate = """
Raj Patel | raj.patel@email.com
1 year experience as a junior marketing associate.
Skills: Excel, PowerPoint.
Education: BBA.
"""

if __name__ == "__main__":
    for label, resume in [("STRONG", strong_candidate), ("WEAK", weak_candidate)]:
        print(f"\n--- {label} CANDIDATE ---")
        result = app.invoke({
            "resume_text": resume,
            "job_description": "",
            "candidate_skills": [],
            "match_result": None,
            "decision": None,
        })
        print("Final decision:", result["decision"])
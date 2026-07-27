from langgraph.graph import StateGraph, END
from schemas.graph_state import RecruitmentState
from graph.nodes import (
    parse_resume_node,
    match_node,
    shortlist_node,
    reject_node,
    review_node,
)

def route_decision(state: RecruitmentState) -> str:
    """Decides which node to go to next, based on the match score."""
    score = state["match_result"]["match_score_percent"]
    if score >= 70:
        return "shortlist"
    elif score < 30:
        return "reject"
    else:
        return "review"

def build_graph():
    graph = StateGraph(RecruitmentState)

    graph.add_node("parse_resume", parse_resume_node)
    graph.add_node("match", match_node)
    graph.add_node("shortlist", shortlist_node)
    graph.add_node("reject", reject_node)
    graph.add_node("review", review_node)

    graph.set_entry_point("parse_resume")
    graph.add_edge("parse_resume", "match")

    graph.add_conditional_edges(
        "match",
        route_decision,
        {
            "shortlist": "shortlist",
            "reject": "reject",
            "review": "review",
        },
    )

    graph.add_edge("shortlist", END)
    graph.add_edge("reject", END)
    graph.add_edge("review", END)

    return graph.compile()
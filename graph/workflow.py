from langgraph.graph import StateGraph, END
from schemas.graph_state import RecruitmentState
from graph.nodes import parse_resume_node, match_node, decision_node

def build_graph():
    graph = StateGraph(RecruitmentState)

    graph.add_node("parse_resume", parse_resume_node)
    graph.add_node("match", match_node)
    graph.add_node("decide", decision_node)

    graph.set_entry_point("parse_resume")
    graph.add_edge("parse_resume", "match")
    graph.add_edge("match", "decide")
    graph.add_edge("decide", END)

    return graph.compile()
from langgraph.graph import StateGraph, END
from app.state import ArticleState
from app.nodes.researcher import researcher
from app.nodes.critic import critic
from app.nodes.formatter import formatter

def critic_router(state: ArticleState):
    # Limit to max 3 critic loops
    if state["good_enough"] or state["critic_count"] >= 2:
        return "formatter"
    else:
        return "researcher"

def build_graph():
    graph = StateGraph(ArticleState)
    graph.add_node("researcher", researcher)
    graph.add_node("critic", critic)
    graph.add_node("formatter", formatter)

    graph.set_entry_point("researcher")
    graph.add_edge("researcher", "critic")
    graph.add_conditional_edges(
        "critic",
        critic_router,
        {
            "formatter": "formatter",
            "researcher": "researcher"
        }
    )
    graph.add_edge("formatter", END)
    return graph.compile()
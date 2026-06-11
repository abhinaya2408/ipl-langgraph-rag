from langgraph.graph import (
    StateGraph,
    START,
    END
)

from app.graph.state import IPLState

from app.agents.router_agent import router_agent
from app.agents.retrieval_agent import retrieval_agent
from app.agents.synthesis_agent import synthesis_agent


builder = StateGraph(IPLState)

builder.add_node(
    "router",
    router_agent
)

builder.add_node(
    "retrieval",
    retrieval_agent
)

builder.add_node(
    "synthesis",
    synthesis_agent
)

builder.add_edge(
    START,
    "router"
)

builder.add_edge(
    "router",
    "retrieval"
)

builder.add_edge(
    "retrieval",
    "synthesis"
)

builder.add_edge(
    "synthesis",
    END
)

graph = builder.compile()
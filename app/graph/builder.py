from langgraph.graph import (
    StateGraph,
    START,
    END
)

from app.graph.state import IPLState
from app.graph.routes import route_query

from app.agents.router_agent import router_agent
from app.agents.batting_agent import batting_agent
from app.agents.bowling_agent import bowling_agent
from app.agents.venue_agent import venue_agent
from app.agents.records_agent import records_agent
from app.agents.synthesis_agent import synthesis_agent


builder = StateGraph(IPLState)

# Router Node
builder.add_node(
    "router",
    router_agent
)

# Specialist Agents
builder.add_node(
    "batting_agent",
    batting_agent
)

builder.add_node(
    "bowling_agent",
    bowling_agent
)

builder.add_node(
    "venue_agent",
    venue_agent
)

builder.add_node(
    "records_agent",
    records_agent
)

# Final Answer Node
builder.add_node(
    "synthesis",
    synthesis_agent
)

# Start
builder.add_edge(
    START,
    "router"
)

# Conditional Routing
builder.add_conditional_edges(
    "router",
    route_query,
    {
        "batting": "batting_agent",
        "bowling": "bowling_agent",
        "venue": "venue_agent",
        "records": "records_agent"
    }
)

# Agent -> Synthesis
builder.add_edge(
    "batting_agent",
    "synthesis"
)

builder.add_edge(
    "bowling_agent",
    "synthesis"
)

builder.add_edge(
    "venue_agent",
    "synthesis"
)

builder.add_edge(
    "records_agent",
    "synthesis"
)

# End
builder.add_edge(
    "synthesis",
    END
)

graph = builder.compile()
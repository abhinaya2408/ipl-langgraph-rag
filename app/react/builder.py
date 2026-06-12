from langgraph.graph import (
    StateGraph,
    MessagesState,
    START
)

from langgraph.prebuilt import (
    ToolNode,
    tools_condition
)

from app.react.assistant import assistant
from app.react.tools import TOOLS


# ---------------------------------------
# Build Graph
# ---------------------------------------

builder = StateGraph(MessagesState)

# ---------------------------------------
# Nodes
# ---------------------------------------

builder.add_node(
    "assistant",
    assistant
)

builder.add_node(
    "tools",
    ToolNode(TOOLS)
)

# ---------------------------------------
# Start
# ---------------------------------------

builder.add_edge(
    START,
    "assistant"
)

# ---------------------------------------
# Assistant → Tool OR End
# ---------------------------------------

builder.add_conditional_edges(
    "assistant",
    tools_condition
)

# ---------------------------------------
# Tool → Assistant
# ---------------------------------------

builder.add_edge(
    "tools",
    "assistant"
)

# ---------------------------------------
# Compile Graph
# ---------------------------------------

graph = builder.compile()
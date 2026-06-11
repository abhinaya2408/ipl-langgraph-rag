from typing import TypedDict

from langgraph.graph import (
    StateGraph,
    START,
    END
)


class State(TypedDict):
    message: str


def node1(state):

    print("Node 1 Executed")

    return {
        "message": state["message"] + " -> Node1"
    }


def node2(state):

    print("Node 2 Executed")

    return {
        "message": state["message"] + " -> Node2"
    }


graph_builder = StateGraph(State)

graph_builder.add_node(
    "node1",
    node1
)

graph_builder.add_node(
    "node2",
    node2
)

graph_builder.add_edge(
    START,
    "node1"
)

graph_builder.add_edge(
    "node1",
    "node2"
)

graph_builder.add_edge(
    "node2",
    END
)

graph = graph_builder.compile()

result = graph.invoke(
    {
        "message": "Start"
    }
)

print(result)
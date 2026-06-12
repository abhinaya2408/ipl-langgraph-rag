from langchain_core.messages import HumanMessage

from app.react.graph import react_graph


response = react_graph.invoke(
    {
        "messages": [
            HumanMessage(
                content="Who has scored the most runs and who has taken the most wickets in IPL history?"
            )
        ]
    }
)

print(response)
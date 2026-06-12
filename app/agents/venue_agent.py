from app.tools.venue_tool import (
    search_venue_info
)


def venue_agent(state):

    result = search_venue_info.invoke(
        {
            "query": state["user_query"]
        }
    )

    return {
    "context": result,
    "sources": [result],
    "tool_used": "search_venue_info"
}
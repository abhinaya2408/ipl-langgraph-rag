from app.tools.bowling_tool import (
    search_bowling_stats
)


def bowling_agent(state):

    result = search_bowling_stats.invoke(
        {
            "query": state["user_query"]
        }
    )

    return {
    "context": result,
    "sources": [result],
    "tool_used": "search_bowling_stats"
}
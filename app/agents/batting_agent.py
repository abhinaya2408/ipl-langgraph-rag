from app.tools.batting_tool import (
    search_batting_stats
)


def batting_agent(state):

    result = search_batting_stats.invoke(
        {
            "query": state["user_query"]
        }
    )

    return {
    "context": result,
    "sources": [result],
    "tool_used": "search_batting_stats"
}
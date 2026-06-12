from app.tools.records_tool import (
    search_records
)


def records_agent(state):

    result = search_records.invoke(
        {
            "query": state["user_query"]
        }
    )

    return {
    "context": result,
    "sources": [result],
    "tool_used": "search_records"
    }
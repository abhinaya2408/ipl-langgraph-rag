from typing import TypedDict

class IPLState(TypedDict, total=False):

    user_query: str

    query_type: str

    context: str

    final_answer: str

    tool_used: str
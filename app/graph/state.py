from typing import TypedDict, List

class IPLState(TypedDict):

    user_query: str

    query_type: str

    context: str

    sources: List[str]

    final_answer: str
from langchain.tools import tool

from app.retrieval.specialized_retrievers import (
    get_bowling_retriever
)

retriever = get_bowling_retriever()


@tool
def search_bowling_stats(query: str) -> str:
    """
    Search bowling statistics from the IPL dataset.
    """

    docs = retriever.invoke(query)

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    return f"""
You are given IPL bowling statistics.

Use ONLY the information below.

{context}
"""
from langchain.tools import tool

from app.retrieval.specialized_retrievers import (
    get_bowling_retriever
)


@tool
def search_bowling_stats(query: str):

    """
    Search bowling statistics.
    """

    retriever = get_bowling_retriever()

    docs = retriever.invoke(query)

    return "\n\n".join(
        doc.page_content
        for doc in docs
    )
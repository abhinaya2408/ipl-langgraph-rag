from langchain.tools import tool

from app.retrieval.specialized_retrievers import (
    get_batting_retriever
)

retriever = get_batting_retriever()


@tool
def search_batting_stats(query: str) -> str:
    """
    Search batting statistics from the IPL dataset.
    """

    docs = retriever.invoke(query)

    docs = docs[:2]

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    return context
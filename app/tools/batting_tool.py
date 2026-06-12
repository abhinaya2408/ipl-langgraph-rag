from langchain.tools import tool

from app.retrieval.specialized_retrievers import (
    get_batting_retriever
)


@tool
def search_batting_stats(query: str):

    """
    Search batting statistics.
    """

    retriever = get_batting_retriever()

    docs = retriever.invoke(query)

    return "\n\n".join(
        doc.page_content
        for doc in docs
    )
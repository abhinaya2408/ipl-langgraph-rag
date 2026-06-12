from langchain.tools import tool

from app.retrieval.specialized_retrievers import (
    get_venue_retriever
)

retriever = get_venue_retriever()


@tool
def search_venue_info(query: str) -> str:
    """
    Search venue and pitch information from the IPL dataset.
    """

    docs = retriever.invoke(query)

    docs = docs[:2]

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    return context
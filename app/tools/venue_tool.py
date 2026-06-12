from langchain.tools import tool

from app.retrieval.specialized_retrievers import (
    get_venue_retriever
)


@tool
def search_venue_info(query: str):

    """
    Search venue information.
    """

    retriever = get_venue_retriever()

    docs = retriever.invoke(query)

    return "\n\n".join(
        doc.page_content
        for doc in docs
    )
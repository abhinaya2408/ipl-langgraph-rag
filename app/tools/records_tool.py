from langchain.tools import tool

from app.retrieval.specialized_retrievers import (
    get_records_retriever
)


@tool
def search_records(query: str):

    """
    Search IPL records.
    """

    retriever = get_records_retriever()

    docs = retriever.invoke(query)

    return "\n\n".join(
        doc.page_content
        for doc in docs
    )
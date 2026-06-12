from langchain.tools import tool

from app.retrieval.specialized_retrievers import (
    get_records_retriever
)

retriever = get_records_retriever()


@tool
def search_records(query: str) -> str:
    """
    Search IPL records and milestones from the dataset.
    """

    docs = retriever.invoke(query)

    docs = docs[:2]

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    return context
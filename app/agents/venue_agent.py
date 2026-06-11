from app.retrieval.specialized_retrievers import (
    get_venue_retriever
)

retriever = get_venue_retriever()

def venue_agent(state):

    print("Venue Agent Executed")

    docs = retriever.invoke(
        state["user_query"]
    )

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    return {
        "context": context,
        "sources": [
            doc.page_content[:500]
            for doc in docs
        ]
    }
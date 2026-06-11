from app.retrieval.specialized_retrievers import (
    get_bowling_retriever
)

retriever = get_bowling_retriever()

def bowling_agent(state):

    print("Bowling Agent Executed")

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
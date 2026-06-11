from app.retrieval.specialized_retrievers import (
    get_batting_retriever
)

retriever = get_batting_retriever()

def batting_agent(state):

    print("Batting Agent Executed")

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
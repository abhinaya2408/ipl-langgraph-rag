from app.retrieval.retriever import get_retriever

retriever = get_retriever()


def records_agent(state):

    print("Records Agent Executed")

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
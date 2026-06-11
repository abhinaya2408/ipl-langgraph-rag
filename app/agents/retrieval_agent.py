from app.retrieval.retriever import get_retriever


retriever = get_retriever()


def retrieval_agent(state):

    query = state["user_query"]

    docs = retriever.invoke(query)

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    return {
        "context": context
    }
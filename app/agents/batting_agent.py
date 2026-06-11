from app.retrieval.retriever import get_retriever

retriever = get_retriever()


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
        "context": context
    }
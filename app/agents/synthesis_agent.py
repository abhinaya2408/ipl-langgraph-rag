from app.llms.llm_factory import get_llm

llm = get_llm()


def synthesis_agent(state):

    query = state["user_query"]

    context = state["context"]

    prompt = f"""
You are an IPL assistant.

Answer ONLY using the given context.

If the answer is not present in the context,
say:

"I couldn't find this information in the dataset."

Context:
{context}

Question:
{query}
"""

    response = llm.invoke(prompt)

    return {
    "final_answer": response.content,
    "context": context,
    "tool_used": state.get("tool_used"),
    "sources": state.get(
        "sources",
        [context]
    ),
    "query_type": state.get("query_type")
}
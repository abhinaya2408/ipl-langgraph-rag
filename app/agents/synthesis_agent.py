from app.llms.llm_factory import get_llm

llm = get_llm()


def synthesis_agent(state):

    query = state["user_query"]

    context = state["context"]

    prompt = f"""
You are an IPL assistant.

Answer only from the given context.

Context:
{context}

Question:
{query}
"""

    response = llm.invoke(prompt)

    return {
        "final_answer": response.content
    }
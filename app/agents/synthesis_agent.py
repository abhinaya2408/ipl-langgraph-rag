from app.llms.llm_factory import get_llm

llm = get_llm()


def synthesis_agent(state):

    query = state["user_query"]

    context = state["context"]

    prompt = f"""
You are an IPL Intelligence Assistant.

You MUST answer ONLY using the information provided in the context.

Rules:
1. Never use outside knowledge.
2. Never guess.
3. If multiple players are present, carefully identify the one matching the question.
4. For record-based questions (highest, most, best, top), always choose the highest value from the context.
5. If the answer is not present in the context, reply exactly:
"I couldn't find this information in the dataset."

Context:
{context}

Question:
{query}

Answer:
"""

    response = llm.invoke(prompt)

    return {
        "final_answer": response.content,
        "context": context,
        "query_type": state.get("query_type"),
        "tool_used": state.get("tool_used"),
        "sources": state.get("sources", [context])
    }
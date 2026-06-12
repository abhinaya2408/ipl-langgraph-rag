from app.llms.llm_factory import get_llm

from app.tools.tools import TOOLS

llm = get_llm().bind_tools(TOOLS)


def react_agent(state):

    query = state["user_query"]

    response = llm.invoke(query)

    # -----------------------------
    # No Tool Required
    # -----------------------------

    if not response.tool_calls:

        return {
            "final_answer": response.content,
            "tool_used": None,
            "context": "",
            "sources": []
        }

    # -----------------------------
    # Tool Selected
    # -----------------------------

    tool_call = response.tool_calls[0]

    tool_name = tool_call["name"]

    tool_args = tool_call["args"]

    tool_result = ""

    for tool in TOOLS:

        if tool.name == tool_name:

            tool_result = tool.invoke(tool_args)

            break

    # -----------------------------
    # Final Prompt
    # -----------------------------

    final_prompt = f"""
You are an IPL Intelligence Assistant.

Answer ONLY using the retrieved context.

Rules:
1. Never use outside knowledge.
2. Never guess.
3. Use only the context.
4. If the answer is not present, reply:
"I couldn't find this information in the dataset."

Context:
{tool_result}

Question:
{query}

Answer:
"""

    final_response = get_llm().invoke(
        final_prompt
    )

    return {
        "final_answer": final_response.content,
        "tool_used": tool_name,
        "context": tool_result,
        "sources": [tool_result]
    }
from langchain_core.messages import SystemMessage

from app.llms.llm_factory import get_llm
from app.react.tools import TOOLS
from app.react.prompts import SYSTEM_PROMPT

llm = get_llm()

llm_with_tools = llm.bind_tools(TOOLS)


def assistant(state):

    messages = state["messages"]

    response = llm_with_tools.invoke(

        [SystemMessage(content=SYSTEM_PROMPT)]

        + messages

    )

    return {

        "messages": [response]

    }
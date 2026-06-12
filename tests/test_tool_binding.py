from app.llms.llm_factory import get_llm

from app.tools.tools import TOOLS

llm = get_llm()

llm_with_tools = llm.bind_tools(
    TOOLS
)

response = llm_with_tools.invoke(
    "Who has taken the most wickets in IPL history?"
)

print(response)
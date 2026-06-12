from app.agents.react_agent import react_agent

result = react_agent(
    {
        "user_query":
        "Who has taken the most wickets?"
    }
)

print(result)
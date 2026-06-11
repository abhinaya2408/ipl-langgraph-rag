def router_agent(state):

    query = state["user_query"].lower()

    if any(word in query for word in ["run", "batting", "century"]):

        query_type = "batting"

    elif any(word in query for word in ["wicket", "bowling"]):

        query_type = "bowling"

    elif any(word in query for word in ["pitch", "venue"]):

        query_type = "venue"

    else:

        query_type = "general"

    print(f"Router → {query_type}")

    return {
        "query_type": query_type
    }
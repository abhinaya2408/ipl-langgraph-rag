def router_agent(state):

    query = state["user_query"].lower()

    if any(
        word in query
        for word in [
            "run",
            "runs",
            "century",
            "batting"
        ]
    ):
        query_type = "batting"

    elif any(
        word in query
        for word in [
            "wicket",
            "wickets",
            "bowling"
        ]
    ):
        query_type = "bowling"

    elif any(
        word in query
        for word in [
            "pitch",
            "venue"
        ]
    ):
        query_type = "venue"

    else:
        query_type = "records"

    print(f"Router -> {query_type}")

    return {
        "query_type": query_type
    }
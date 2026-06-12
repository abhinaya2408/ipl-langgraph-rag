def router_agent(state):

    query = state["user_query"].lower()

    # -----------------------------
    # Records Queries
    # -----------------------------
    if any(
        word in query
        for word in [
            "highest",
            "most",
            "record",
            "records",
            "title",
            "titles",
            "history",
            "highest score",
            "highest team",
            "highest individual",
            "most runs",
            "most wickets",
            "most centuries",
            "most matches",
            "partnership"
        ]
    ):

        query_type = "records"

    # -----------------------------
    # Venue Queries
    # -----------------------------
    elif any(
        word in query
        for word in [
            "pitch",
            "stadium",
            "venue",
            "ground",
            "hyderabad",
            "chennai",
            "wankhede",
            "eden",
            "chinnaswamy"
        ]
    ):

        query_type = "venue"

    # -----------------------------
    # Bowling Queries
    # -----------------------------
    elif any(
        word in query
        for word in [
            "wicket",
            "bowling",
            "economy",
            "bowler",
            "average",
            "spell"
        ]
    ):

        query_type = "bowling"

    # -----------------------------
    # Batting Queries
    # -----------------------------
    elif any(
        word in query
        for word in [
            "virat",
            "rohit",
            "warner",
            "rahul",
            "runs",
            "batting",
            "strike rate",
            "average",
            "fifties",
            "centuries"
        ]
    ):

        query_type = "batting"

    else:

        query_type = "records"

    print(f"Router -> {query_type}")

    return {
        "query_type": query_type
    }
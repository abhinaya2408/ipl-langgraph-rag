from app.graph.builder import graph

queries = [
    "Virat Kohli runs",
    "Who has most wickets?",
    "Tell me about Hyderabad pitch"
]

for query in queries:

    print("\n" + "=" * 50)
    print("Query:", query)

    result = graph.invoke(
        {
            "user_query": query
        }
    )

    print("\nAnswer:")
    print(result["final_answer"])
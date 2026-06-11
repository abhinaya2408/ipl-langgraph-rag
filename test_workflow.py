from app.graph.builder import graph

result = graph.invoke(
    {
        "user_query": "How many runs has Virat Kohli scored?"
    }
)

print("\nAnswer:\n")

print(
    result["final_answer"]
)
from app.graph.builder import graph


def main():

    print("=" * 50)
    print("IPL Intelligence Assistant")
    print("Type 'exit' to quit")
    print("=" * 50)

    while True:

        query = input("\nAsk Question: ")

        if query.lower() == "exit":
            break

        result = graph.invoke(
            {
                "user_query": query
            }
        )

        print("\nAnswer:\n")

        print(
            result["final_answer"]
        )


if __name__ == "__main__":
    main()
from app.retrieval.retriever import get_retriever

retriever = get_retriever()

docs = retriever.invoke(
    "Virat Kohli runs"
)

print("\nRetrieved Documents:\n")

for i, doc in enumerate(docs, start=1):

    print(f"\nDocument {i}")
    print("-" * 50)

    print(doc.page_content)
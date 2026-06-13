from app.retrieval.specialized_retrievers import get_batting_retriever

retriever = get_batting_retriever()

docs = retriever.invoke("Virat Kohli strike rate")

print("=" * 50)

for i, doc in enumerate(docs, 1):
    print(f"\nDocument {i}")
    print(doc.metadata)
    print(doc.page_content)
    print("=" * 50)
from app.retrieval.specialized_retrievers import (
    get_records_retriever
)

retriever = get_records_retriever()

docs = retriever.invoke(
    "highest individual score"
)

for i, doc in enumerate(docs, start=1):

    print(f"\nDocument {i}")
    print("-" * 50)

    print(doc.page_content[:500])
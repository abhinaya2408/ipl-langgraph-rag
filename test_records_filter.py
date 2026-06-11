# test_find_records.py

from app.ingestion.pdf_loader import load_pdf
from app.retrieval.chunking import create_chunks

docs = load_pdf(
    "data/IPL_LangGraph_RAG_Dataset.pdf"
)

chunks = create_chunks(docs)

for i, chunk in enumerate(chunks):

    text = chunk.page_content.lower()

    if "highest individual score" in text:

        print("\nFOUND")
        print("=" * 50)

        print("Chunk:", i)

        print(chunk.metadata)

        print(chunk.page_content[:1000])
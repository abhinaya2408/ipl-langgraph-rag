from app.ingestion.pdf_loader import load_pdf
from app.retrieval.chunking import create_chunks

docs = load_pdf(
    "data/IPL_LangGraph_RAG_Dataset.pdf"
)

chunks = create_chunks(docs)

print("Total Chunks:", len(chunks))

print("\nFirst Chunk:\n")
print(chunks[0].page_content[:1000])
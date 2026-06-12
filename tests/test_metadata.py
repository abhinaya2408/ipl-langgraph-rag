from app.ingestion.pdf_loader import load_pdf
from app.retrieval.chunking import create_chunks

docs = load_pdf(
    "data/IPL_LangGraph_RAG_Dataset.pdf"
)

chunks = create_chunks(docs)

for i in range(10):

    print(f"\nChunk {i+1}")
    print(chunks[i].metadata)
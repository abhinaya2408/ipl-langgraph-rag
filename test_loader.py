from app.ingestion.pdf_loader import load_pdf

docs = load_pdf(
    "data/IPL_LangGraph_RAG_Dataset.pdf"
)

print(f"Pages: {len(docs)}")

print("\nFirst Page:\n")

print(docs[0].page_content[:1000])
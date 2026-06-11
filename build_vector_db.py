from app.ingestion.pdf_loader import load_pdf
from app.retrieval.chunking import create_chunks
from app.retrieval.vectorstore import (
    create_vectorstore
)


def main():

    docs = load_pdf(
        "data/IPL_LangGraph_RAG_Dataset.pdf"
    )

    chunks = create_chunks(docs)

    create_vectorstore(chunks)

    print("Vector Database Created Successfully")


if __name__ == "__main__":
    main()
from langchain_chroma import Chroma

from app.retrieval.embeddings import (
    get_embeddings
)


def create_vectorstore(chunks):

    embeddings = get_embeddings()

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="vector_db"
    )

    return vectorstore
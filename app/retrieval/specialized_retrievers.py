from langchain_chroma import Chroma

from app.retrieval.embeddings import (
    get_embeddings
)


def get_batting_retriever():

    vectorstore = Chroma(
        persist_directory="vector_db",
        embedding_function=get_embeddings()
    )

    return vectorstore.as_retriever(
        search_kwargs={
            "k": 3,
            "filter": {
                "category": "batting"
            }
        }
    )


def get_bowling_retriever():

    vectorstore = Chroma(
        persist_directory="vector_db",
        embedding_function=get_embeddings()
    )

    return vectorstore.as_retriever(
        search_kwargs={
            "k": 3,
            "filter": {
                "category": "bowling"
            }
        }
    )


def get_venue_retriever():

    vectorstore = Chroma(
        persist_directory="vector_db",
        embedding_function=get_embeddings()
    )

    return vectorstore.as_retriever(
        search_kwargs={
            "k": 3,
            "filter": {
                "category": "venue"
            }
        }
    )


def get_records_retriever():

    vectorstore = Chroma(
        persist_directory="vector_db",
        embedding_function=get_embeddings()
    )

    return vectorstore.as_retriever(
        search_kwargs={
            "k": 3,
            "filter": {
                "category": "records"
            }
        }
    )
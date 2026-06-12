from app.retrieval.embeddings import get_embeddings

embeddings = get_embeddings()

vector = embeddings.embed_query(
    "Virat Kohli"
)

print("Embedding Dimension:", len(vector))

print("\nFirst 5 Values:")

print(vector[:5])
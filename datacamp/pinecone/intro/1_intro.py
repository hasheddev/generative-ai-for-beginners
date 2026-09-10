from pinecone import ServerlessSpec, Pinecone
import os
from dotenv import load_dotenv

load_dotenv()

pc = Pinecone(
    api_key=os.getenv("PINECONE_API_KEY"),
    
    )

pc.create_index(
    name="my-first-index",
    dimension=1536,  # Match your embedding model dimension (e.g., OpenAI text-embedding-ada-002 / 3-small)
    metric="cosine",  # Options: "cosine", "euclidean", or "dotproduct"
    spec=ServerlessSpec(
        cloud="aws",
        region="us-east-1",
    ),
)

index = pc.Index("my-first-index")

# Print the index statistics
print(index.describe_index_stats())

pc.delete_index('my-first-index')

# List your indexes
print(pc.list_indexes())

vectors = [
    {
        "id": "0",
        "values": [0.025525547564029694, 0.0188823901116848]
        "metadata": {"genre": "action", "year": 2024}
    }
]

pc.create_index(
    name="datacamp-index", 
    dimension=1536, 
    spec=ServerlessSpec(
        cloud='aws', 
        region='us-east-1'
    )
)

# Check that each vector has a dimensionality of 1536
vector_dims = [len(vector['values']) == 1536 for vector in vectors]
print(all(vector_dims))

index = pc.Index("datacamp-index")

# Ingest the vectors and metadata
index.upsert(
    vectors=vectors
)

# Print the index statistics
print(index.describe_index_stats())
from utils import get_datacamp_index

index = get_datacamp_index()

vector=[]

# Update the values of vector ID 7
index.update(
    id="7",
    values=vector
)

# Fetch vector ID 7
fetched_vector = index.fetch(ids=["7"])
print(fetched_vector)

index.update(
    id="7",
    set_metadata={"genre": "thriller", "year": 2024}
)

# Delete vectors
index.delete(ids=["3", "4"])

# Retrieve metrics of the connected Pinecone index
print(index.describe_index_stats())
from utils import chunks, get_datacamp_index, pc

index = get_datacamp_index(multi_thread=True)

vectors = []
# Upsert vectors in batches of 100
for chunk in chunks(vectors):
    index.upsert(vectors=chunk)

# Retrieve statistics of the connected Pinecone index
print(index.describe_index_stats())

with pc.Index('datacamp-index', pool_threads=20) as index:
    async_results = [index.upsert(vectors=chunk, async_req=True) for chunk in chunks(vectors, batch_size=200)]
    [async_result.get() for async_result in async_results]

# Retrieve statistics of the connected Pinecone index
print(index.describe_index_stats())
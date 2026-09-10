from utils import get_datacamp_index

index = get_datacamp_index()

ids = ['2', '5', '8']

fetched_vectors = index.fetch(ids=ids)
print(fetched_vectors)

# Extract the metadata from each result in fetched_vectors
metadatas = [fetched_vectors['vectors'][id]['metadata'] for id in ids]
print(metadatas)

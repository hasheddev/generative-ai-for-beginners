from utils import get_datacamp_index

vector_set1= []

vector_set2 =[]

index = get_datacamp_index()

index.upsert(
  vectors=vector_set1,
  namespace='namespace1'
)

# Upsert vector_set2 to namespace2
index.upsert(
  vectors=vector_set2,
  namespace='namespace2'
)

# Print the index statistics
print(index.describe_index_stats())

vector = []

query_result = index.query(
    vector=vector,
    namespace='namespace1',
    top_k=3
)
print(query_result)
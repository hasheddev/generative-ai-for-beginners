from utils import get_datacamp_index

index = get_datacamp_index()

vector= []

query_result = index.query(
    vector=vector,
    include_metadata=True,
    top_k=1,
    filter={
        "year": {"$eq": 2024}
    }
)

query_result = index.query(
    vector=vector,
    include_metadata=True,
    top_k=1,
    filter={ "$and": [
            {"year": {"$lt": 2018}},
            {"genre": "thriller"}
        ]
    }
)
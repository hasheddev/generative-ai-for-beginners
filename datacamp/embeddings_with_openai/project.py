import numpy as np
import pandas as pd
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import chromadb

reviews = pd.read_csv("womens_clothing_e-commerce_reviews.csv")

client = chromadb.PersistentClient(path='./db')
collection = client.get_or_create_collection(name="clothing_reviews")

ids = []
texts = []
metadatas = []

for i, row in reviews.iterrows():
    review_text = row['Review Text']
    if pd.isna(review_text) or not str(review_text).strip():
        continue
    
    ids.append(str(i))
    metadatas.append({
        'customer_age': int(row['Age']) if pd.notna(row['Age']) else 0,
        'customer_rating': int(row['Rating']) if pd.notna(row['Rating']) else 0,
        'clothing_id': int(row['Clothing ID']) if pd.notna(row['Clothing ID']) else 0
    })
    texts.append(str(review_text))

collection.upsert(ids=ids, metadatas=metadatas, documents=texts)

results = collection.get(include=["embeddings"])
embeddings = results['embeddings']

tsne = TSNE(n_components=2, perplexity=15, random_state=42)
embeddings_2d = tsne.fit_transform(np.array(embeddings))

plt.scatter(embeddings_2d[:, 0], embeddings_2d[:, 1], alpha=0.5)
plt.title("t-SNE Review Embeddings")
plt.show()

# 5. Feedback Categorization
topics = ["quality", "fit", "style", "comfort"]
category_results = {}
N_RESULTS = 10

for topic in topics:
    query_response = collection.query(
        query_texts=[f"This review is about product {topic}."],
        n_results=N_RESULTS,
        include=["documents", "metadatas", "distances"]
    )
    
    matching_docs = query_response["documents"][0]
    matching_metas = query_response["metadatas"][0]
    distances = query_response["distances"][0]
    
    category_results[topic] = pd.DataFrame({
        "topic": topic,
        "review_text": matching_docs,
        "clothing_id": [m["clothing_id"] for m in matching_metas],
        "rating": [m["customer_rating"] for m in matching_metas],
        "distance": distances
    })

categorized_reviews_df = pd.concat(category_results.values(), ignore_index=True)

def get_three_closest_reviews(input_review):
    query_res = collection.query(
        query_texts=[input_review],
        n_results=3,
        include=["documents"]
    )
    return query_res["documents"][0]

first_review = "Absolutely wonderful - silky and sexy and comfortable"
most_similar_reviews = get_three_closest_reviews(first_review)

print(most_similar_reviews)
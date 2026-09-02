from datasets import load_dataset

my_dataset = load_dataset("TIGER-Lab/MMLU-Pro", split="validation")

# Display dataset details
print(my_dataset)

# 1. Load your dataset
dataset = load_dataset("imdb", split="train")

# 2. Filter for a specific condition
filtered_dataset = dataset.filter(lambda example: example["label"] == 1)

# 3. Choose a range from the filtered results (e.g., rows 10 to 50)
start_idx = 10
end_idx = 50
range_dataset = filtered_dataset.select(range(start_idx, end_idx))

print(range_dataset[0]["text"])

# filtered = wikipedia.filter(lambda row: "football" in row["text"])

# # Create a sample dataset
# example = filtered.select(range(1))

# print(example[0]["text"])

# search = wikipedia.filter(lambda row: "May 25" in row["text"])
# result = search.select(range(4))

# for val in result:
#     print(val["text"])
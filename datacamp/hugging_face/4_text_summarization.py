from transformers import pipeline

original_text = """"""

# Create the summarization pipeline
summarizer = pipeline(task="summarization", model="cnicu/t5-small-booksum")

# Summarize the text
summary_text = summarizer(original_text)

# Compare the length
print(f"Original text length: {len(original_text)}")
print(f"Summary length: {len(summary_text[0]['summary_text'])}")

short_summarizer = pipeline(task="summarization", model="cnicu/t5-small-booksum", min_new_tokens=1, max_new_tokens=10)

short_summary_text = short_summarizer(original_text)

print(short_summary_text[0]["summary_text"])

long_summarizer = pipeline(task="summarization", model="cnicu/t5-small-booksum", min_new_tokens=50, max_new_tokens=150)

long_summary_text = long_summarizer(original_text)

print(long_summary_text[0]["summary_text"])
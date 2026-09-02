from transformers import pipeline
from huggingface_hub import InferenceClient
import os

gpt2_pipeline = pipeline(
    task="text-generation", 
    model="openai-community/gpt2", 
)
results = gpt2_pipeline("How to Learn Ai", max_new_tokens=10, num_return_sequences=2)

for result in results:
    print(result['generated_text'])

client = InferenceClient(
    provider="together",
    api_key=os.environ["HF_KEY"]
)

completion = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-V3",
    messages=[{
        "role": "user",
        "content": "What is the capital of belgium"
    }]
)

print(completion.choices[0].message)
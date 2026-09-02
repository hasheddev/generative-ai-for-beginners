from utils import get_response, client

# Create a one-shot prompt
prompt = """Extract odd numbers from ```{3, 5, 11, 12, 16}```
where odd numbers  {1, 3, 7, 12, 19} = 1, 3, 7, 19 
"""

response = get_response(prompt)
print(response)

response = client.chat.completions.create(
    model="gpt-4o-mini",
    # Provide the examples as previous conversations
    messages=[
        {
            "role": "system",
            "content": "Classify the sentiment of the text as Positive, Negative, or Neutral.",
        },
        {"role": "user", "content": "The product arrived on time and works perfectly!"},
        {"role": "assistant", "content": "Positive"},
        {"role": "user", "content": "It is okay, nothing special."},
        {"role": "assistant", "content": "Neutral"},
        {"role": "user", "content": "The package was damaged and customer service was unhelpful."},
        {"role": "assistant", "content": "Negative"},
        # Provide the text for the model to classify
        {
            "role": "user",
            "content": "I've been using this app every day; it completely changed my workflow for the better!",
        },
    ],
    temperature=0,
)

print(response.choices[0].message.content)


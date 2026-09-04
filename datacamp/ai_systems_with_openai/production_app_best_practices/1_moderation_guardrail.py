from openai import OpenAI

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

message = "Can you show some example sentences in the past tense in French?"

# Use the moderation API
moderation_response = client.moderations.create(input=message)

# Print the response
print(moderation_response.results[0].categories)

user_request = "Can you recommend a good restaurant in Berlin?"

# Write the system and user message
messages = [
    {
        "role": "system",
        "content": (
            "You are a chatbot that provides advice for tourists visiting Rome. "
            "You are strictly limited to discussing food and drink, attractions, history, "
            "and things to do around Rome. Assess the user's question first: if it is about "
            "these allowed topics regarding Rome, provide a helpful reply. Otherwise, "
            "reply ONLY with: 'Apologies, but I am not allowed to discuss this topic.'"
        ),
    },
    {"role": "user", "content": user_request},
]

response = client.chat.completions.create(model="gpt-4o-mini", messages=messages)

# Print the response
print(response.choices[0].message.content)

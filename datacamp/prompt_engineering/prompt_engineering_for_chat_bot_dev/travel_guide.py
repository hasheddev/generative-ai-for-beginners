from openai import OpenAI

# Define the model to use
model = "gpt-4o-mini"

# Define the client
client = OpenAI()

# Start coding here
# Add as many cells as you like
system_prompt = "You are an expert Parisian travel guide working for Peterman Reality Tours. Your task is to assist tourists by providing clear, accurate, and concise information about iconic Parisian landmarks, driving distances, artwork, and local treasures. Keep your answers helpful, friendly, and brief."

conversation = [{"role": "system", "content": system_prompt}]

questions = [
    "How far away is the Louvre from the Eiffel Tower (in miles) if you are driving?",
    "Where is the Arc de Triomphe?",
    "What are the must-see artworks at the Louvre Museum?",
]

for question in questions:
    conversation.append({"role": "user", "content": question})
    response = client.chat.completions.create(
        messages=conversation,
        model=model,
        temperature=0.0,
        max_completion_tokens=100
    )
    assistant_response = response.choices[0].message.content
    conversation.append({"role": "assistant", "content": assistant_response})
print(conversation) 
from openai import OpenAI

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Define the conversation messages
conversation_messages = [
    {"role": "system", "content": "You are a helpful event management assistant."},
    {"role": "user", "content": "What are some good conversation starters at networking events?"},
    {"role": "assistant", "content": (
            "Here are a few effective conversation starters for networking"
            " events:\n\n1. **Event-Focused:** 'What brings you to this"
            " event today?' or 'Have you attended this conference before?'\n2."
            " **Role & Industry:** 'What kind of projects are you currently"
            " working on?' or 'What do you enjoy most about your work?'\n3."
            " **Lighthearted & Casual:** 'What’s been your favorite session or"
            " takeaway so far?' or 'How did you hear about this event?'\n\nKeep"
            " your delivery open and friendly, and follow up by actively"
            " listening to their response!"
        )
    }
]

response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=conversation_messages
)
print(response.choices[0].message.content)

shown = """Here are some effective conversation starters for networking events:

1. **Event-Focused Questions:**
   - "What brings you to this event today?"
   - "Have you attended this conference before? How was your experience?"

2. **Role & Industry Discussion:**
   - "What kind of projects are you currently working on?"
   - "What do you enjoy most about your work or industry?"

3. **Session Insights:**
   - "What’s been your favorite session or takeaway so far?"
   - "Did you have a chance to see any interesting speakers today?"

4. **Shared Interests:**
   - "What challenges are you currently facing in your work?"
   - "How did you get started in your field?"

5. **Future Trends:**
   - "What trends do you see shaping our industry in the next few years?"
   - "Are there any new technologies or practices you're excited about?"

6. **Personal Touch:**
   - "What do you like to do outside of work?"
   - "Do you have any book or podcast recommendations that you’ve found helpful lately?"

7. **Learning Opportunities:**
   - "Is there any skill you’re currently trying to develop?"
   - "What’s the best piece of professional advice you’ve ever received?"

Remember to approach conversations with curiosity and openness, and follow up with thoughtful questions based on their responses to keep the dialogue flowing!
"""

def get_response(prompt):
  # Create a request to the chat completions endpoint
  response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}], 
    temperature = 0)
  return response.choices[0].message.content

# Test the function with your prompt
response = get_response("write a poem about ChatGPT.")
print(response)
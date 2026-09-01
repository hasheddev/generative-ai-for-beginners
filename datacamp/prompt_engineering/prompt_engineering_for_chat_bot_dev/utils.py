from openai import OpenAI

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

def get_response(system_prompt, user_prompt):
  # Create a request to the chat completions endpoint
  response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "system", "content": system_prompt},
      		  {"role": "user", "content": user_prompt}],
    temperature = 0)
  return response.choices[0].message.content
from openai import OpenAI

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

measurements = []
messages = []
# Provide a system message and user messages to send the batch
messages.append({"role": "system", "content": "convert the given measurements from kilometers to miles and present the response in a table containing both original and converted measurements"})
# Append measurements to the message
[messages.append({"role": "user", "content": f"{i}"}) for i in measurements]
model = ''
response = client.chat.completions.create(
      model=model,
      messages=messages
      )
print(response)
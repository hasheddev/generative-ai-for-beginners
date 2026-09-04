from openai import OpenAI
from uuid import uuid4

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

unique_id = str(uuid4())

messages=[]

response = client.chat.completions.create(  
  model="gpt-4o-mini", 
  messages=messages,
# Pass a user identification key
  user=unique_id
)

print(response.choices[0].message.content)
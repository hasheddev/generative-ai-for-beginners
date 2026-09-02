from utils import get_response

#can be applied to previous techniques

prompt = "Give me the top 10 pre-trained language models"

prompt = """Give me the top 10 pre-trained language models.
Generate a table presenting information on each model's name, release year and its owning company."""

response = get_response(prompt)
print(response)

prompt = """
Receiving a promotion at work made me feel on top of the world -> Happiness
The movie's ending left me with a heavy feeling in my chest -> Sadness
Walking alone in the dark alley sent shivers down my spine -> Fear
Time flies like an arrow -> no explicit emotion.
He picked up the keys from the table and opened the door -> no explicit emotion.
They sat and ate their meal ->
"""

response = get_response(prompt)
print(response)
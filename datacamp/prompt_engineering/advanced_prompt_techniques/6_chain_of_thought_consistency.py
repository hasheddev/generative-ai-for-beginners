from utils import get_response

prompt = """determine my friend's father's age in 10 years, given that he is currently twice your friend's age, and your friend is 20.
A: do this step by step
"""

response = get_response(prompt)
print(response)

example = """Q: Sum the even numbers in the following set: {9, 10, 13, 4, 2}.
             A: Even numbers: 10, 4, 2. Adding them: 10+4+2=16"""

# Define the question
question = """Q:  Sum the even numbers in the following set: 15, 13, 82, 7, 14}
              A:"""

# Create the final prompt
prompt = example + question
response = get_response(prompt)
print(response)

self_consistency_instruction = (
    "Have 3 independent experts solve the problem inside the backticks. "
    "Keep each expert's step-by-step reasoning concise. "
    "Finally, combine their results and determine the final answer using a majority vote."
)

# Create the problem to solve
problem_to_solve = "If you own a store that sells laptops and mobile phones. You start your day with 50 devices in the store, out of which 60% are mobile phones. Throughout the day, three clients visited the store, each of them bought one mobile phone, and one of them bought additionally a laptop. Also, you added to your collection 10 laptops and 5 mobile phones. How many laptops and mobile phones do you have by the end of the day?"

# Create the final prompt
prompt = f"{self_consistency_instruction}\n```{problem_to_solve}```"

response = get_response(prompt)
print(response)
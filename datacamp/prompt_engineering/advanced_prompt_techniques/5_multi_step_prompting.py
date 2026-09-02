#Least to most, 
from utils import get_response

prompt = """Make a plan for a beach vacation:
Step 1: Give four potential locations.
Step 2: State accommodation options for each location.
Step 3: State activities available at each location.
Step 4: Evaluate the pros and cons of each location."""

response = get_response(prompt)
print(response)

code = '''
def calculate_rectangle_area(length, width):
    area = length * width
    return area
'''

# Create a prompt that analyzes correctness of the code
prompt = f"""Assess the function provided in the code string delimited by backticks:
```{code}```

Follow these steps:
Step 1: Check if the function has correct syntax.
Step 2: Check if the function receives two inputs.
Step 3: Check if the function returns one output."""

response = get_response(prompt)
print(response)
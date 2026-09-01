from utils import get_response

#use examples or problem description, language and format(function, class) to generate or modify code

prompt = """
create a python function that accepts a list of 12 numbers representing sales for each month of the year and outputs the month with the highest sales value
"""

response = get_response(prompt)
print(response)

examples="""input = [10, 5, 8] -> output = 23
input = [5, 2, 4] -> output = 11
input = [2, 1, 3] -> output = 6
input = [8, 4, 6] -> output = 18
"""

prompt = f"""use the exampes in the delimited in the backtick to generate a python function that predicts the estimated completion time of 
a project based on historical data ```{examples}```"""

response = get_response(prompt)
print(response)


function = """def calculate_area_rectangular_floor(width, length):
					return width*length"""

# Craft a multi-step prompt that asks the model to adjust the function
prompt = f"""adjust the function in the backticks```{function}```
follow these steps
step 1: return the area of the rectangle as well the perimeter
step 2: test if the inputs (floor dimensions) are positive, and if not, display appropriate error messages."""

response = get_response(prompt)
print(response)

prompt = f"""Explain the function in the backticks. ```{function}```
A: do this step by step"""
 
response = get_response(prompt)
print(response)
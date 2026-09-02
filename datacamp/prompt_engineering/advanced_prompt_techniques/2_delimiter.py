from .utils import get_response

story = """With a mix of excitement and trepidation, Alex decided to retrieve the sphere.
As they reached out to touch it, a surge of energy coursed through their body, and the ship's systems flickered.
Suddenly, Alex found themselves in a vast, starry expanse, surrounded by swirling galaxies and vibrant nebulae.
The sphere had transported them to a different dimension."""

# Create a prompt that completes the story
#prompt = f"""Complete the story below delimited by the triple backticks  ```{story}```"""

prompt = f"""Complete the story below delimited by the triple backticks in two paragraphs and in the Shakespeare style ```{story}```"""

# Get the generated response
response = get_response(prompt)

# Get the generated response 
response = get_response(prompt)

print("\n Original story: \n", story)
print("\n Generated story: \n", response)
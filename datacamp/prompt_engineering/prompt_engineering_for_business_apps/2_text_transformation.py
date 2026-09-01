from utils import get_response

# rephrasing for target audience, proofreading, language translation
marketing_message = " Introducing our latest collection of premium leather handbags. Each bag is meticulously crafted using the finest leather, ensuring durability and elegance. With a variety of designs and colors, our handbags are perfect for any occasion. Shop now and experience the epitome of style and quality."

prompt = f"""translate the text in backticks from english to french, spanish and japanese ```{marketing_message}```"""
 
response = get_response(prompt)

print("English:", marketing_message)
print(response)

sample_email = """ 
Subject: Check out our latest products!

Dear Customer,

We are excited to introduce our latest product line that includes a wide range of items to suit your needs. Whether you're looking for electronics, home appliances, or fashion accessories, we have it all!

Hurry and visit our website to explore the fantastic deals and discounts we have for you. Don't miss out on the opportunity to get the best products at unbeatable prices.

Thank you for being a valued customer, and we look forward to serving you soon!

Best regards,
The Marketing Team"""

prompt = f"""transform the tone of the text in backtick to be professonal, positive and user-centric```{sample_email}```"""

response = get_response(prompt)

print("Before transformation: \n", sample_email)
print("After transformation: \n", response)

shown = """Subject: Discover Our Latest Product Offerings!

Dear Valued Customer,

We are pleased to announce the launch of our latest product line, thoughtfully designed to meet your diverse needs. From cutting-edge electronics to essential home appliances and stylish fashion accessories, we have something for everyone.

We invite you to visit our website to explore the exceptional deals and discounts available to you. This is a wonderful opportunity to find high-quality products at competitive prices.

Thank you for your continued support. We look forward to serving you and enhancing your experience with us!

Warm regards,  
The Marketing Team"""

text = " Hey guys, wanna know a cool trick? Here's how u can up your productivity game! First, download this awesome app, it's like the best thing ever! Then, just start using it and u'll see the difference. Its super easy and fun, trust me! So, what are u waiting for? Try it out now!"

prompt = f"""Follow these steps to adjust the text delimited by triple backticks:
Step 1: Proofread the text without changing its structure.
Step 2: Adjust its tone to be formal and friendly.

```{text}```"""

response = get_response(prompt)

print("Before transformation:\n", text)
print("After transformation:\n", response)

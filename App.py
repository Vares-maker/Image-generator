import streamlit as st
from PIL import Image
Input = st.text_input("Type the prompt:")
import requests
image_url = "https://image.pollinations.ai/prompt/"+Input  # Replace with the actual image URL

response = requests.get(image_url)
if response.status_code == 200:
    with open("image.jpg", "wb") as f:
        f.write(response.content)
    print("Image downloaded successfully!")
else:
    print("Failed to download the image.")

# Open the image file
image = Image.open('image.jpg')

# Display the image
st.image(image, caption='The output', use_column_width=True)

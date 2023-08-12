import streamlit as st
import requests
from PIL import Image
import json
from io import BytesIO
import os

# Get the API_URL endpoint from the environment variable
api_url = os.getenv("API_URL")

if api_url:
    print("API URL:", api_url)
else:
    print("API URL environment variable not set.")

st.title("Image Classification with FastAPI and Streamlit")

# Input: URL
url_input = st.text_input("Enter Image URL:", "")

# Add a "Submit" button
submit_button = st.button("Classify")

if submit_button and url_input:
    try:
        # Load the image from the URL
        response = requests.get(url_input)
        response.raise_for_status()  # Check for request errors

        # Display the image from the URL
        image = Image.open(BytesIO(response.content))
        st.image(image, caption="Loaded Image", use_column_width=True)

        # Define API data
        api_data = {
            "user_id": "streamlit_user",
            "image_url": url_input  # Pass the image URL directly
        }

        headers = {'Content-type': 'application/json', 'Accept': 'application/json'}

        # Make a POST request to the FastAPI API
        response = requests.post(api_url, data=json.dumps(api_data), headers=headers)

        # Display the API response
        if response.status_code == 200:
            result = response.json()
            st.subheader("Prediction:")
            for pred in result["prediction"]:
                st.write(f"Class::: '{pred['className']}' -------------- Probability: {pred['probability']:.2f}")
        else:
            st.error("Error occurred while processing the image.")
    except Exception as e:
        st.error(f"Error: {str(e)}")

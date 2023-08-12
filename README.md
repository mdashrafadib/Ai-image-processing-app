# Image Classification App using FastAPI and Streamlit

This project demonstrates an image classification application built using FastAPI for the backend and Streamlit for the frontend. Users can input an image URL, and the app will display the loaded image and provide predictions for the objects in the image.

## Prerequisites

- Docker: To containerize the application.
- Python: To run the Streamlit app locally (if desired).

## Usage

### Running the Streamlit App Locally

1. Clone the repository:
   -    ```bash
        git clone <repository-url>
        ```
   -    ```bash
        cd <repository-directory>
        ```

2. Install the required Python packages:
   -    ```bash
        pip install -r requirements.txt
        ```

3. Set the environment variable `API_URL` to the FastAPI API endpoint. Replace `<fastapi-api-url>` with the actual URL:
   -    ```bash 
        export API_URL=<fastapi-api-url>
        ```

4. Run the Streamlit app:
   -    ```bash
        streamlit run streamlit_app.py    
        ```

5. Access the app in your web browser at `http://localhost:8501`.

### Running the Application using Docker

1. Clone the repository:
   -    ```bash
        git clone <repository-url>
        ```
   -    ```bash
        cd <repository-directory>
        ```

2. Build the Docker image:
   -    ```bash
        docker build -t image-classification-app .
        ```

3. Run the Docker container:
   -    ```bash
        docker run -p 8501:8501 -e API_URL=<fastapi-api-url> image-classification-app
        ```

4. Access the app in your web browser at `http://localhost:8501`.

## Files

- `streamlit_app.py`: Streamlit frontend application code. This script allows users to input an image URL and displays image predictions using the FastAPI backend.

- `Dockerfile`: Docker configuration to build an image for the application. It installs necessary packages and sets up the Streamlit app to run.

- `requirements.txt`: List of required Python packages for the application.

## Notes

- Ensure that the FastAPI API endpoint is up and running before using the Streamlit app.

- The API URL should be set as an environment variable `API_URL` to enable communication between the Streamlit app and the FastAPI backend.

- This README provides basic instructions for running the application locally and using Docker. Adjustments might be needed based on your environment and requirements.

import os
import base64
import streamlit as st
import anthropic
from anthropic import Anthropic
import requests

# Initialize Claude client
client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

# Set up the Streamlit application with tabs
st.set_page_config(page_title="Image Analysis with Anthropic Claude", layout="wide")
st.title("Transcription and Information Extraction with Anthropic Claude")

# Function to encode an image to base64
def get_base64_encoded_image(image_path):
    with open(image_path, "rb") as image_file:
        binary_data = image_file.read()
        base_64_encoded_data = base64.b64encode(binary_data)
        base64_string = base_64_encoded_data.decode('utf-8')
        return base64_string

# Function to send a prompt to the Claude model
def send_claude_request(image_path, instruction, model):
    image_data_base64 = get_base64_encoded_image(image_path)
    message_list = [
        {
            "role": 'user',
            "content": [
                {"type": "image", "source": {"type": "base64", "media_type": "image/jpeg", "data": image_data_base64}},
                {"type": "text", "text": instruction}
            ]
        }
    ]
    response = client.completions.create(
        model=model,
        messages=message_list,
        max_tokens_to_sample=1000
    )
    return response.completion

# Function to dynamically fetch available models
def get_available_models():
    # Assuming the client has a method to list available models
    models = client.models.list()
    return [model['name'] for model in models]

# Define the tabs
tab1, tab2, tab3 = st.tabs(["Use Cases", "Upload Image", "About"])

# Use Case Tab
with tab1:
    st.header("Select Use Case")
    
    # Define the use cases based on the notebook
    use_cases = [
        "Transcribing Typed Text",
        "Transcribing Handwritten Text",
        "Transcribing Forms",
        "Complicated Document QA",
        "Unstructured Information -> JSON",
        "User Defined"
    ]
    
    # Dropdown menu for selecting use cases
    selected_use_case = st.selectbox("Choose a Use Case:", use_cases)
    
    # Provide instructions based on the selected use case
    instructions = {
        "Transcribing Typed Text": "Transcribe this typed text.",
        "Transcribing Handwritten Text": "Transcribe this handwritten note.",
        "Transcribing Forms": "Transcribe this form exactly.",
        "Complicated Document QA": "Answer the questions based on this document.",
        "Unstructured Information -> JSON": "Convert the content of this document to structured JSON.",
        "User Defined": ""
    }
    
    # Dynamically fetch the available models
    available_models = get_available_models()
    selected_model = st.selectbox("Choose a model:", available_models)
    
    # Allow user to choose or provide an image
    image_selection = st.radio("Choose an image:", ("Use uploaded image", "Use default image"))
    
    # Custom prompt input for "User Defined" use case
    if selected_use_case == "User Defined":
        instruction_text = st.text_area("Enter your prompt:", "")
    else:
        instruction_text = instructions[selected_use_case]
    
    # Image path to be used for processing
    image_path = None
    
    if image_selection == "Use uploaded image":
        uploaded_images_dir = "uploaded_images"
        images_list = os.listdir(uploaded_images_dir)
        if images_list:
            image_name = st.selectbox("Select an uploaded image:", images_list)
            image_path = os.path.join(uploaded_images_dir, image_name)
        else:
            st.warning("No uploaded images found. Please upload an image in the 'Upload Image' tab.")
    
    else:
        # Placeholder for default image path for each use case
        default_images = {
            "Transcribing Typed Text": "./data/examples/ex1-stack_overflow.png",
            "Transcribing Handwritten Text": "./data/examples/ex2-school_notes.png",
            "Transcribing Forms": "./data/examples/ex3-vehicle_form.jpeg",
            "Complicated Document QA": "./data/examples/ex4-doc_qa.png",
            "Unstructured Information -> JSON": "./data/examples/ex5-org_chart.jpeg"
        }
        image_path = default_images.get(selected_use_case)
        st.image(image_path, caption="Default Image", use_column_width=True)
    
    # Process the request if an image is selected and prompt is not empty
    if image_path and instruction_text and st.button("Process with Claude"):
        # Send request to Claude and display the response
        response = send_claude_request(image_path, instruction_text, selected_model)
        st.subheader("Claude's Response:")
        st.write(response)

# Image Upload Tab
with tab2:
    st.header("Upload Image")
    
    # Define the upload directory
    upload_directory = "uploaded_images"
    os.makedirs(upload_directory, exist_ok=True)
    
    # File uploader to select an image
    uploaded_file = st.file_uploader("Upload an image for transcription", type=["png", "jpg", "jpeg"])
    
    if uploaded_file:
        # Save uploaded image to the directory
        file_path = os.path.join(upload_directory, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success(f"Image saved to {file_path}")
        st.image(file_path, caption="Uploaded Image", use_column_width=True)

# About Tab
with tab3:
    st.header("About")
    st.write(
        '''
        This application allows users to transcribe and extract information from various types of documents using the Claude model by Anthropics.
        The functionality includes transcribing typed or handwritten text, extracting data from forms, performing QA on complex documents, and converting unstructured information into JSON.
        Use the tabs to explore different use cases, upload images for processing, and learn more about the app.
        '''
    )

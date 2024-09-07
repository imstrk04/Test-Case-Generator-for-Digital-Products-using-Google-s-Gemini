"""
This module is all about making it easier to create detailed test cases for
images you upload. It’s part of a user-friendly Streamlit app designed to help you generate 
test cases for various image-based functionalities using advanced AI.

With this app, you can upload your images and even add some extra context if you want. 
The AI then takes this information and produces step-by-step test case instructions tailored 
to your needs. These instructions come complete with descriptions, what needs to be set up 
before testing, detailed testing steps, and what you should expect as a result.

We’re using Google’s Gemini API to power the content generation, ensuring high-quality and 
useful test cases. The app provides a straightforward interface where you can easily upload 
your images, enter additional context, and see the generated instructions all in one place.

Created on Sat Sept 7 2024

Original Author: T. Sadakopa Ramakrishnan <nstsrka04@gmail.com>
"""


from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

chat = model.start_chat(history=[])

default_prompt = """
    What is a Test Case?
    A Test Case is a specific set of conditions or variables under which a tester will determine whether an application, software system, or one of its features is working correctly or not. A Test Case aims to validate software features’ accuracy, completeness, and reliability. A test case usually includes the following details:
    test case ID,
    test case description,
    steps to follow,
    expected results,
    pass/fail criteria, and
    status of the test case.
    A successful test case should identify correct and incorrect results, and any unexpected results should be reported as a bug. Test cases provide the basis for exhaustively testing a system and thus help increase the reliability and quality of the system by uncovering mistakes or gaps in the system.

    What are the Manual Test Cases?
    Manual testing involves testing software manually, i.e., without using any automated tools. For executing this testing, you sometimes create test cases beforehand. These test cases are called manual test cases. Manual test cases are written in a clear and precise manner, which helps testers to understand and execute the tests accurately. Moreover, manual test cases can be used multiple times to execute tests, helping to save time and money on software testing.

    How to write test cases: A step-by-step guide
    Step 1 – Test Case ID:
    In this step, the tester will assign a unique identifier to the test case. This allows the tester to recall and identify the test case in the future easily.

    Step 2 – Test Case Description:
    The tester will describe the test case, outlining what it is designed to do. 

    Step 3 – Pre-Conditions:
    The tester will document any pre-conditions that need to be in place for the test case to run properly.

    Step 4 – Test Steps:
    The tester will document the detailed steps necessary to execute the test case.

    Step 5 – Test Data:
    The tester will define any necessary test data.

    Step 6 – Expected Result:
    The tester will provide the expected result of the test.

    Step 7 – Post Condition:
    The tester will provide any cleanup that needs to be done after running the test case.

    Step 8 – Actual Result:
    The tester will document the actual result of the test.

    Step 9 – Status:
    The tester will report the status of the test.

    Best Practice for writing good Test Case:
    Identify the purpose of the test case, write it clearly and concisely, consider all scenarios and edge cases, maintain organization and structure, and review and refine periodically.

    Benefits of writing high-quality Test cases:
    Accurately identify issues, enhance test coverage, enrich software quality, improve collaboration between stakeholders, and improve user experience.
    
    so,
    Describe a detailed, step-by-step guide on how to test the functionality for the image provided. Each test case should include:
    - Description: What the test case is about.
    - Pre-conditions: What needs to be set up or ensured before testing.
    - Testing Steps: Clear, step-by-step instructions on how to perform the test.
    - Expected Result: What should happen if the feature works correctly.
    Manual testing is a way of testing software applications, products, and systems while using a minimum number of tools or sometimes without using any tools. This blog will provide an overview of the fundamentals of writing effective test cases in manual testing and key tips and strategies to consider. Creating good test cases requires careful planning, attention to detail, and a deep understanding of the software to be tested. But don’t worry, with a well-designed test case; you can save time and effort and make the testing process super efficient.

    use above details for format
    
    """

def get_gemini_response(input_text, image):
    multimodal_input = [input_text] if input_text else [default_prompt]
    multimodal_input.append(image)

    response = model.generate_content(multimodal_input)
    
    result_text = ""
    for candidate in response.candidates:
        for part in candidate.content.parts:
            result_text += part.text
    
    return result_text

# Initialise Streamlit App

st.set_page_config(page_title="LLM Test Case Generator")

st.header("Multimodal LLM Tool for Testing Instructions Generation")

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input_text = st.text_input("Input Prompt (Optional): ", key="input", placeholder="Enter additional context here...")
uploaded_files = st.file_uploader("Choose Image(s)...", type=["jpg", "jpeg", "png"], accept_multiple_files=True)
images = []

if uploaded_files:
    for uploaded_file in uploaded_files:
        image = Image.open(uploaded_file)
        images.append(image)
        st.image(image, caption="Uploaded Image", use_column_width=True)

submit = st.button("Generate Testing Instructions")

# Handle the submit button click
if submit:
    if not images:
        st.error("Please upload at least one image.")
    else:
        with st.spinner('Generating instructions...'):
            for i, image in enumerate(images):
                response = get_gemini_response(input_text, image)
                st.subheader(f"Generated Testing Instructions for Image {i+1}")
                st.write(response)
                st.session_state['chat_history'].append(("You", input_text))
                st.session_state['chat_history'].append((f"Bot (Image {i + 1})", response))

st.subheader("Chat History:")
for role, text in st.session_state['chat_history']:
    st.write(f"**{role}:** {text}")

from dotenv import load_dotenv
load_dotenv()
import google.generativeai as genai
import os
import streamlit as st
import random
import datetime
from PIL import Image
from utils import input_image_details, writeTofile, extract_text_from_image, download_butt
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.text

def get_gemini_vision_response(input,image,user_prompt):
    model=genai.GenerativeModel('gemini-pro-vision')
    response=model.generate_content([input,image[0],user_prompt])
    return response.text

prompt=[
    """
    You are an expert in converting youtube transcript to a detailed self prepared notes to properly formatted well documented with explntion in markdown code!
    also add usefull explanation for every line used for documentation also the markdown code should have appropriate explanation in short.
    """,
    
    """
    you are an expert in OCR that is optical character recognition you need to extract each and every thing from the image and give me the extracted text!
    and also  You are an expert in converting English language self prepared notes to properly formatted markdown code!
    also add usefull explanation for every line used for documentation also the markdown code should have appropriate explanation in short.
    """,

]
st.set_page_config(page_title="notes for self")
st.header("Gemini App To Make Notes")

question = st.text_input("INPUT : ",key="input")
st.write(question)

uploaded_file = st.file_uploader("Choose an image of the invoice...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)


submit = st.button("give me my notes in formatted way")


if submit:
    if uploaded_file:
        image_data =  input_image_details(uploaded_file)
        response = get_gemini_vision_response(prompt[1],image_data,question)
        st.write(response)
        # st.write(extract_text_from_image(uploaded_file))
        download_butt(response)

    else:
            
        response = get_gemini_response(question=question,prompt=prompt)
        # writeTofile(response)
        st.write(response)

        # Add download button
        download_butt(response)




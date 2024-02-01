from dotenv import load_dotenv
load_dotenv()
import google.generativeai as genai
import os
import streamlit as st
import random
import datetime
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.text

prompt=[
    """
    You are an expert in converting English language self prepared notes to properly formatted markdown code!
    also add usefull explanation for every line used for documentation also the markdown code should have appropriate explanation in short. 
    """


]
st.set_page_config(page_title="notes for self")
st.header("Gemini App To Make Notes")

question = st.text_input("INPUT : ",key="input")
st.write(question)
submit = st.button("give me my notes in formatted way")

def writeTofile(file_content:str,filename="notes_{}.md".format(datetime.datetime.now())):
    with open(filename,"a") as f:

        f.writelines(file_content)
    


if submit:
    response = get_gemini_response(question=question,prompt=prompt)
    writeTofile(response)
    st.write(response)

      # Add download button
    download_button = st.download_button(
        label="Download your notes",
        data=response,
        file_name=f"notes_{datetime.datetime.now()}.md",
        key="download_button"
    )
    st.markdown(download_button, unsafe_allow_html=True)




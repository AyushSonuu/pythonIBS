import datetime
from PIL import Image
import pytesseract
import streamlit as st

def input_image_details(uploaded_file):
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

def writeTofile(file_content:str,filename="notes_{}.md".format(datetime.datetime.now())):
    with open(filename,"a") as f:

        f.writelines(file_content)
    


def extract_text_from_image(image_path):
    try:
        
        image = Image.open(image_path)

        
        text = pytesseract.image_to_string(image)

        return text
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    print(extract_text_from_image("./imgg.jpg"))



def download_butt(response):
    download_button = st.download_button(
            label="Download your notes",
            data=response,
            file_name=f"notes_{datetime.datetime.now()}.md",
            key="download_button"
        )
    st.markdown(download_button, unsafe_allow_html=True)
    
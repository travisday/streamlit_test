import streamlit as st
from io import StringIO
import os


st.title('EDL Editor')

uploaded_file = st.file_uploader("Upload EDL .txt file", type=['txt'], accept_multiple_files=False, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False)
if uploaded_file:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    string_data = stringio.read()
    lines = string_data.splitlines()
    subA = lines[len(lines)-1][:34]
    lines[len(lines)-1] = subA + "tk03_comp_V001.mov"
    
    files = [file for file in os.listdir("/Users/Travis/Desktop") if not file.startswith('.')] # Ignore hidden files
    st.write(files)


    new_string = ""

    for line in lines:
        new_string += line + "\n"
    
    st.download_button('Download some text', new_string)
    


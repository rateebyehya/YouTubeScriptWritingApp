#UI of the application 

import streamlit as st 
from utils import generate_script
#Applying Styling 

st.markdown("""
            
<style>  
div.stButton > button:first-child {
    background-color: #0099ff;
    color:#ffffff;
}
div.stButton > button:hover {
    background-color: #00ff00;
    color:#FFFFFF;
}
<style>""", unsafe_allow_html=True
    )

#Creating Session State Variable
if "API_Key" not in st.session_state: 
    #This is to hold the API_Key throughouts the session 
    st.session_state['API_Key'] = ''

st.title("❤️ YouTube Script Writing Tool")

#Sidebar to capture the API key from OPENAI
st.sidebar.title("🔑😎")
st.session_state['API_Key']= st.sidebar.text_input("What is your API key?", type="password")
st.sidebar.image('./Youtube.png', width = 300, use_column_width=True)

#Capture user input 
prompt = st.text_input("Please provide the topic of the video")
video_length=st.text_input("Expected Video Length ⏰ (in minutes)")
creativity = st.slider("Creativity 💫 - (0 LOW || 1 HIGH)", 0.0, 1.0, 0.2, step = 0.1)

submit = st.button("Generate Script for me")
#The markdown in the beginning of the video is for this (the button changes color if you hover on it)
#The markdown is telling the application that whenever the user hovers over the button, to change its colors 

if submit: 

    if st.session_state['API_Key']:

        search, title, script = generate_script(prompt, video_length, creativity, st.session_state['API_Key'])

        #Let us generate the script 
        st.success('Hope you like this script!')

        #Display title 
        st.subheader("Title:🔥")
        st.write(title)

        #Display Video Script 
        st.subheader("Your Video Script:📝")
        st.write(script)

        #Display Search Engine Results 
        st.subheader("Checkout - DuckDuckGo Search: 🔍")
        st.write()

        with st.expander("Show me 👀"):
            st.info(search) #the difference between .info() and .write is that .info() is an EXPANDER on streamlit

    else: #If API key is not provided
        st.error("Ooooopsssss.... Please provide API KEY.....")
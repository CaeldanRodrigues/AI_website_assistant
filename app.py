import os

import streamlit as st

# Creating Session State Variable
if 'HuggingFace_API_Key' not in st.session_state:
    st.session_state['HuggingFace_API_Key'] = os.environ['HUGGINGFACEHUB_API_KEY']
if 'Pinecone_API_Key' not in st.session_state:
    st.session_state['Pinecone_API_Key'] = os.environ['PINECONE_API_KEY']


#
st.title('🤖 AI Website Assistant') 

# Sidebar

# capture the API keys
# st.sidebar.title("😎🗝️")
# st.session_state['HuggingFace_API_Key']= st.sidebar.text_input("What's your HuggingFace API key?",type="password")
# st.session_state['Pinecone_API_Key']= st.sidebar.text_input("What's your Pinecone API key?",type="password")

load_button = st.sidebar.button("Load data to Pinecone", key="load_button")

#If the bove button is clicked, pushing the data to Pinecone...
if load_button:
    #Proceed only if API keys are provided
    if st.session_state['HuggingFace_API_Key'] !="" and st.session_state['Pinecone_API_Key']!="" :

        # fetch and push data to Pinecone

        st.sidebar.success("Data pushed to Pinecone successfully!")
    else:
        st.sidebar.error("ERROR! Please provide the API keys")
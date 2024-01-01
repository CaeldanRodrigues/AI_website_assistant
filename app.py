import os
import streamlit as st

from utils import *
import constants

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

if load_button:
    if st.session_state['HuggingFace_API_Key'] !="" and st.session_state['Pinecone_API_Key']!="" :

        site_data=get_website_data(constants.WEBSITE_URL)
        st.write("Data pull done...")

        chunks_data=split_data(site_data)
        st.write("Spliting data done...")

        embeddings=create_embeddings()
        st.write("Embeddings instance creation done...")

        push_to_pinecone(st.session_state['Pinecone_API_Key'],constants.PINECONE_ENVIRONMENT,constants.PINECONE_INDEX,embeddings,chunks_data)
        st.write("Pushing data to Pinecone done...")

        st.sidebar.success("Data pushed to Pinecone successfully!")
    else:
        st.sidebar.error("ERROR! Please provide the API keys")
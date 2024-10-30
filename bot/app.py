import streamlit as st
import os
from config import get_settings

settings = get_settings()

os.environ["GOOGLE_API_KEY"] = settings.google_api
os.environ["GOOGLE_CSE_ID"] = settings.google_cse_id
os.environ["OPENAI_API_KEY"] = settings.openai_api

st.set_page_config(
    page_title="Langchain Chatbot",
    page_icon='💬',
    layout='wide'
)

st.header(settings.header)
st.markdown(settings.template)

import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
from langchain_groq import ChatGroq
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    st.error("Groq API key not found in environment variables.")
    st.stop()

st.header("Fitness AI ChatBot")
model_name = st.selectbox("Select Groq Model",["llama3-8b-8192","qwen-2.5-32b"])
try:
    chat = ChatGroq(temperature=0.7 , groq_api_key = groq_api_key , model_name = model_name )
except Exception as e:
    st.error(f"Error initializing Groq chatbot: {str(e)}")
    st.stop()

user_input = st.text_input("Enter your question")
if st.button("Ask"):
    if user_input.strip():
        try:
            response = chat.invoke(user_input)
            st.write(response.content)
        except Exception as e:
            st.write(f"An error occured: {str(e)} ")
    else:
        st.warning("Please enter a question.")

from langchain.chat_models import init_chat_model
from pydantic import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

# prompt Template

prompt = ChatPromptTemplate.from_messages(
    [

        ("system", "you are a helpful assistant. Please respond to the user queries"),
        ("user","Question:{question}")
    ]
)

## Streamlit Framework

st.title('Langchain demo with OPENAI API')
input_text = st.text_input("search the topic you want")

# Ollama LLM Model

llm = ChatOllama(model="Llama3.2")

output_parser  =StrOutputParser()

chain = prompt|llm|output_parser 

if input_text:
    st.write(chain.invoke({'question':input_text}))
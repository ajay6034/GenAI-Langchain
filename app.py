from langchain.chat_models import init_chat_model
from pydantic import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os

from dotenv import load_dotenv
load_dotenv()

# Langsmith Tracking

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]= "true"
os.environ["LANGCHAIN_API_KEY"]= os.getenv("LANGCHAIN_API_KEY")

## Prompt Template

prompt = ChatPromptTemplate.from_messages(
    [

        ("system", "you are a helpful assistant. Please respond to the user queries"),
        ("user","Question:{question}")
    ]
)

## Streamlit Framework

st.title('Langchain demo with OPENAI API')
input_text = st.text_input("search the topic you want")

# OpenAI LLM

llm = init_chat_model(model="gpt-3.5-turbo")

output_parser  =StrOutputParser()

chain = prompt|llm|output_parser 

if input_text:
    st.write(chain.invoke({'question':input_text}))
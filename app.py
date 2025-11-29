from langchain.chat_models import init_chat_model
from pydantic import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate

import streamlit as st
import os

from dotenv import load_dotenv

# Langsmith Tracking

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]= "true"
os.environ["LANGCHAIN_API_KEY"]= os.getenv("LANGCHAIN_API_KEY")

## Prompt Template

prompt = ChatPromptTemplate.from_messages(
    [

        ("system", "you are a helpful assistant. Please respond to the user queries")
        ("user","Question:{question}")
    ]
)

## Streamlit Framework

st.title('Langchain demo with OPENAI API')
input_text = st.text_input("search the topic you want")

# OpenAI LLM

llm = init_chat_model(model="gpt-3.5-turbo")

model =init_chat_model.with_structured_output(prompt)

chain = prompt|llm|model

if input_text:
    st.write(chain.invoke({'question':input_text}))
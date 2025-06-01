from dotenv import load_dotenv
from typing import Literal, Any
import os

from langchain_tavily import TavilySearch
from langchain.chat_models import init_chat_model
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq

load_dotenv()

supervisor_llm = os.getenv("SUPERVISOR_LLM")
model_provider = os.getenv("MODEL_PROVIDER")
agent_llm = os.getenv("AGENT_LLM")

def get_web_search(max_results=3):
    return TavilySearch(max_results=max_results)

def get_supervisor_llm() -> Any:
    return init_chat_model(model=supervisor_llm, model_provider=model_provider)

def get_web_search_llm(
    temperature=0.7,
    top_p=0.8
):
    return ChatGroq(
        model=agent_llm,
        temperature=temperature,
        model_kwargs={"top_p": top_p}
    )

def get_math_llm(
    temperature=0.7,
    top_p=0.8
):
    return ChatGroq(
        model=agent_llm,
        temperature=temperature,
        model_kwargs={"top_p": top_p}
    )
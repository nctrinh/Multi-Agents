from dotenv import load_dotenv
from typing import Literal, Any
from langchain_tavily import TavilySearch
from langchain.chat_models import init_chat_model
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

def get_web_search(max_results=3):
    return TavilySearch(max_results=max_results)

def get_supervisor_llm(
    model : Literal["gemini-2.0-flash", "gemini-1.5-flash"] = "gemini-2.0-flash"
) -> Any:
    return init_chat_model(model, model_provider="google_genai")

def get_web_search_llm(
    model="gemini-2.0-flash",
    temperature=0.7,
    top_p=0.8,
    top_k=40,
):
    return ChatGoogleGenerativeAI(
        model=model,
        temperature=temperature,
        top_p=top_p,
        top_k=top_k,
    )

def get_math_llm(
    model="gemini-2.0-flash",
    temperature=0.7,
    top_p=0.8,
    top_k=40,
):
    return ChatGoogleGenerativeAI(
        model=model,
        temperature=temperature,
        top_p=top_p,
        top_k=top_k,
    )
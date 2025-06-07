import os
from typing import Any

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_groq import ChatGroq
from langchain_tavily import TavilySearch

load_dotenv()

supervisor_llm = os.getenv("SUPERVISOR_LLM")
model_provider = os.getenv("MODEL_PROVIDER")
agent_llm = os.getenv("AGENT_LLM")


# Tavily Search
def get_web_search(max_results=3):
    return TavilySearch(max_results=max_results)


# Supervisor LLM
def get_supervisor_llm() -> Any:
    return init_chat_model(model=supervisor_llm, model_provider=model_provider)


# Research LLM
def get_web_search_llm(temperature: float = 0.7, top_p: float = 0.8):
    return ChatGroq(
        model=agent_llm,
        temperature=float(temperature),
        model_kwargs={"top_p": float(top_p)},
    )


# Math LLM
def get_math_llm(temperature: float = 0.7, top_p: float = 0.8):
    return ChatGroq(
        model=agent_llm,
        temperature=float(temperature),
        model_kwargs={"top_p": float(top_p)},
    )


# Cypher LLM
def get_cypher_llm(temperature: float = 0.7, top_p: float = 0.8):
    return ChatGroq(
        model=agent_llm,
        temperature=float(temperature),
        model_kwargs={"top_p": float(top_p)},
    )


def get_action_build_llm(temperature: float = 0.7, top_p: float = 0.8):
    return ChatGroq(
        model=agent_llm,
        temperature=float(temperature),
        model_kwargs={"top_p": float(top_p)},
    )

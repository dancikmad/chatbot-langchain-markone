import os

from functools import lru_cache
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()

class Settings(BaseSettings):
    env_name: str = "Local"

    openai_api: str = os.getenv("OPENAI_API_KEY")
    google_api: str = os.getenv("GOOGLE_API_KEY")
    google_cse_id: str = os.getenv("GOOGLE_CSE_ID")

    header: str = "Mark One - Interactive Chatbot with Memory and Web Search"
    template: str = """
    ### Home take assignment for Big Data Federation

    **Develop a Python script for an interactive chat using Langchain that can perform the following actions:**

    Accept questions from the user ✅

    Conduct web searches to answer questions ✅

    Keep track of conversation history, allowing for follow-up questions that retain context ✅

    Stream responses in real-time as they are generated ✅
    """


@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    print(f"--- Loading settings for: {settings.env_name}")
    return settings

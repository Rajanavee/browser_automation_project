import os
import pytest
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import SecretStr
from dotenv import load_dotenv  # Load .env file

# Load environment variables from .env
load_dotenv()


@pytest.fixture(scope="session")
def gemini_llm():
    """Fixture to initialize Google Gemini AI model for all tests."""

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        pytest.fail("❌ GEMINI_API_KEY is not set in the environment! Please check .env file.")

    return ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp", api_key=SecretStr(api_key))







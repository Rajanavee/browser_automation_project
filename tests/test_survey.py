import pytest
import os
from browser_use.agent.service import Agent
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import SecretStr

os.environ["GEMINI_API_KEY"] = "AIzaS5LpK0w"  # Replace with your actual key

@pytest.mark.asyncio
async def test_survey_navigation(browser):
    task = (
        'Open website https://qa.goeducate.com/. '
        'Login with username raj@abs.com and password Ac@123. '
        'Navigate to GOsurvey section. '
        'Validate that the survey loads successfully.'
    )

    api_key = os.getenv("GEMINI_API_KEY")
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp", api_key=SecretStr(api_key))
    agent = Agent(task, llm, use_vision=True)
    history = await agent.run()
    test_result = history.final_result()
    print("✅ Survey Test Passed:", test_result)

    assert "survey" in test_result.lower()

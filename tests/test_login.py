import pytest
import warnings
import os  # For environment variables
from browser_use.agent.service import Agent

# Suppress specific deprecation warnings
warnings.filterwarnings("ignore", category=DeprecationWarning, module="pydantic")
warnings.filterwarnings("ignore", category=DeprecationWarning, module="importlib.resources")
warnings.filterwarnings("ignore", category=UserWarning, module="langchain")


@pytest.mark.asyncio
async def test_login_automation(gemini_llm):
    """Test case to validate login automation on QA website."""

    username = os.getenv("QA_USERNAME", "raja.naveen+1@accionlabs.com")
    password = os.getenv("QA_PASSWORD", "Accion@123")

    task = (
        "Important: I am a UI Automation tester validating the tasks. "
        "Open website https://qa.goeducate.com/. "
        "Click on the Login button and enter credentials. "
        f"Enter username {username} and password {password}, then login. "
        "Select GOsurvey. "
        "After login, select the Profile Icon and Logout."
    )

    agent = Agent(task, gemini_llm, use_vision=True)
    history = await agent.run()

    # ✅ Ensure correct handling of `final_result()`
    test_result = await history.final_result() if callable(
        getattr(history.final_result, "cr_code", None)) else history.final_result()

    print("Test Result:", test_result)











































# import asyncio
# import os
# import pytest
# from browser_use.agent.service import Agent
# from langchain_google_genai import ChatGoogleGenerativeAI
# from pydantic import SecretStr
#
# @pytest.mark.asyncio
# async def test_site_validation():
#     """Pytest case for validating website automation."""
#     task = (
#         "Important: I am a UI Automation tester validating the tasks. "
#         "Open website https://qa.goeducate.com/. "
#         "Select the Login button and enter credentials. "
#         "Enter username raja.naveen+1@accionlabs.com and password Accion@123, then select the Login button. "
#         "After login, select the Profile Icon and Logout."
#     )
#
#     api_key = os.getenv("GEMINI_API_KEY")
#     if not api_key:
#         raise ValueError("GEMINI_API_KEY is not set. Please configure the environment variable.")
#
#     llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp", api_key=SecretStr(api_key))
#     agent = Agent(task, llm, use_vision=True)
#     history = await agent.run()
#     test_result = history.final_result()
#
#     print('✅ Test Passed: Login functionality Tested and completed successfully!')
#
#


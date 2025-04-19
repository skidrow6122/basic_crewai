from crewai import Agent
from langchain_openai import ChatOpenAI
from config.settings import OPENAI_API_KEY
import os

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

writer = Agent(
    role="Writer",
    goal="Create engaging content based on research. answer in Korean",
    llm=ChatOpenAI(model="gpt-4o", max_tokens=3000),
    backstory="You are a skilled writer who can transform complex information into readable content."
)

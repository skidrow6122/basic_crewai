from crewai import Agent
from langchain_openai import ChatOpenAI
from config.settings import OPENAI_API_KEY
import os

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

outline_generator = Agent(
    role="Outline Generator",
    goal="Create structured outlines for articles on given topics. answer in Korean",
    llm=ChatOpenAI(model="gpt-4o-mini", max_tokens=1000),
    backstory="You are an expert at organizing information and creating comprehensive outlines for various subjects."
)

from crewai import Agent
from langchain_openai import ChatOpenAI
from config.settings import OPENAI_API_KEY
import os

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

writer = Agent(
    role="Writer",
    goal="Create content based on the research result. answer in Korean",
    llm=ChatOpenAI(model="gpt-4o", max_tokens=3000),
    backstory="You are a skilled writer who can transform complicated information into readable content.",
    allow_delegation=False # 목표달성 실패시 다른 agent에게 위임. loop 방지를 위해 false 처리
)

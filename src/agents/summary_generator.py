from crewai import Agent
from langchain_openai import ChatOpenAI
from config.settings import OPENAI_API_KEY
import os

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

summary_generator = Agent(
    role="Summary Generator",
    goal="Create structured summary for articles on given topics. answer in Korean",
    llm=ChatOpenAI(model="gpt-4o-mini", max_tokens=1000),
    backstory="You are an expert at building information and creating comprehensive summaries and outlines for various subjects.",
    allow_delegation=False # 목표달성 실패시 다른 agent에게 위임. loop 방지를 위해 false 처리
)

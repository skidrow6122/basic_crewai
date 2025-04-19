from crewai import Agent, Task, Crew
from langchain_openai import ChatOpenAI
import os

os.environ['OPENAI_API_KEY'] = 'xxxxxxx'


# 목차 설정 에이전트
outline_generator = Agent(
    role="Outline Generator",
    goal="Create structured outlines for articles on given topics. answer in Korean",
    llm=ChatOpenAI(model= "gpt-4o-mini", max_tokens = 1000),
    backstory="You are an expert at organizing information and creating comprehensive outlines for various subjects."
)

print("SSss")
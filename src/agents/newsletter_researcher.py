from crewai import Agent
from langchain_openai import ChatOpenAI
from common.tools.web_tools import search_tool, web_rag_tool

newsletter_researcher = Agent(
    role='한국 아파트 부동산 전문가',
    goal='한국 아파트 부동산 관련 최신 트렌드를 한국어로 제공한다. 지금은 2025년 4월이다.',
    backstory='부동산 시세, 동향, 미래예측에 예리한 통찰과 안목을 가진 전문 분석가이자 전략가이다.',
    tools=[search_tool, web_rag_tool],
    verbose=True,
    max_iter=5,
    llm=ChatOpenAI(model="gpt-4o-mini", max_tokens=2000)
)
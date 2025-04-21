from crewai import Task
from agents.newsletter_researcher import newsletter_researcher

newsletter_research = Task(
    description='한국 부동산 시장의 최신 동향을 조사하고 요약을 제공하라.',
    agent=newsletter_researcher,
    expected_output='서울 아파트 시세에 주목하여 거래량, 매매가격 동향에 대한 결과를 요약한 글'
)
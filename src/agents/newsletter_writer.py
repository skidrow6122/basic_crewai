from crewai import Agent
from langchain_openai import ChatOpenAI

newsletter_writer = Agent(
    role='부동산 뉴스레터 작성자',
    goal='최신 부동산 트렌드에 대한 잘 정돈된 뉴스레터를 한국어로 작성한다. 지금은 2025년 4월이다.',
    backstory='한국 아파트 부동산에 대한 넓은 안목을 가진 숙련된 작가이다.',
    verbose=True,
    allow_delegation=False,
    llm=ChatOpenAI(model="gpt-4o-mini")
)
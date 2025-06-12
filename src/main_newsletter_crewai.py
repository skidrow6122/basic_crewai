import os
import warnings
warnings.filterwarnings("ignore")
os.environ['OPENAI_API_KEY'] = 'xxxxxxx'
os.environ['SERPER_API_KEY'] = 'xxxxxxx'  # google search API


from crewai import Agent, Task, Crew
from crewai.process import Process
from crewai_tools import (
    SerperDevTool,
    WebsiteSearchTool,
    ScrapeWebsiteTool
)
from langchain_openai import ChatOpenAI
from IPython.display import display, Markdown

search_tool = SerperDevTool() # 특정 키워드를 줬을때 해당 키워드로 구글에 검색한 결과를 가져오는 API 툴
web_rag_tool = WebsiteSearchTool() # 특정 키워드와 웹사이트를 주면 해당 웹사이트 안에서 해당 키워드와 관련된 부분만 가져오는 일종의 RAG가 내부적으로 실행되는 툴
scrap_tool = ScrapeWebsiteTool() # 어떤 url을 줬을때 해당 url에 있는 모든 텍스트를 스크래핑/크롤링 해오는 툴

## Define agents
newsletter_researcher = Agent(
    role='한국 아파트 부동산 전문가',
    goal='한국 아파트 부동산 관련 최신 트렌드를 한국어로 제공한다. 지금은 2025년 4월이다.',
    backstory='부동산 시세, 동향, 미래예측에 예리한 통찰과 안목을 가진 전문 분석가이자 전략가이다.',
    tools=[search_tool, web_rag_tool],
    verbose=True,
    max_iter=5, # 웹검색을 계속 반복하지 않고 5번으로 제한. (토큰 낭비 방지)
    llm = ChatOpenAI(model="gpt-4o-mini", max_tokens=2000)
)

newsletter_writer = Agent(
    role='부동산 뉴스레터 작성자',
    goal='최신 부동산 트렌드에 대한 잘 정돈된 뉴스레터를 한국어로 작성한다. 지금은 2025년 4월이다.',
    backstory='한국 아파트 부동산에 대한 넓은 안목을 가진 숙련된 작가이다.',
    verbose=True,
    allow_delegation=False,
    llm = ChatOpenAI(model="gpt-4o-mini")
)


## Define tasks
newsletter_research = Task(
    description='한국 부동산 시장의 최신 동향을 조사하고 요약을 제공하라.',
    agent=newsletter_researcher,
    expected_output='서울 아파트 시세에 주목하여 거래량, 매매가격 동향에 대한 결과를 요약한 글'
)

newsletter_write = Task(
    description='한국 아파트 부동산 전문가의 요약을 바탕으로 매력적인 뉴스레터를 작성하라.',
    agent=newsletter_writer,
    expected_output='재미있는 말투로 소개하는 5문단 짜리 마크다운 형식의 뉴스레터',
    output_file='/src/common/data/output/newsletter_latest.md'
)


## Assemble a crew with planning enabled
newsletter_crew = Crew(
    agents=[newsletter_researcher, newsletter_writer],
    tasks=[newsletter_research, newsletter_write],
    verbose=True,
    process=Process.sequential
)

# Execute tasks
result = newsletter_crew.kickoff()
display(Markdown(result.raw))

from crewai import Agent, Task, Crew
from langchain_openai import ChatOpenAI
from crewai.process import Process
from IPython.display import display, Markdown
import os


print("### Crew ai configuration ###")

os.environ['OPENAI_API_KEY'] = 'xxxxxxx'

## Agent 정의
# 목차 설정 에이전트
outline_generator = Agent(
    role="Outline Generator",
    goal="Create structured outlines for articles on given topics. answer in Korean",
    llm=ChatOpenAI(model= "gpt-4o-mini", max_tokens = 1000),
    backstory="You are an expert at organizing information and creating comprehensive outlines for various subjects."
)

# 본문 작성 에이전트
writer = Agent(
    role="Writer",
    goal="Create engaging content based on research. answer in Korean",
    llm=ChatOpenAI(model= "gpt-4o", max_tokens = 3000),
    backstory="You are an skilled writer who can transform complex information into readable content."
)

## Task 정의
outline_task = Task(
    description="Create a detailed outline for an article about AI\`s impact on job markets",
    agent=outline_generator,
    expected_output="A comprehensive outline covering the main aspects of AI\`s influence on employment"
)

writing_task = Task(
    description="Write an article about the findings from the research",
    agent=writer,
    expected_output="An engaging article article discussing AI\'s influence on job markets"
)

## Crew & Process 정의
# Process 정의하지 않으면 agent들이 알아서 주어진 태스크를 수행하고 작업흐름도 자동으로 진행됨, 직접 정의시 주어진 작업흐름에 알맞게 agent와 task 가 할당되어 수행
ai_impact_crew = Crew(
    agents=[outline_generator, writer],
    tasks=[outline_task, writing_task],
    verbose=True, # 중간 실행결과 로깅 출력
    Process=Process.sequential
)

print("### task kickoff ###")
## Crew 실행
result = ai_impact_crew.kickoff()
display(Markdown(result.raw))

print("### task terminated ###")
from crewai import Crew
from crewai.process import Process
from tasks.outline_task import outline_task
from tasks.writing_task import writing_task
from agents.outline_generator import outline_generator
from agents.writer import writer

ai_impact_crew = Crew(
    agents=[outline_generator, writer],
    tasks=[outline_task, writing_task],
    verbose=True,
    process=Process.sequential
)

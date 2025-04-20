from crewai import Crew
from crewai.process import Process
from tasks.summary_task import summary_task
from tasks.writing_task import writing_task
from agents.summary_generator import summary_generator
from agents.writer import writer

report_crew = Crew(
    agents=[summary_generator, writer],
    tasks=[summary_task, writing_task],
    verbose=True,
    process=Process.sequential
)

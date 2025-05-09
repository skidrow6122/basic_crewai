from crewai import Task
from agents.writer import writer

writing_task = Task(
    description="Write an article about the findings from the research result",
    agent=writer,
    expected_output="An engaging article discussing the history of computer science",
)

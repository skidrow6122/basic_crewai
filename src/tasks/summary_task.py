from crewai import Task
from agents.summary_generator import summary_generator

summary_task = Task(
    description="Create a detailed outline for an article about the history of computer science",
    agent=summary_generator,
    expected_output="A comprehensive summary containing the history of computer science",
)

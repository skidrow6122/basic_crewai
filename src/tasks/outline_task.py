from crewai import Task
from agents.outline_generator import outline_generator

outline_task = Task(
    description="Create a detailed outline for an article about AI's impact on job markets",
    agent=outline_generator,
    expected_output="A comprehensive outline covering the main aspects of AI's influence on employment"
)

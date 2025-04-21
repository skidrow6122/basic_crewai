from crewai import Crew
from crewai.process import Process
from agents.newsletter_researcher import newsletter_researcher
from agents.newsletter_writer import newsletter_writer
from tasks.newsletter_research_task import newsletter_research
from tasks.newsletter_write_task import newsletter_write

newsletter_crew = Crew(
    agents=[newsletter_researcher, newsletter_writer],
    tasks=[newsletter_research, newsletter_write],
    verbose=True,
    process=Process.sequential
)

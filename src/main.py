from crews.ai_impact_crew import ai_impact_crew
from IPython.display import display, Markdown

if __name__ == "__main__":
    print("### Crew kickoff ###")
    result = ai_impact_crew.kickoff()
    display(Markdown(result.raw))
    print("### Task completed ###")
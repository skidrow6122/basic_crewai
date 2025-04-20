from crews.report_crew import report_crew
from IPython.display import display, Markdown

if __name__ == "__main__":
    print("### Crew kickoff ###")
    result = report_crew.kickoff()
    display(Markdown(result.raw))
    print("### Task completed ###")
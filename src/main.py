import os
from common.config.settings import OPENAI_API_KEY, SERPER_API_KEY
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
os.environ["SERPER_API_KEY"] = SERPER_API_KEY

from crews.report_crew import report_crew
from crews.newsletter_crew import newsletter_crew
from IPython.display import display, Markdown



if __name__ == "__main__":
    # print("### simple Crew kickoff ###")
    # result = report_crew.kickoff()
    # display(Markdown(result.raw))
    # print("### simple Crew Task completed ###")

    print("### newsletter Crew kickoff ###")
    result = newsletter_crew.kickoff()
    display(Markdown(result.raw))
    print("### newsletter Crew Task completed ###")
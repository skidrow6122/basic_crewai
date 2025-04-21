from crewai import Task
from agents.newsletter_writer import newsletter_writer

newsletter_write = Task(
    description='한국 아파트 부동산 전문가의 요약을 바탕으로 매력적인 뉴스레터를 작성하라.',
    agent=newsletter_writer,
    expected_output='재미있는 말투로 소개하는 5문단짜리 마크다운 뉴스레터',
    output_file='data/output/newsletter_latest.md'
)
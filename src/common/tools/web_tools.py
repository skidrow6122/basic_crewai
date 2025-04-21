from crewai_tools import (
    SerperDevTool,
    WebsiteSearchTool,
    ScrapeWebsiteTool
)

search_tool = SerperDevTool() # 특정 키워드를 줬을때 해당 키워드로 구글에 검색한 결과를 가져오는 API 툴
web_rag_tool = WebsiteSearchTool() # 특정 키워드와 웹사이트를 주면 해당 웹사이트 안에서 해당 키워드와 관련된 부분만 가져오는 일종의 RAG가 내부적으로 실행되는 툴
scrap_tool = ScrapeWebsiteTool() # 어떤 url을 줬을때 해당 url에 있는 모든 텍스트를 스크래핑/크롤링 해오는 툴

__all__ = ['search_tool', 'web_rag_tool', 'scrap_tool']
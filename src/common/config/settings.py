import os
import warnings
warnings.filterwarnings('ignore')

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "xxxxxxx")
SERPER_API_KEY = os.getenv("SERPER_API_KEY", "xxxxxxx") # 구글 웹검색 결과를 제공하는 google search API
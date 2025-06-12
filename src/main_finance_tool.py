import os
import warnings
warnings.filterwarnings("ignore")

from crewai.tools import tool # 커스텀 툴을 만들때 함수 위에다 데코레이터로 tool 만 명시해주면, crew ai의 agent 가 할용할 수 있는 도구로 wrapping 됨
import yfinance as yf
from datetime import datetime, timedelta
import pandas as pd  # yfinance 로 재무제표를 가져올때 데이터프레임 형태로 yfinance 가 응답하기때문에 받아주기 위한 포맷
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)


ticker = yf.Ticker("TSLA") # ticker 메서드를 통해 원하는 기업을 지정. 이 ticker 안에는 재무정보를 가져오는 다양한 함수를 제공함
# help(ticker)

# 총 5일치 일간 주가정보 조회
df_stock = ticker.history(period="5d", interval="1d") # 총 5일치 정보를 가져옴
print(df_stock)

# 재무제표 정보 조회
df_annual_finance = ticker.get_financials() # 전체
df_annual_finance_balance_sheet = ticker.get_balance_sheet()
df_annual_finance_income_statement = ticker.get_income_stmt()
df_quarter_finance = ticker.get_financials(freq="quarterly") # 분기별 정보
print(df_quarter_finance)

# 주식 종가를 불러오는 tool 정의
@tool # 이 데코레이터 밑으로 있는 함수에 대해서는 agent 가 활용할 수 있는 커스텀 tool로 등록 됨
def latest_stock_price(ticker):
    """ 
    주어진 주식 티커에 대한 최근 종가를 가져오는 툴 
    """ # doc string 으로 반드시 기입해주어야 agent가 해당 툴이 어떤 툴인지 인지할 수 있어서 이 툴을 쓸지말지를 판단할 수 있음
    ticker = yf.Ticker(ticker)
    historical_prices = ticker.history(period="5d", interval="1d")
    latest_price = historical_prices['Close']
    return latest_price

print(latest_stock_price.run("META"))

# 재무 제표를 불러오는 tool 정의
@tool
def financial_anaysis(ticker):
    """
    연간 재무제표의 주요 정보를 가져오는 툴
    """
    ticker = yf.Ticker(ticker)
    annual_financials = ticker.get_financials()
    summary = {} # 서머리 딕셔너리
    for date, data in annual_financials.items():
        date_str = date.strftime("%Y-%m-%d")
        summary[date_str] = {
            "총수익" : data.get('TotalRevenue'),
            "영업이익" : data.get('OperatingIncome'),
            "순이익" : data.get('NetIncome'),
            "EBITDA" : data.get('EBITDA')
        }
    return summary

print(financial_anaysis.run("AAPL"))

# 종합적인 주식분석 tool 정의
@tool ("Updated Comprehensive Stock Analysis") # 커스텀 tool 명칭 정의
def comprehensive_stock_analysis(ticker):
    """
    주어진 주식 티커에 대한 업데이트된 종합적인 재무 분석을 수행합니다.
    최신 주가 정보, 재무 지표, 성장률, 밸류에이션 및 주요 비율을 제공합니다.
    가장 최근 영업일 기준의 데이터를 사용합니다.

    :param ticker: 분석할 주식의 티커 심볼
    :return: 재무 분석 결과를 포함한 문자열
    """
    def format_number(number):
        if number is None or pd.isna(number):
            return "N/A"
        return f"{number:,.0f}" # 천단위 콤마 + 소수점 뒷자리 무시

    def calculate_growth_rate(current, previous): # 성장률 계산 함수
        if previous and current and previous != 0:
            return (current - previous) / abs(previous) * 100
        return None

    def format_financial_summary(financials) :
        summary = {}
        for date, data in annual_financials.items():
            date_str = date.strftime("%Y-%m-%d")
            summary[date_str] = {
                "총수익": data.get('TotalRevenue'),
                "영업이익": data.get('OperatingIncome'),
                "순이익": data.get('NetIncome'),
                "EBITDA": data.get('EBITDA')
            }
        return summary

    ticker = yf.Ticker(ticker)
    historical_prices = ticker.history(period="1d", interval="1m")
    latest_price = historical_prices['Close']
    latest_time = historical_prices.index[-1].strftime("%Y-%m-%d %H:%M:%S")

    # 연간, 분기별 재무제표 데이터 불러오기
    annual_financials = ticker.get_financials()
    quarter_financials = ticker.get_financials(freq="quarterly")

    # 주요 재무지표 (연간) - 불러온 재무제표 결과를 인덱싱
    revenue = annual_financials.loc["TotalRevenue", annual_financials.columns[0]] # 첫번째 컬럼값이 가장 최근정보이므로
    cost_of_revenue = annual_financials.loc["CostOfRevenue", annual_financials.columns[0]]
    gross_profit = annual_financials.loc["GrossProfit", annual_financials.columns[0]]
    operating_income = annual_financials.loc["OperatingIncome", annual_financials.columns[0]]
    net_income = annual_financials.loc["NetIncome", annual_financials.columns[0]]
    ebitda = annual_financials.loc["EBITDA", annual_financials.columns[0]]

    # 주요 비율 계산
    gross_margin = (gross_profit / revenue) * 100 if revenue != 0 else None
    operating_margin = (operating_income / revenue) * 100 if net_income != 0 else None
    net_margin = (net_income / revenue) * 100 if revenue != 0 else None

    # 성장률 지표 계산 (연간)
    revenue_growth = calculate_growth_rate(revenue, annual_financials.loc["TotalRevenue", annual_financials.columns[1]])
    net_income_growth = calculate_growth_rate(net_income, annual_financials.loc["NetIncome", annual_financials.columns[1]])

    # 분기별 데이터 분석
    quarterly_revenue = quarter_financials.loc['TotalRevenue', quarter_financials.columns[0]]
    quarterly_net_income = quarter_financials.loc['NetIncome', quarter_financials.columns[0]]
    quarterly_revenue_growth = calculate_growth_rate(
        quarterly_revenue,
        quarter_financials.loc['TotalRevenue', quarter_financials.columns[1]]
    )
    quarterly_net_income_growth = calculate_growth_rate(
        quarterly_net_income,
        quarter_financials.loc['NetIncome', quarter_financials.columns[1]]
    )

    return {
        "현재 주가": {
            "현재 주가": latest_price,
            "기준 시간": latest_time
        },
        "연간 데이터": {
            "매출": format_number(revenue),
            "매출원가": format_number(cost_of_revenue),
            "매출총이익": format_number(gross_profit),
            "영업이익": format_number(operating_income),
            "순이익": format_number(net_income),
            "EBITDA": format_number(ebitda),
            "매출총이익률": f"{gross_margin:.2f}%" if gross_margin is not None else "N/A",
            "영업이익률": f"{operating_margin:.2f}%" if operating_margin is not None else "N/A",
            "순이익률": f"{net_margin:.2f}%" if net_margin is not None else "N/A",
            "매출 성장률": f"{revenue_growth:.2f}%" if revenue_growth is not None else "N/A",
            "순이익 성장률": f"{net_income_growth:.2f}%" if net_income_growth is not None else "N/A",
        },
        "분기 데이터": {
            "매출": format_number(quarterly_revenue),
            "순이익": format_number(quarterly_net_income),
            "매출 성장률(QoQ)": f"{quarterly_revenue_growth:.2f}%" if quarterly_revenue_growth is not None else "N/A",
            "순이익 성장률(QoQ)": f"{quarterly_net_income_growth:.2f}%" if quarterly_net_income_growth is not None else "N/A",
        },
        "연간 재무제표 요약": format_financial_summary(annual_financials),
        "분기별 재무제표 요약": format_financial_summary(quarter_financials),
    }

print(comprehensive_stock_analysis.run("AAPL"))





import yfinance as yf
import numpy as np
ticker = "TATAMOTORS.NS"  
data = yf.download(ticker, start="2023-04-01", end="2024-04-1", progress=False)
data['Daily Return'] = data['Adj Close'].pct_change()
risk_free_rate_annual = 0.07015  
risk_free_rate_daily = risk_free_rate_annual / 248  
data['Excess Return'] = data['Daily Return'] - risk_free_rate_daily
average_excess_return = data['Excess Return'].mean()
volatility = data['Daily Return'].std()
sharpe_ratio = average_excess_return / volatility
print(f"Sharpe Ratio of Tata Motors: {sharpe_ratio:.2f}")

import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
market_symbol = "^NSEI"  
stock_symbol = "TATAMOTORS.NS" 
start_date = "2023-04-01"
end_date = "2024-04-01"
market_data = yf.download(market_symbol, start=start_date, end=end_date)
stock_data = yf.download(stock_symbol, start=start_date, end=end_date)
stock_data['Return'] = stock_data['Adj Close'].pct_change()
market_data['Return'] = market_data['Adj Close'].pct_change()
returns = pd.DataFrame({
    'Stock': stock_data['Return'],
    'Market': market_data['Return']
}).dropna()
X = returns['Market'].values.reshape(-1, 1)  
y = returns['Stock'].values.reshape(-1, 1) 
reg = LinearRegression()
reg.fit(X, y)
beta = reg.coef_[0][0]
alpha = reg.intercept_[0]
print(f"Alpha: {alpha}")
print(f"Beta: {beta}")
plt.scatter(returns['Market'], returns['Stock'], alpha=0.5, label='Data points')
plt.plot(returns['Market'], reg.predict(X), color='red', label='Regression line')
plt.xlabel('Market Return')
plt.ylabel('Stock Return')
plt.title(f'{stock_symbol} vs {market_symbol}')
plt.legend()
plt.show()

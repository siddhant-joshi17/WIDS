import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)
time_steps = 100 
stock_prices = 100 + np.cumsum(np.random.randn(time_steps)) 
strike_price = 100 
option_premium = 5 

call_prices = np.maximum(stock_prices - strike_price, 0)
put_prices = np.maximum(strike_price - stock_prices, 0)
portfolio_values = []
for i in range(time_steps):
    pnl = (option_premium * 2) - (call_prices[i] + put_prices[i])
    portfolio_values.append(pnl)
df = pd.DataFrame({
    'Time': np.arange(time_steps),
    'StockPrice': stock_prices,
    'CallPrice': call_prices,
    'PutPrice': put_prices,
    'PortfolioValue': portfolio_values
})
plt.figure(figsize=(10, 5))
plt.plot(df['Time'], df['PortfolioValue'], label="Portfolio Value", color='blue')
plt.axhline(0, color='black', linestyle='--', linewidth=1)  
plt.xlabel("Time Steps")
plt.ylabel("Portfolio Value")
plt.title("Short Straddle Strategy Performance")
plt.legend()
plt.grid()

net_pnl = portfolio_values[-1]  
max_drawdown = min(portfolio_values)
print(f"Net PnL: {net_pnl:.2f}")
print(f"Max Drawdown: {max_drawdown:.2f}")

plt.show()

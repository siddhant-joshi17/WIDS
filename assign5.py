
import numpy as np
from scipy.stats import norm
import pandas as pd

class BlackScholesModel:
    def __init__(self, spot_price, strike_price, time_to_expiry, risk_free_rate, volatility):
        """
        Initialize the Black-Scholes model with given parameters.
        """
        self.S = spot_price  
        self.K = strike_price  
        self.T = time_to_expiry 
        self.r = risk_free_rate  
        self.sigma = volatility  
    def d1(self):
        """
        Calculate d1 in the Black-Scholes formula.
        """
        return (np.log(self.S / self.K) + (self.r + 0.5 * self.sigma ** 2) * self.T) / (self.sigma * np.sqrt(self.T))
    
    def d2(self):
        """
        Calculate d2 in the Black-Scholes formula.
        """
        return self.d1() - self.sigma * np.sqrt(self.T)
    
    def call_price(self):
        """
        Calculate the call option price using the Black-Scholes formula.
        """
        d1 = self.d1()
        d2 = self.d2()
        return self.S * norm.cdf(d1) - self.K * np.exp(-self.r * self.T) * norm.cdf(d2)
    
    def put_price(self):
        """
        Calculate the put option price using the Black-Scholes formula.
        """
        d1 = self.d1()
        d2 = self.d2()
        return self.K * np.exp(-self.r * self.T) * norm.cdf(-d2) - self.S * norm.cdf(-d1)
r = 0.07  
sigma = 0.15  
expiry_date = pd.Timestamp("2023-02-23")
current_date = pd.Timestamp("2023-02-01")
T = (expiry_date - current_date).days / 365.0
spot_price_data_path = "NIFTY50_1min_01FEB.csv"
spot_prices = pd.read_csv(spot_price_data_path)
strike_price = 100
spot_price = spot_prices['Close'].iloc[0]  

bs_model = BlackScholesModel(spot_price, strike_price, T, r, sigma)
call_price = bs_model.call_price()
put_price = bs_model.put_price()

print(f"Call Price: {call_price:.2f}")
print(f"Put Price: {put_price:.2f}")

 

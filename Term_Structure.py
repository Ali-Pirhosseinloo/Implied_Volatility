import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from Financial_Data import FinancialData as fd
from Implied_Volatility import Implied_Volatility as iv


# Assuming you have the following functions and data


ticker = ''
ticker = input(f"Please enter the ticker: {ticker}")

stock = fd(ticker)
expiration_dates = stock.get_stock_dates()
S = stock.get_spot_price()  # current stock price
r = stock.get_risk_free_rate()  # risk-free rate

K_vals = []
T_vals = []
vol_vals = []

for TtMaturity in expiration_dates:
    T = np.float32([(pd.to_datetime(TtMaturity) - pd.Timestamp.now()).days / 365.0])
    T = T[0]
    if T <= 0:
        continue 
    calls = stock.get_option_data(TtMaturity)
    K_range = calls['strike'].values
    for j in range(10,len(K_range)-10):
        market_prices = 0.5 * (calls['bid'].values[j] + calls['ask'].values[j])
        if market_prices < S - np.exp(-r * T) * K_range[j]:
            continue
        vol = iv(S, K_range[j], r, T, market_prices).Call_IV()
        if vol < 0.01:
            continue
        T_vals.append(T)
        K_vals.append(K_range[j])
        vol_vals.append(vol)

# Convert lists to numpy arrays for easier manipulation
K_vals = np.array(K_vals)
T_vals = np.array(T_vals)
vol_vals = np.array(vol_vals)

# Plot the term structure for a specific strike price
# Assuming you want to plot the term structure for the strike price closest to the current stock price
unique_strikes = np.unique(K_vals)
for strike in unique_strikes:
    mask = K_vals == strike
    plt.plot(T_vals[mask], vol_vals[mask])
    

plt.xlabel('Time to Expiration (Years)')
plt.ylabel('Implied Volatility')
plt.title('Term Structure of Implied Volatility')
plt.legend()
plt.show()
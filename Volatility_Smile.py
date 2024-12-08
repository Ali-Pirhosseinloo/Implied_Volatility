import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from Implied_Volatility import Implied_Volatility as iv
from Financial_Data import FinancialData as fd


ticker = ''
ticker = input(f"Please enter the ticker: {ticker}")

stock = fd(ticker)
expiration_dates = stock.get_stock_dates()
S = stock.get_spot_price()  # current stock price
r = stock.get_risk_free_rate()  # risk-free rate

K_vals = []
T_vals = []
vol_vals = []

for TtMaturity in expiration_dates[:8]:
    T = np.float32([(pd.to_datetime(TtMaturity) - pd.Timestamp.now()).days / 365.0])
    T = T[0]
    if T <= 0:
        continue 
    calls = stock.get_option_data(TtMaturity)
    K_range = calls['strike'].values
    for j in range(len(K_range)):
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

# Plot the volatility smile for a specific maturity
# Assuming you want to plot the smile for the first maturity in the list
unique_maturities = np.unique(T_vals)
for maturity in unique_maturities:
    mask = T_vals == maturity
    plt.plot(K_vals[mask], vol_vals[mask], label=f'T={maturity:.2f}')

plt.xlabel('Strike Price')
plt.ylabel('Implied Volatility')
plt.title('Volatility Smile')
plt.legend()
plt.show()
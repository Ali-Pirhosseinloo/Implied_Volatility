import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from Financial_Data import FinancialData as fd
from Implied_Volatility import Implied_Volatility as iv
from scipy.interpolate import SmoothBivariateSpline

ticker = ''
ticker = input(f"Please enter the ticker: {ticker}")

stock = fd(ticker) 
expiration_dates = stock.get_stock_dates()
S = stock.get_spot_price()  # current stock price
r = stock.get_risk_free_rate()  # risk-free rate

T_vals = [] # time to maturity
K_vals = [] # strike price
vol_vals = [] # implied volatility

for TtMaturity in expiration_dates:

    T = np.float32([(pd.to_datetime(TtMaturity) - pd.Timestamp.now()).days / 365.0]) 
    T = T[0] # time to maturity in years
    if T <= 0: # if the maturity date has passed, skip
        continue 

    calls = stock.get_option_data(TtMaturity)
    K_range = calls['strike'].values # strike prices

    for j in range(len(K_range)):
 
        market_prices = 0.5 * (calls['bid'].values[j] + calls['ask'].values[j]) # average of bid and ask prices

        if  market_prices < S - np.exp(-r * T) * K_range[j] : 
            continue        # if the market price is less than the
                            # minimum possible estimated by BSM) then skip

        vol = iv(S, K_range[j], r, T, market_prices).Call_IV() # implied volatility

        if vol < 0.01: # if the implied volatility is too small, skip
            continue

        T_vals.append(T) 
        K_vals.append(K_range[j])
        vol_vals.append(vol)
    


# Create the surface plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


# Add axis labels
ax.set_xlabel('Time to Expiration')
ax.set_ylabel('Strike Price')
ax.set_zlabel('Implied Volatility')


# Add scatter plot
ax.scatter(T_vals, K_vals, vol_vals, color='b')
ax.set_zlim(0, 2)
plt.show()


# Convert lists to numpy arrays
K_vals = np.array(K_vals)
T_vals = np.array(T_vals)
vol_vals = np.array(vol_vals)

# Create a mesh grid for strike prices and maturities
K_grid, T_grid = np.meshgrid(np.linspace(K_vals.min(), K_vals.max(), 100), 
                             np.linspace(T_vals.min(), T_vals.max(), 100))

# Interpolate volatilities on the grid using spline interpolation
spline = SmoothBivariateSpline(K_vals, T_vals, vol_vals, s=15)
vol_grid = spline.ev(K_grid.ravel(), T_grid.ravel()).reshape(T_grid.shape)


# Create the surface plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Add axis labels
ax.set_ylabel('Strike Price')
ax.set_xlabel('Time to Expiration')
ax.set_zlabel('Implied Volatility')

# Plot the surface
surf = ax.plot_surface(T_grid, K_grid, vol_grid, cmap='viridis')
plt.title('Volatility Surface') 
plt.colorbar(surf) 
plt.show()
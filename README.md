# Implied Volatility Analysis and Modeling

## Overview  

This project is a Python-based toolkit for analyzing and modeling implied volatility, a key metric in options trading that reflects the market's expectation of future price volatility of an underlying asset. Implied volatility is derived from options prices using mathematical models and is widely used for pricing, risk management, and strategy development.

The project  visualizes:  
- **Volatility Surface**: A 3D representation of implied volatility across different strike prices and maturities, providing a comprehensive view of market expectations.  
- **Volatility Smile**: A curve showing how implied volatility varies with strike prices for a given maturity, often forming a "smile" shape.  
- **Term Structure**: A graph showing the relationship between implied volatility and time to expiration for a specific strike price, offering insights into time-based market sentiment.  


## Features  
- **Implied Volatility Calculation**: Compute implied volatility for call and put options using the Newton-Raphson method.  
- **Real-Time Data Integration**: Fetches financial data (spot price, option price, strike price, maturity) from [yfinance](https://github.com/ranaroussi/yfinance) and U.S. Treasury websites.  
- **Volatility Surface Visualization**: Generates volatility surface graphs using bivariate splines and scatter plots based on user-specified tickers.
- **Volatility Smile and Term Structure**: Creates detailed graphs for volatility smiles and term structures based on user-specified tickers.


Examples
--------

### 1\. Volatility Surface Visualization

Run the `volatility_surface.py` module to visualize the volatility surface for a given ticker, such as **AAPL** (Apple Inc.). The module fetches real-time financial data and generates a 3D plot of implied volatility across different strike prices and maturities.



-------------------------------------------------------------------------

### Example 2: Volatility Smile Visualization  
Run the `volatility_smile.py` module to visualize the volatility smile for a given ticker, such as **AAPL** (Apple Inc.). This module fetches real-time financial data and generates a plot showing how implied volatility varies with strike prices for a specific maturity.

-------------------------------------------------------------------------

### Example 3: Term Structure Visualization  
Run the `Term_Strucutre.py` module to visualize the term structure for a given ticker, such as **AAPL** (Apple Inc.). This module fetches real-time financial data and generates a plot showing how implied volatility varies with strike prices for a specific maturity.


## Project Structure  
```plaintext
├── Implied_Volatility.py   # Module for implied volatility calculations
├── Options.py              # Module for option pricing with Black Scholes
├── financial_data.py       # Module to fetch real-time data from yfinance and U.S. Treasury
├── volatility_surface.py   # Generates volatility surface graphs
├── volatility_smile.py     # Graphs volatility smile and term structure
├── requirements.txt        # List of required Python libraries
└── README.md               # Project documentation
```

## Prerequisites
*   Python 3.8+
* `numpy`, `pandas` , `yfinance`,  `matplotlib`, `scipy`, `bs4` , `requests`

Install dependencies with:

```
pip install -r requirements.txt
```

## Usage

1.  **Clone the Repository**
    ```
    git clone https://github.com/Ali-Pirhosseinloo/Implied_Volatility.git
    cd Implied_Volatility
    ```
    
    
2.  **Implied Volatility Calculation**  
    Compute implied volatility for specific options:
    ```
    python Implied_Volatility.py
    ```
    
3.  **Generate Volatility Surface**  
    Visualize the surface for a given ticker:
    ```
    python Volatility_Surface.py
    ```
    
4.  **Graph Volatility Smile or Term Structure**  
    Produce smile or term structure graphs:
    ```
    python Volatility_Smile.py
    ```

4.  **Graph Term Structure**  
    Produce smile or term structure graphs:
    ```
    python Term_Structure.py
    ```

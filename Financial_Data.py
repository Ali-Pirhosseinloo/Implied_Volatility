import yfinance as yf
import requests
from bs4 import BeautifulSoup

class FinancialData:
    def __init__(self, ticker):
        self.ticker = ticker
        self.stock = yf.Ticker(ticker)

    def get_risk_free_rate(self): # get the 1-year Treasury yield
        url = 'https://home.treasury.gov'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        data_1yr = soup.find('span', id='data-1yr')
        if data_1yr:
            return float(data_1yr.text) / 100.0
        else:
            raise ValueError("1-year Treasury yield not found")

    def get_option_data(self, expiration_date):
        option_chain = self.stock.option_chain(expiration_date)
        calls = option_chain.calls  # get the calls
        return calls

    def get_stock_dates(self):
        return self.stock.options # return the expiration dates

    def get_spot_price(self):
        return self.stock.history(period='1d')['Close'].iloc[0] # return the spot price

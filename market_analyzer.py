import yfinance as yf
import pandas as pd
import numpy as np

def analyze_stock(ticker):
    # Fetching real-time market data
    data = yf.download(ticker, period="1y")
    
    # Moving Average Crossover Signal (HFT Logic)
    data['SMA_20'] = data['Close'].rolling(window=20).mean()
    data['SMA_50'] = data['Close'].rolling(window=50).mean()
    
    # Vectorized Volatility Calculation (NumPy Optimization)
    returns = np.log(data['Close'] / data['Close'].shift(1))
    volatility = returns.std() * np.sqrt(252)
    
    print(f"Analysis for {ticker}:")
    print(f"Annualized Volatility: {volatility:.2%}")
    return data

if __name__ == "__main__":
    analyze_stock("AAPL")

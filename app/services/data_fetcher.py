import yfinance as yf
from datetime import datetime, timedelta

def get_stock_data(symbol, days=60):
    end = datetime.today()
    start = end - timedelta(days=days)
    df = yf.download(f"{symbol}.NS", start=start, end=end)
    return df
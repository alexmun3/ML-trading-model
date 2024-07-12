import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import pandas as pd

ticker = "AAPL"
start_date = "2022-12-01"
end_date = "2022-12-30"

def create_chart(ticker, start_date, end_date, interval):
    data = yf.download(ticker, start=start_date, end=end_date, interval=interval)
    

plt.figure(figsize=(12, 6))
plt.plot(data.index, data['Adj Close'])
plt.title(f"{ticker} Stock Price")
plt.xlabel("Date")
plt.ylabel("Adjusted Close Price")
plt.grid(True)

plt.savefig(f"{ticker}_stock_price.png")
plt.close()

end_date = datetime.now()
intervals = [
    ("1d", end_date - timedelta(days=30)),from datetime import datetime, timedelta
]

for interval, start_date in intervals:
    create_chart(ticker, start_date, end_date, interval)

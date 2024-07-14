#import relevant servers and as what
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from datetime import datetime, timedelta

#define our ticker and data(pulled from yfinance)
ticker = "CL=F"
data = yf.download(ticker, start="2020-01-01", end="2020-12-31")

#define start dates
start_date = datetime(2020, 1, 1)
end_date = datetime(2020, 12, 31)
delta = timedelta(days=7)  #this defines the time period for each photo (7 days/1 week)


while start_date <= end_date:
    end_of_period = min(start_date + delta - timedelta(days=1), end_date)
    
    #this code uses matplotlib to plot the chart and add design (grid and tittles)
    plt.figure(figsize=(12, 6))
    plt.plot(data.loc[start_date:end_of_period].index, data.loc[start_date:end_of_period]["Adj Close"])
    #plt.title(f"{start_date.strftime('%b %d')} - {end_of_period.strftime('%b %d')} 2022 Daily Chart")
    #plt.xlabel("Date")
    #plt.ylabel("Adjusted Close Price")
    plt.grid(False)
    
    #this tells it where/how to save message
    filename = f"{start_date.strftime('%Y%m%d')}-{end_of_period.strftime('%Y%m%d')} Daily Chart.png"
    plt.savefig(filename)
    plt.close()
    print(f"Saved chart: {filename}")
    
    start_date += delta
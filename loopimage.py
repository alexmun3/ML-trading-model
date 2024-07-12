import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

ticker = "AAPL"
data = yf.download(ticker, start="2022-01-01", end="2022-12-31")


df = pd.read_csv('AAPLdata.csv')

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

for i, month in enumerate(months):
   
    month_data = data[(data["Date"].dt.month == i + 1) & (data["Date"].dt.year == 2022)]
    
    plt.figure(figsize=(12, 6))
    plt.plot(month_data["Date"], month_data["Value"])
    plt.title(f"{month} 2022 Daily Chart")
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.grid(True)
    

    filename = f"{month} 2022 Daily Chart.png"
    plt.savefig(filename)
    plt.close()
    print(f"Saved chart: {filename}")
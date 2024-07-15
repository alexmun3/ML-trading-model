import os
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime, timedelta

# Function to determine if a week is bullish, bearish, or consolidated
def classify_week(week_data):
    start_price = week_data.iloc[0]['Adj Close']
    end_price = week_data.iloc[-1]['Adj Close']
    if end_price > start_price * 1.02:
        return 'bullish'
    elif end_price < start_price * 0.98:
        return 'bearish'
    else:
        return 'consolidated'

# Function to plot and save the weekly data
def plot_and_save(week_data, week_start, week_end, classification):
    plt.figure(figsize=(1.5, 0.75))
    plt.plot(week_data['Date'], week_data['Adj Close'], marker='', linestyle='-')
    #plt.title(f'Crude Oil Prices: {week_start.strftime("%Y-%m-%d")} to {week_end.strftime("%Y-%m-%d")} ({classification})')
    #plt.xlabel('Date')
    #plt.ylabel('Adjusted Close Price')
    plt.grid(False)
    filename = f"{week_start.strftime('%Y%m%d')}_{week_end.strftime('%Y%m%d')}_{classification}.png"
    plt.savefig(filename)
    plt.close()
    print(f"Saved chart as {filename}")
    plt.tick_params(axis='both', which='both', bottom=False, top=False, left=False, right=False,
                    labelbottom=False, labelleft=False)

    plt.xticks([])
    plt.yticks([])

# Download data from Yahoo Finance
ticker = "CL=F"
data = yf.download(ticker, start="2010-01-01", end="2019-12-31")

# Add a Date column for easier handling
data.reset_index(inplace=True)

# Process data week by week
start_date = data['Date'].min()
end_date = data['Date'].max()
current_date = start_date

while current_date <= end_date:
    week_end_date = current_date + timedelta(days=6)
    week_data = data[(data['Date'] >= current_date) & (data['Date'] <= week_end_date)]
    if not week_data.empty:
        classification = classify_week(week_data)
        plot_and_save(week_data, current_date, week_end_date, classification)
    current_date += timedelta(days=7)

print("Process complete.")

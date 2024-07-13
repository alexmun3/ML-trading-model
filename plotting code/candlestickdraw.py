import yfinance as yf
import matplotlib.pyplot as plt  # This line imports pyplot and assigns it to plt
import seaborn as sns
import plotly.graph_objects as go

# Set the ticker and date range
ticker = "AAPL"
start_date = "2023-01-01"
end_date = "2023-12-31"

# Download the data
data = yf.download(ticker, start=start_date, end=end_date)

# Create the plot using matplotlib
plt.figure(figsize=(12, 6))
plt.plot(data.index, data['Adj Close'])
plt.title(f"{ticker} Stock Price")
plt.xlabel("Date")
plt.ylabel("Adjusted Close Price")
plt.grid(True)

# Save the image
plt.savefig(f"{ticker}_stock_price.png")
plt.close()

# Seaborn example
sns.set(style="darkgrid")
plt.figure(figsize=(12, 6))
sns.lineplot(x=data.index, y=data['Adj Close'])
plt.title(f"{ticker} Stock Price")
plt.xlabel("Date")
plt.ylabel("Adjusted Close Price")
plt.savefig(f"{ticker}_stock_price_seaborn.png")
plt.close()

# Plotly example
fig = go.Figure(data=[go.Candlestick(x=data.index,
                open=data['Open'],
                high=data['High'],
                low=data['Low'],
                close=data['Close'])])
fig.update_layout(title=f"{ticker} Stock Price", xaxis_title="Date", yaxis_title="Price")
fig.write_image(f"{ticker}_candlestick.png")

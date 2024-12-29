import yfinance as yf

# Function to fetch histoical stock data from Yahoo Finance
def fetch_stock_data(ticker: str, period="1mo", interval="1d"):
    stock = yf.Ticker(ticker)

    data = stock.history(period=period, interval=interval)
    data.reset_index(inplace=True)

    return data

if __name__ == "__main__":
    data = fetch_stock_data("AAPL")
    print(data.head())
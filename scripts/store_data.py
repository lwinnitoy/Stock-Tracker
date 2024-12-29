import sqlite3
import pandas as pd
from data_ingestion import fetch_stock_data

# Connect to SQLite database (or create it)
conn = sqlite3.connect("data/stock_data.db")

# Fetch and store data
ticker = "AAPL"
data = fetch_stock_data(ticker)
data.to_sql(ticker, conn, if_exists="replace", index=False)

print(f"Data for {ticker} saved successfully!")

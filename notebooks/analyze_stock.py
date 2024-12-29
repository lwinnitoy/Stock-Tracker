import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

# Load data
conn = sqlite3.connect("data/stock_data.db")
data = pd.read_sql("SELECT * FROM AAPL", conn)

# Plot
data["Close"].plot(title="AAPL Stock Price Over Time")
plt.xlabel("Date")
plt.ylabel("Price")
plt.show()
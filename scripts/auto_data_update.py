import schedule
import time
from data_ingestion import fetch_stock_data

def job():
    data = fetch_stock_data("AAPL")
    print(data.head())

schedule.every().day.at("09:00").do(job)

if __name__ == "__main__":
    job()

while True:
    schedule.run_pending()
    time.sleep(1) #change to 86400 for 24 hours. currently set to 1 second for testing purposes



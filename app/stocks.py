

print("STOCKS REPORT...")

import os
from app.utils import to_usd
from app.alphavantage_service import fetch_stocks_data

#user inputs which stock data they want to see
symbol = input("Please input a stock symbol (default: 'NFLX'): ") or "NFLX"

#retrieve data for stock user wants to see data for
df = fetch_stocks_data(symbol)

#get latest stock data
latest = df.iloc[0]

#print stock information
print(symbol)
print(latest["timestamp"])
print(to_usd(latest["close"]))

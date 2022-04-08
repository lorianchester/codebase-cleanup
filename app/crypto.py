

print("CRYPTO REPORT...")

import os
from app.utils import to_usd
from app.alphavantage_service import fetch_crypto_data

#ask user which crypto data they want to see
symbol = input("Please input a crypto symbol (default: 'BTC'): ") or "BTC"

#retrieve data for crypto user wants to see data for
parsed_response = fetch_crypto_data(symbol)
tsd = parsed_response["Time Series (Digital Currency Daily)"]

#get crypto data for latest day
dates = list(tsd.keys())
latest_date = dates[0]
latest = tsd[latest_date]

#print latest crypto data
print(symbol)
print(latest_date)
print(to_usd(float(latest['4a. close (USD)'])))

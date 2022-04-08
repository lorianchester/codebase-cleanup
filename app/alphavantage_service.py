import os
from dotenv import load_dotenv
import requests
import json
from pandas import read_csv

load_dotenv()

ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", default="demo")


def fetch_crypto_data(symbol):
    """
    Fetches crypto data.
    Makes a request then parses data and converts it into a Python datastructure.
    
    Parameters:
        symbol (str): A string of a crypto symbol
    
    Returns:
        parsed_response (dict): A dictionary of the crypto data
            
    Invoke like this: fetch_crypto_data("BTC")
    """
    url = f"https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&market=USD&symbol={symbol}&apikey={ALPHAVANTAGE_API_KEY}"
    response = requests.get(url)
    parsed_response = json.loads(response.text)
    return parsed_response
    

def fetch_stocks_data(symbol):
    """
    This function fetches stock data.
    It makes a request then parses data and converts it into a Python datastructure.

    Parameters:
        symbol (str): A string of a stock symbol
    
    Returns: 
        df (DataFrame): A DataFrame of stock data

    Invoke like this: fetch_stocks_data("NFLX")
    """
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={ALPHAVANTAGE_API_KEY}&datatype=csv"
    df = read_csv(url)
    return df


def fetch_unemployment_data():
    """
    This function fetches unemployment data.
    It makes a request then parses data and converts it into a Python datastructure.
    
    Returns:
        parsed_response (dict): A dictionary of the unemployment data
    
    Invoke like this: fetch_unemployment_data()
    """
    url = f"https://www.alphavantage.co/query?function=UNEMPLOYMENT&apikey={ALPHAVANTAGE_API_KEY}"
    response = requests.get(url)
    parsed_response = json.loads(response.text)
    return parsed_response

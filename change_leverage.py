import hmac
import hashlib
import requests 
import time
import json


with open("misc/endpoints.json", "r") as f:
    endpoints = json.load(f)

with open("misc/keys.json", "r") as f:
    keys = json.load(f)

with open("tickers/binance_tickers_new.json", "r") as f:
    tickers = json.load(f)

def change_all_leverage(symbol):
    headers = {
        "X-MBX-APIKEY": keys["binance"]['public']
    }
    timestamp = int(time.time()) * 1000 # miliseconds
    queries = f"timestamp={timestamp}&recvWindow=10000&leverage=1&symbol={symbol}" # query
    signature = hmac.new(
        keys['binance']['private'].encode('utf-8'),
        msg=queries.encode('utf-8'),
        digestmod=hashlib.sha256
    ).hexdigest()
    queries = queries + f"&signature={signature}"
    response = requests.post(f"{endpoints['binance']['base_url']+endpoints['binance']['change_leverage']}?{queries}", headers=headers) 
    return response


if __name__ == "__main__":
    for symbol in tickers:
        response = change_all_leverage(symbol)
        print(response.json())

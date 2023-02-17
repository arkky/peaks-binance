import requests
import json
import pprint
import asyncio
import aiohttp
import time
import traceback
import sys
from datetime import datetime
from core import exchanges
from core.tg_bot import send_signal


with open("misc/keys.json", "rb") as f:
    keys = json.load(f)


async def calculate_arbitrage():
    with open("tickers/binance_tickers_new.json", "r") as f:
        tickers_old = json.load(f)

    await asyncio.gather(binance.get_tickers_price())
    with open("tickers/binance_tickers_new.json", "r") as f:
        tickers_new = json.load(f)

    keys_old = list(tickers_old.keys())
    keys_new = list(tickers_new.keys())

    keys = set(keys_old + keys_new)
    for key in keys:
        sample_old = tickers_old[key]
        sample_new = tickers_new[key]
        ratio = sample_old['price'] / sample_new['price']
        if ratio < diff:
            text = f"""
            Exchange: Binance\n
            Symbol: {key}\n
            Ratio: {ratio}\n
"""
            await send_signal(text)
            pprint.pprint(text)


async def main():
    pasta = f"\n{'---'*20}\nМАШИНА ДЕНЕГ ПО FUTURES ЗАПУЩЕНА ☄️☄️☄️\nРазница между ценами: {round((1-diff)*100, 2)}%\nПерезарядка на {secs} секунд\n{'---'*20}\n"
    await send_signal(pasta)
    await asyncio.gather(binance.get_tickers_price())
    while True:
        time.sleep(secs)
        await asyncio.gather(calculate_arbitrage())

if __name__ == "__main__":
    diff = 0.992
    secs = 30
    binance = exchanges.BinanceExchange()
    try:
        asyncio.run(main())
    except Exception as e:
        traceback.print_exception(*sys.exc_info())
        asyncio.run(send_signal("ПРОГРАММА ПО FUTURES ВЫКЛЮЧИЛАСЬ"))

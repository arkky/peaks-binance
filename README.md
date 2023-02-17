# Finding peaks in the last N seconds

I wrote a simple bot that looks at the trading pairs of the Binance exchange and finds the difference between prices in N seconds starting from 3% and above.

In general, I don’t know how to beat such a situation so that I can earn money.

# Logic

The logic of work is simple:

1) The program first finds a trading area for binance futures
2) If the trading pair meets the conditions (the price difference is more than 3%, the volume of sales is more than 200k USDT, etc.), then all the necessary information is sent to telegram
3) As soon as the message arrives, I immediately go to the exchange and look at the auction

# Usage

1) You need to get your binance API key and paste it into json file
2) Run the tg_core.py file. This file starts the logic of the telegram bot.
3) Run the main.py file. This file launches the logic of working with the binance exchange and interaction with the telegram
4) OPTIONAL: Run change_leverage.py file to remove x20 leverage
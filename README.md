# Discord_StockBot
Discord bot that can grab the price of any ticker on Yahoo Finance to display to your discord server 

## User Documentation 
This is a discord bot you can add to your discord server to provide real time stock price data to all server members. 
Crypto trades can also be made through the bot, see [here]([url](https://github.com/hadisrour6/TA-Trading-Bot)) for more details.

List of commands:
- .about  will bring up all commands
- .price or .$ followed by any valid ticker will bring up its price for example: .price AAPL or .$ AAPL
- .trade or .Trade will begin the 'CryptoTrading' script that will begin calculating RSI and buying/selling your crypto of choice based on RSI. When an order is made an update is sent to users phone through text 
- .sector or .sec followed by any valid ticker will return the sector said company is in
- .dividends or .div followed by any valid ticker will return the amount of dividends the company gives out to its share holders
- .shares or .Shares followed by any valid ticker will return the number of outstanding shares a company has 

## Technical Documentation 
  1. Install Python 3.7 or above. Install Python [here](https://www.python.org/).  

  2. Run ```pip install -r requirements.txt``` to install all dependencies.

  3. Edit all the crededentials in ```config.py``` to your unique keys. You can get all the keys and numbers from the discord, twilio and binance website after creating        accounts.
 
  4. Run the bot with  ```python Discord_StockBot```
 

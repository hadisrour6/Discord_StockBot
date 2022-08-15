from discord.ext import commands
from datetime import datetime
from yfinance import Ticker
from yahoo_fin.stock_info import *
from CryptoBot import run_Trade
import config

token = config.DISCORD_TOKEN
client = commands.Bot(command_prefix='.')

@client.command()
@commands.is_owner()
async def shutdown(context):
    exit()

@client.event
async def on_ready():
    print("Bot is ready")

@client.command(aliases=['About'])
async def about(ctx):
    await ctx.send(
                   "Hey! Here is a list of my commands:\n"
                   "-> .about  will bring up my commands\n"
                   "-> .price or .$ followed by any valid ticker will bring up its price for example: .price AAPL or .$ AAPL\n"
                   "-> .trade or .Trade will begin the 'CryptoTrading' script that will begin calculating RSI and buying/selling ETH "
                   "\t\tbased on RSI. When an order is made an update is sent to users phone through text\n"
                   "-> .sector or .sec followed by any valid ticker will return the sector said company is in\n"
                   "-> .dividends or .div followed by any valid ticker will return the amount of dividends the company gives out to its share holders\n"
                   "-> .shares or .Shares followed by any valid ticker will return the number of outstanding shares a company has  "
                  )

@client.command(aliases=['$'])
async def price(ctx,*, ticker):
    company = Ticker(ticker)
    company_name = company.info['longName']

    time = str(datetime.datetime.now().strftime(' %Y/%m/%d - %I:%M:%S %p EST'))

    await ctx.send("-> $" + str(round(get_live_price(ticker),3)) + " <- " + company_name + " ($" + ticker.upper() + ")" + " as of " + time)


@client.command(aliases=['sec'])
async def sector(ctx,*, ticker):
    company = Ticker(ticker)
    company_sector = company.info['sector']

    await ctx.send(company_sector)

@client.command(aliases=['Shares'])
async def shares(ctx,*, ticker):
    company = Ticker(ticker)
    company_shares = company.info['sharesOutstanding']

    await ctx.send(company_shares)

@client.command(aliases=['div'])
async def dividends(ctx,*, ticker):
    company = Ticker(ticker)
    company_dividends = company.info['dividends']

    await ctx.send(company_dividends)


@client.command(aliases=['Trade'])
async def trade(ctx):
    await ctx.send(config.CRYPTO_SYMBOL, + " is currently being bought and sold")
    run_Trade()


client.run(token)



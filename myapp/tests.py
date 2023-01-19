from django.test import TestCase
from django.db import models
import yfinance as yf

# This is a dictionary to contain all data to pass on to the website
data = {}

# I need to get a ticker from the input box
ticker = "MMM"

# get the current price
ohlc = yf.Ticker(ticker).history(period='1d')
data['current_price'] = ohlc['Close'][0]

# get stock info
print(msft.info)


class stock(models.Model):

    ticker = str(models.CharField(max_length=10))

    if ticker == "":
        ticker = "DIS"

# Yfinance is not working and cannot retrieve all the information
    stock_info = yf.Ticker(ticker).info
    stock_name = stock_info['longName']
    stock_biz = stock_info['longBusinessSummary']
    def __repr__(self):
        return self.ticker + " " + self.stock_name
    def __str__(self):
        return self.ticker + " " + self.stock_name



"""
import snscrape.modules.twitter as sntwitter
import pandas as pd


name = "Eli Lilly"

dic = {}

for i, tweet in enumerate(
        sntwitter.TwitterSearchScraper(name).get_items()):

    dic[i] = tweet.content

    if i > 20:
        break

for x in dic:
    print(dic[x])


# col = ['date','CONTENT','USER_NAME']

# df = pd.DataFrame(tweets , columns =   col               )

# print(df['CONTENT'])
"""
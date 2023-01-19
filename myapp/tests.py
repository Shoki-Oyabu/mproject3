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
from mproject2.settings import STATICFILES_DIRS

("how to upload CSV!\"!!\n"
 "    import csv\n"
 "    from myapp.models import Stock\n"
 "\n"
 "    # with open(r\"C:\Users\Shoki\PycharmProjects\djangoProject\mproject2\static\List_Equities.csv\") as file:\n"
 "        reader = csv.reader(file)\n"
 "        next(reader)\n"
 "\n"
 "        for row in reader:\n"
 "            stock = Stocks(tick=row[0], name=row[1],country=row[2] , IPO=row[3] , sector=row[4])\n"
 "            stock.save()\n")

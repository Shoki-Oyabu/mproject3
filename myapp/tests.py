from django.test import TestCase
from django.db import models
import yfinance as yf

# This is a dictionary to contain all data to pass on to the website
data = {}

# I need to get a ticker from the input box
ticker = "MMM"

# get the current price
ohlc = yf.Ticker(ticker).history(period='100d')
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



def get_currency_list():
    currency_list = list()
    import requests
    from bs4 import BeautifulSoup
    url = "https://thefactfile.org/countries-currencies-symbols/"
    response = requests.get(url)
    if not response.status_code == 200:
        return currency_list
    soup = BeautifulSoup(response.content, features="lxml")
    data_lines = soup.find_all('tr')
    for line in data_lines:
        try:
            detail = line.find_all('td')
            currency = detail[2].get_text().strip()
            iso = detail[3].get_text().strip()
            if (currency,iso) in currency_list:
                continue
            currency_list.append((currency,iso))
        except:
            continue

        print(currency_list)
    return currency_list

def add_currencies(currency_list):
    for currency in currency_list:
        currency_name = currency[0]
        currency_symbol = currency[1]
    try:
        c = Currency.objects.get(iso=currency_symbol)
    except:
        c = Currency(long_name=currency_name, iso=currency_symbol)
        c.save()




data["time_of_day"] = datetime.datetime.now()
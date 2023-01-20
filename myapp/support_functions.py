def getmarketdata(ticker):
    import yfinance as yf
    import matplotlib.pyplot as plt

    num_shares = yf.Ticker(ticker).shares.iloc[-1,0]
    ohlc = yf.Ticker(ticker).history(period='100d')
    market_cap = num_shares * ohlc.Close[-1]
    open = ohlc.Open[-1]
    high = ohlc.High[-1]
    low = ohlc.Low[-1]
    close = ohlc.Close[-1]

    ohlc.Close.plot(kind='line',
                    title='Stock price chart',
                    legend=True)
    # When local, use plt.savefig(r'C:\Users\Shoki\PycharmProjects\djangoProject\mproject2\static\chart.png')
    plt.savefig('/static/chart.png')

    return(open, high, low, close, market_cap)

def DMS_to_decimal(dms_coordinates):
    degrees = int(dms_coordinates.split('°')[0])
    minutes = int(dms_coordinates.split('°')[1].split("′")[0])
    try:
        seconds = int(dms_coordinates.split('°')[1].split("′")[1][:2])
    except:
        seconds = 0.0
    decimal = degrees + minutes/60 + seconds/3600
    try:
        if dms_coordinates[-1] == "S":
            decimal = -decimal
    except:
        pass
    try:
        if dms_coordinates[-1] == "W":
            decimal = -decimal
    except:
        pass
    return decimal

def get_lat_lon(city_name):
    import requests
    from bs4 import BeautifulSoup
    try:
        city = City.objects.get(name=city_name)
        lat = city.latitude
        lon = city.longitude
        wiki_link = ""
    except:
        url = "https://en.wikipedia.org/wiki/"
        url += city_name.replace(" ","_")
        wiki_link = url
        try:
            text = requests.get(url).text
            soup = BeautifulSoup(text)
            lat = soup.find('span', class_="latitude").get_text()
            lon = soup.find('span', class_="longitude").get_text()
            lat = DMS_to_decimal(lat)
            lon = DMS_to_decimal(lon)
        except:
            lat = 0.0
            lon = 0.0
    return lat,lon,wiki_link


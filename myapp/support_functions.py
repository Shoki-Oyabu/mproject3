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


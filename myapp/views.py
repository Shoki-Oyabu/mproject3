import folium as folium
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from mproject2.settings import STATICFILES_DIRS
from django.contrib.auth.models import User
from myapp import support_functions
from myapp.models import AccountHolder, Stock


def home(request):
    from myapp.models import Stock
    data = dict()
    ticker_list = Stock.objects.all()
    data["ticker_list"] = ticker_list

    return render(request, "home.html", context=data)

"""def maintenance(request):
    data = dict()
    try:
        choice = request.GET['selection']
        if choice == "currencies":
            support_functions.add_currencies(support_functions.get_currency_list())
            c_list = Currency.objects.all()
            # print("Got c_list", len(c_list))
            data['currencies'] = c_list
            return HttpResponseRedirect(reverse('currencies'))
    except:
        pass
    return render(request, "maintenance.html", context=data)
"""

def DBsearch(request):
    from myapp.models import Stock
    data = dict()
    ticker_list = Stock.objects.all()
    data["ticker_list"] = ticker_list

    try:
        search = request.GET['search'].upper()
        result = Stock.objects.get(tick=search)
        data['s_ticker'] = result.tick
        data['s_name'] = result.name
        data['s_IPO'] = result.IPO
        data['s_country'] = result.country
        data['s_sector'] = result.sector
    except:
       pass

    return render(request, "DBsearch.html", context=data)

def DBupdate(request):
    from myapp.models import Stock
    data = dict()
    ticker_list = Stock.objects.all()
    data["ticker_list"] = ticker_list

    try:
        Ticker = request.GET['Ticker']
        Name = request.GET['Name']
        Country = request.GET['Country']
        IPOY = request.GET['IPOY']
        Sector = request.GET['Sector']

        if len(Ticker) * len(Name) * len(Country) * len(IPOY) * len(Sector) > 0:
            new_stock = Stock(tick=Ticker,name=Name,country=Country,IPO=IPOY,sector=Sector)
            new_stock.save()
            data['result'] = 'The database is updated. The company has successfully added to the list!'
            data['ticker'] = Ticker
            data['name'] = Name
            data['country'] = Country
            data['IPO'] = IPOY
            data['sector'] = Sector
        else:
            data['result'] = 'The database has not been updated. Please enter all information.'

    except:
        data['result'] = 'The database has not been updated. Please enter all information.  '
        pass

    return render(request, "DBupdate.html", context=data)

def test(request):
    import csv
    from myapp.models import Stock
    from myapp.models import NumShares

    #for i in range(-1000,1000):
     #   number = NumShares(num=i)
      #  number.save()

#    with open("/static/List_Equities.csv") as file:
#        reader = csv.reader(file)
#        next(reader)
#        for row in reader:
#            stock = Stock(tick=row[0], name=row[1],country=row[2] , IPO=row[3] , sector=row[4])
#            stock.save()
    return render(request, "test.html")


def result(request):
    from myapp.models import Stock
    import yfinance as yf
    from django.shortcuts import render
    import matplotlib.pyplot as plt
    import io
    import urllib, base64

    data = dict()
    ticker_list = Stock.objects.all()
    data["ticker_list"] = ticker_list

    try:
        query = request.GET["ticker"].upper()
        found = Stock.objects.get(tick=query)
        data['ticker'] = query
        data['name'] = found.name
        data['sector'] = found.sector
        data['country'] = found.country
        num_shares = yf.Ticker(query).shares.iloc[-1, 0]
        ohlc = yf.Ticker(query).history(period='100d')
        data['market_cap'] = round(num_shares * ohlc.Close[-1]/1000000)
        data['open'] = round(ohlc.Open[-1],2)
        data['high'] = round(ohlc.High[-1],2)
        data['low'] = round(ohlc.Low[-1],2)
        data['close'] = round(ohlc.Close[-1],2)

        chart_title = found.name + ' Price Chart'
        plt.clf()
        ohlc.Close.plot(kind='line', title=chart_title, legend=True)
        fig = plt.gcf()
        buf = io.BytesIO()
        fig.savefig(buf, format='png')
        buf.seek(0)
        string = base64.b64encode(buf.read())
        uri = urllib.parse.quote(string)
        #plt.savefig("/static/chart111.png")
        # plt.savefig(r'C:\Users\Shoki\PycharmProjects\djangoProject\mproject2\static\chart.png')
        data['uri'] = uri

    except:
        newthing = request.GET["ticker"].upper()
        data['ticker'] = newthing
        return render(request, "notfound.html", context=data)
        pass

    return render(request, "result.html", context=data)





def register_new_user(request):
    context = dict()
    form = UserCreationForm(request.POST)
    if form.is_valid():
        new_user = form.save()
        dob = request.POST["dob"]
        acct_holder = AccountHolder(user=new_user,date_of_birth=dob)
        acct_holder.save()
        return render(request,"home.html",context=context)
    else:
        form = UserCreationForm()
        context['form'] = form
        return render(request, "registration/register.html", context=context)

def added(request):
    from myapp.models import Stock
    from myapp.models import NumShares

    data = dict()
    user = request.user
    if user.is_authenticated:
        shares = request.GET["sharenum"]
        target = request.GET["target"]
        account_holder = AccountHolder.objects.get(user=user)
        account_holder.stocks_holding.add(Stock.objects.get(tick=target))
        account_holder.shares.add(NumShares.objects.get(num=shares))
        final_list=[]
        num_shares_list = NumShares.objects.all()
        for x in account_holder.stocks_holding.all():
            for y in range(len(num_shares_list)):
                holding = x.tick
                sharenum = num_shares_list[y].num
                final_list.append([holding,sharenum])

        data['portfolio'] = final_list
        #data['holding'] = account_holder.stocks_holding.all()
        #data['num_shares'] = account_holder.shares.all()
        #data['account_holder'] = account_holder

    else:
        return render(request, "usernotfound.html", context=data)
        pass

    return render(request, "added.html", context=data)

def usernotfound(request):
    data = dict()
    return render(request, "usernotfound.html", context=data)

def portfolio(request):
    from myapp.models import Stock

    data = dict()
    user = request.user
    if user.is_authenticated:
        account_holder = AccountHolder.objects.get(user=user)
        data['account_holder'] = account_holder

    else:
        return render(request, "usernotfound.html", context=data)
        pass

    return render(request, "portfolio.html", context=data)


def backtest(request):
    from myapp.models import Stock
    import yfinance
    from django.shortcuts import render
    import matplotlib.pyplot as plt
    import io
    import urllib, base64

    data = dict()
    user = request.user
    if user.is_authenticated:
        account_holder = AccountHolder.objects.get(user=user)
        data['account_holder'] = account_holder


    else:
        return render(request, "usernotfound.html", context=data)
        pass

    return render(request, "backtest.html", context=data)
import folium as folium
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from mproject2.settings import STATICFILES_DIRS
from django.contrib.auth.models import User
from myapp import support_functions
from myapp.models import AccountHolder


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
    import matplotlib
    import matplotlib.pyplot as plt

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
        data['market_cap'] = round(num_shares * ohlc.Close[-1])
        data['open'] = round(ohlc.Open[-1],2)
        data['high'] = round(ohlc.High[-1],2)
        data['low'] = round(ohlc.Low[-1],2)
        data['close'] = round(ohlc.Close[-1],2)

        user = request.user

        if user.is_authenticated:
            account_holder = AccountHolder.objects.get(user=user)
            account_holder.stocks_visited.add(Stock.objects.get(tick=query))
            data['stocks_visited'] = account_holder.stocks_visited.all()
    except:
        newthing = request.GET["ticker"].upper()
        data['ticker'] = newthing
        return render(request, "notfound.html", context=data)
        pass

    try:
        plt.clf()
        ohlc.Close.plot(kind='line',
                        title=found.name + ' price chart',
                        legend=True)
        plt.savefig('/static/chart.png')
        # plt.savefig(r'C:\Users\Shoki\PycharmProjects\djangoProject\mproject2\static\chart.png')

    except:
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

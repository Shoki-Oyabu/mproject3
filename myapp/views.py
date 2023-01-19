from django.shortcuts import render
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.

def home(request):
    data = dict()
    try:
        ticker = request.GET['ticker']
        if len(ticker) > 0:
            return HttpResponseRedirect(reverse('ticker'))
    except:
        pass


    data["time_of_day"] = datetime.datetime.now()
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
        search = request.GET['search']
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
    with open( STATICFILES_DIRS, "/List_Equities.csv") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            stock = Stock(tick=row[0], name=row[1],country=row[2] , IPO=row[3] , sector=row[4])
            stock.save()

    return render(request, "test.html")
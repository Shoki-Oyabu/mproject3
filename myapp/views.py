from django.shortcuts import render
import datetime

# Create your views here.

def home(request):
    data = dict()
    data["time_of_day"] = datetime.datetime.now()
    return render(request, "home.html", context=data)
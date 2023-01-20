"""mproject2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path("", views.home, name="home"),
    path('home',views.home, name='home'),
    # path('maintenance', views.maintenance, name='maintenance'),
    path("DBsearch", views.DBsearch, name="DBsearch"),
    path("DBupdate", views.DBupdate, name="DBupdate"),
    path("test", views.test, name="test"),
    path("result", views.result, name="result"),
    path("notfound", views.result, name="notfound"),
    path('register',views.register_new_user,name="register_user"),
    path('added',views.added,name="added"),
    path('usernotfound',views.usernotfound,name="usernotfound"),
    path('portfolio', views.portfolio, name='portfolio'),
    path('backtest', views.backtest, name='backtest'),
    # path('map',views.map,name='map'),


]

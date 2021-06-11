from aiohttp.web_routedef import static
from django.urls import path, include

from myproj import settings
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^creat_in/$', views.creat_in, name='creat_in'),
]



from django.urls import path

from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('chainsaw', views.chainsaw, name='chainsaw'),
    path('gas_drills', views.gas_drills, name='gas_drills'),
    path('gas_cutters', views.gas_cutters, name='gas_cutters'),
    path('concrete_mixers', views.concrete_mixers, name='concrete_mixers'),
    path('grinders', views.grinders, name='grinders'),
    path('generators', views.generators, name='generators'),
    path('stairs', views.stairs, name='stairs'),
    path('mixers', views.mixers, name='mixers'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^creat_in/$', views.creat_in, name='creat_in'),
]



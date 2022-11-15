
from django.urls import path
from . import views

"""Urls for this app 
url for home and url for about
"""
urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
]

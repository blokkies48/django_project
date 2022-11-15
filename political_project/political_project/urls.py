from django.contrib import admin
from django.urls import include, path

"""Includes all the urls to the related apps for the project
"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("base.urls")),
    path('news/', include('news.urls')),
    path('discussions/', include('discu.urls')),
    path('login/', include('login.urls')),
]

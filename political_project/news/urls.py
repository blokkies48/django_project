from django.views.generic import ListView, DetailView
from django.urls import path
from .models import Post
# URL patterns getting the list of post and ordering them by date
urlpatterns = [
    path('', ListView.as_view(queryset= Post.objects.all().order_by("-date")[:25],template_name="news/news.html")),   
    path('<int:pk>/',DetailView.as_view(model=Post, template_name="news/post.html")),   
]
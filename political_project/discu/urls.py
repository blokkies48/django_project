from django.views.generic import ListView, DetailView
from django.urls import path
from .models import Discussion
from . import views


urlpatterns = [
    path('', views.discussions, name="discussions"),
    path('<str:pk>/', views.discussion, name="discussion"),
    #path('<int:pk>/',DetailView.as_view(model=Discussion, template_name="discussions/discussion.html"))
]
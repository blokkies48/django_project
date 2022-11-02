from django.urls import path
from . import views


urlpatterns = [
    path('', views.discussions, name="discussions"),
    # For starting a discussion and updating and deleting
    path('new-discussion/', views.start_discussion, name="new_discussion"),
    path('update-discussion/<str:pk>/', views.update_discussion, name="update-discussion"),
    path('delete-discussion/<str:pk>/', views.delete_discussion, name="delete-discussion"),
    path('delete-comment/<str:pk>/', views.delete_comment, name="delete-comment"),
    # This caused a bug in django so had to be placed at the end
    # To avoid said bug when adding a new discussion
    path('<str:pk>/', views.discussion, name="discussion"),

    
   
]
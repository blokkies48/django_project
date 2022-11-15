from django.db import models

# Create your models here.
class Post(models.Model):
    '''Table model for post'''
    title = models.CharField(max_length=140)
    date = models.DateField(auto_now_add=True)
    body = models.TextField()
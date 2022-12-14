from django.db import models
# User from django
from django.contrib.auth.models import User

# Used for relationship key
class Topic(models.Model):
    """Table model for the Topics"""
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

# Main table for the discussion
class Discussion(models.Model):
    """Table model for the Discussion"""
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=140)
    description = models.TextField(null=True, blank=True)
    update = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    # Used to order from newest to oldest
    class Meta:
        ordering = ['-update', '-created']

    def __str__(self):
        return self.title

# Message that displays on the table page
class Message(models.Model):
    """Table model for the Message"""
    # Setting user key
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Relationship between other database 
    # Deletes when main is deleted
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE) 
    body = models.TextField()
    update = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]
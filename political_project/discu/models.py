from cgi import parse_multipart
from django.db import models

# Create your models here.
class Discussion(models.Model):
    #host =
    #topic =
    title = models.CharField(max_length=140)
    description = models.TextField(null=True, blank=True)
    #participants =
    update = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
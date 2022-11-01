from django.contrib import admin
from .models import Discussion, Topic, Message
# Register your models here.

admin.site.register(Discussion)
admin.site.register(Topic)
admin.site.register(Message)
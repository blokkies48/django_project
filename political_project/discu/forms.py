# This is the form model from django

from django.forms import ModelForm
from .models import Discussion

class Discussion_Form(ModelForm):
    class Meta:
        model = Discussion
        fields = "__all__"
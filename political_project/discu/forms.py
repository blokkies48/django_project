# This is the form model from django

from django.forms import ModelForm
from .models import Discussion

class Discussion_Form(ModelForm):
    """Form used for the discussion"""
    class Meta:
        model = Discussion
        fields = "__all__"
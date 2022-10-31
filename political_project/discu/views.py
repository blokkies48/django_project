from django.shortcuts import render 
from .models import Discussion
# Create your views here.


def discussions(request):
    discussions1 = Discussion.objects.all()
    context = {'discussions': discussions}
    return render(request, 'discussions/discussions.html', context)

def discussion(request, pk):
    discussion = Discussion.objects.get(id=pk)
    context = {'discussion': discussion}

    return render(request, 'discussions/discussion.html', context)
from django.shortcuts import render

# Create your views here.

def home(request):
    ''':returns: home template'''
    return render(request,"base/home.html")

def about(request):
    ''':returns: about template'''
    return render(request, 'base/about.html')

def rooms(request):
    ''':returns: discussions template'''
    return render(request,"base/discussions.html")
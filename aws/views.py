from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("hiii welcome")

def homepage(request):
    return render(request,"index.html")
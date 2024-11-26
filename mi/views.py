from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def captain(request):
    return HttpResponse('<h1>Hardik pandya is the Captain of MI</h1>')

def vicecaptain(request):
    return HttpResponse('<h1>Rohit sharma is the Vice-Captain of MI</h1>')
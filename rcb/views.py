from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def captain(request):
    return HttpResponse('<h1>Kohli is the captain of RCB</h1>')

def vicecaptain(request):
    return HttpResponse('<h1>Rajat Patidar is the Vice-captain of RCB</h1>')
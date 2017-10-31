from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>hello this is my first web site </h1>')

# Create your views here.

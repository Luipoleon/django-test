from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from datetime import datetime

def home(request):
    return HttpResponse("Welcome to Little Lemon!")


def say_hello(request):
    return HttpResponse("<h1>Hello World<h1/>")



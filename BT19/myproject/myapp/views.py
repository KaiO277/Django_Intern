from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def hello_world(request):
    return HttpResponse('Hello World')

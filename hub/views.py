from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hub(request):
    return HttpResponse('<h1>hello github</h1>')

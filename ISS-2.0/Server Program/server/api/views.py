from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
import os

def index(request):
    index = loader.get_template('api.html')
    return HttpResponse(index.render())
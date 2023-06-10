from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
import os
from api.models import iss_2_input
def index(request):
    data = iss_2_input.objects.all().values()
    index = loader.get_template('dbadmin.html')
    context = {
    'data': data,
  }
    return HttpResponse(index.render(context, request))
def users(request):
    data = User.objects.all().values()
    admin = loader.get_template('admin.html')
    context = {
        'data': data,
    }
    return HttpResponse(admin.render(context, request))
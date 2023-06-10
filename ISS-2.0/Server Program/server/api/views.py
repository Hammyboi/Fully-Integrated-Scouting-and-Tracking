from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from server.settings import settings
import os
from .clean_data import *
from .models import iss_2_input
input_fields = ['username', 'names', 'match', 'robot', 'teamnumber', 'noshow', 'location', 'auto_upper_cone', 'auto_middle_cone', 'auto_lower_cone', 'auto_upper_cube', 'auto_middle_cube', 'auto_lower_cube', 'mobility', 'auto_pickup', 'auto_dock_engage', 'teleop_upper_cone', 'teleop_middle_cone', 'teleop_lower_cone', 'teleop_upper_cube', 'teleop_middle_cube', 'teleop_lower_cube', 'teleop_pickup', 'links', 'early_endgame', 'endgame', 'num_docked', 'skill', 'defense', 'died', 'tipped', 'card', 'damage', 'comments', 'md5']


def index(request):
    # for debugging if 500 error occurs
    def print_model_values(model_obj):
    # Get all the fields of the model
        fields = model_obj._meta.fields
    
    # Iterate over the fields and print their values
        for field in fields:
            field_name = field.name
            field_value = getattr(model_obj, field_name)
            print(f"{field_name}: {field_value}")

    index = loader.get_template('api.html')
    if "string" in request.GET:
        input = request.GET.copy().__getitem__("string")
        input_array = [input.split("~")[0]] + input.split("~")[2:]
        user = authenticate(username=input.split("~")[0], password=input.split("~")[1])
        if user is not None and user.groups.filter(name__in=settings['allowed_groups']).exists():
            login(request, user)
            input_dict = dict(zip(input_fields, input_array))
            clean(input_dict)
            input_query = iss_2_input(**input_dict)
            # print_model_values(input_query)
            input_query.save()
            return HttpResponse("<script>window.alert('Data Entered Successfully!');window.close();</script>")
        elif user is not None:
            return HttpResponse("<script>window.alert('You do not have the required permissions.');window.close();</script>")
        else:
            return HttpResponse("<script>window.alert('Invalid user.');window.close();</script>")
        
    else:
        return HttpResponse(index.render({}, request))
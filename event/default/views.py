import os
from django import http
from django.shortcuts import render
from default import forms
from default import models
from django.http import JsonResponse
import pprint

# Create your views here.

def index(request):

    context = {}
    return render(request, 'default/index.html', context=context)

# def login(request):

#     context = {}
#     return render(request, 'default/login.html' ,context=context)

def contact_us(request):

    context = {}
    return render(request, 'default/contact_us.html' ,context=context)



def insert_into_db(request):
    eventform = forms.InsertEventForm()

    if request.method == "POST":
        form = forms.InsertEventForm(request.POST, request.FILES)
        print(form.__dict__)
        if form.is_valid():
            # save the form data to model
            event = models.Event()

            event.title = form.cleaned_data.get("title")
            event.description = form.cleaned_data.get("description")
            event.date = form.cleaned_data.get("date")
            event.location = form.cleaned_data.get("location")
            event.cover_image = form.cleaned_data.get("cover_image")
            event.time_start_at = form.cleaned_data.get("time_start_at")
            event.time_end_at = form.cleaned_data.get("time_end_at")
            event.set_created_date()
            event.set_modified_date()

            pprint.pprint(event.__dict__)
            
            event.save()

    context = {'eventform': eventform}
    return render(request, 'default/insert_into_db.html', context=context)

def test_load(request):
    hostname = os.uname()[1]
    context = {'message': 'Hello World', 'name': hostname }
    return JsonResponse(context)

def get_events(request):
    events = models.Event.objects.all()
    context = {'events': events}
    return render(request, 'default/get_events.html', context=context)
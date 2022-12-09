from django.shortcuts import render
from .models import Reminder
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def index(request):
    reminders = Reminder.objects.all()
    empty_list = []
    for reminder in reminders:
        empty_list.append({'id': reminder.id, 'title': reminder.title, 'description': reminder.description})
    dictionary = {'reminders': empty_list}
    return JsonResponse(dictionary)
@csrf_exempt
def new_reminder(request):
    #breakpoint()
    data = json.loads(request.body)
    title = data.get('title')
    description = data.get('description')
    reminder = Reminder.objects.create(title=title, description=description)
    di = {'id': reminder.id, 'title': title, 'description': description}
    return JsonResponse(di)
    
    


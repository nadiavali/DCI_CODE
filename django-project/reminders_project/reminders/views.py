from django.shortcuts import render
from .models import Reminder



# Create your views here.
from django.http import HttpResponse, JsonResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def index(request):
    reminders = Reminder.objects.all()
    empty_list = []
    for reminder in reminders:
        empty_list.append({'id': reminder.id, 'title': reminder.title, 'description': reminder.description})
    dictionary = {'reminders': empty_list}
    return JsonResponse(dictionary)


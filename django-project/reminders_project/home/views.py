from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def index(request):
    numbers = range(0, 2000)
    context = {'numbers': numbers}
    return render(request, 'home/index.html', context)

def hello_json(request):
    return JsonResponse({'name': 'Nadia'})

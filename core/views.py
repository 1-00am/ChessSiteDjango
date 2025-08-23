from django.shortcuts import render
from django.http import JsonResponse
import json

# Create your views here.

def home(request):
    return render(request, 'home.html')

def game(request):
    return render(request, 'game.html')

def move(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
    return JsonResponse({
        'hel': 'lo'
    })

from django.shortcuts import render
from .models import Team

# Create your views here.
def index(request):  
    context = {
        'title': 'Home',
    }
    return render(request, 'pages/index.html', context)

def about(request):
    teams       = Team.objects.all() 
    context = {
        'teams': teams,
        'title': 'About Us',
    }
    return render(request, 'pages/about.html', context)

def service(request):
    context = {
        'title': 'Services',
    }
    return render(request, 'pages/services.html', context)
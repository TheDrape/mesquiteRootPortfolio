from django.shortcuts import render
from django.http import HttpResponse, request
# Create your views here.


def home(request):
    return render(request, 'port_app/home.html')

def projects(request):
    return render(request, 'port_app/projects.html')

def projects2(request):
    return render(request, 'port_app/projects2.html')

def bio(request):
    return render(request, 'port_app/bio.html')

def trackFarm(request):
    return render(request, 'port_app/projects/trackfarm.html')

def thereapy(request):
    return render(request, 'port_app/projects/thereapy.html')

def phpmotors(request):
    return render(request, 'port_app/projects/phpmotors.html')

def cages(request):
    return render(request, 'port_app/projects/cages.html')

def purple(request):
    return render(request, 'port_app/projects/purple.html')


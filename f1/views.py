from django.shortcuts import render
from .services import get_drivers

def index(request):
    return render(request, 'index.html')

def circuits(request):
    return render(request, 'circuits.html')

def constructors(request):
    return render(request, 'constructors.html')

def drivers(request):
    drivers = get_drivers()
    return render(request, 'drivers.html', {'drivers': drivers})

def seasons(request):
    return render(request, 'seasons.html')

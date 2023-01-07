from django.shortcuts import render
from .services import get_circuits, get_constructors, get_drivers, get_seasons


def index(request):
    return render(request, 'index.html')


def circuits(request):
    circuits = get_circuits()
    return render(request, 'circuits.html', {'circuits': circuits})


def constructors(request):
    constructors = get_constructors()
    return render(request, 'constructors.html', {'constructors': constructors})


def drivers(request):
    drivers = get_drivers()
    return render(request, 'drivers.html', {'drivers': drivers})


def seasons(request):
    seasons = get_seasons()
    return render(request, 'seasons.html', {'seasons': seasons})

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def circuits(request):
    return render(request, 'circuits.html')

def constructors(request):
    return render(request, 'constructors.html')

def drivers(request):
    return render(request, 'drivers.html')

def seasons(request):
    return render(request, 'seasons.html')

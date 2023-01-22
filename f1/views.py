from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from .services import *
from datetime import date

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

def index(request):
    return render(request, 'index.html')

@cache_page(CACHE_TTL)
def drivers(request):
    drivers = get_drivers(request)
    return render(request, 'drivers.html', {'drivers': drivers})

@cache_page(CACHE_TTL)
def constructors(request):
    constructors = get_constructors(request)
    return render(request, 'constructors.html', {'constructors': constructors})

@cache_page(CACHE_TTL)
def circuits(request):
    circuits = get_circuits(request)
    return render(request, 'circuits.html', {'circuits': circuits})

@cache_page(CACHE_TTL)
def races(request):
    races = get_races(request)
    return render(request, 'races.html', {'races': races})

@cache_page(CACHE_TTL)
def qualifyings(request, round):
    qualifyings = get_qualifyings(request, round)
    return render(request, 'qualifyings.html', {'qualifyings': qualifyings})

@cache_page(CACHE_TTL)
def race_results(request, round):
    raceResults = get_race_results(request, round)
    return render(request, 'race_results.html', {'raceResults': raceResults})

@cache_page(CACHE_TTL)
def pit_stops(request, round):
    pitStops = get_pit_stops(request, round)
    return render(request, 'pit_stops.html', {'pitStops': pitStops})

@cache_page(CACHE_TTL)
def lap_times(request, round):
    lapTimes = get_lap_times(request, round)
    return render(request, 'lap_times.html', {'lapTimes': lapTimes})

@cache_page(CACHE_TTL)
def driver_standings(request, round):
    driverStandings = get_driver_standings(request, round)
    return render(request, 'driver_standings.html', {'driverStandings': driverStandings})

@cache_page(CACHE_TTL)
def constructor_standings(request, round):
    constructorStandings = get_constructor_standings(request, round)
    return render(request, 'constructor_standings.html', {'constructorStandings': constructorStandings})

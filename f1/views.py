from django.shortcuts import render
from .services import *
from datetime import date


def index(request):
    return render(request, 'index.html')


def drivers(request):
    drivers = get_drivers(request)
    return render(request, 'drivers.html', {'drivers': drivers})


def constructors(request):
    constructors = get_constructors(request)
    return render(request, 'constructors.html', {'constructors': constructors})


def circuits(request):
    circuits = get_circuits(request)
    return render(request, 'circuits.html', {'circuits': circuits})


def races(request):
    races = get_races(request)
    return render(request, 'races.html', {'races': races})


def qualifyings(request, round):
    qualifyings = get_qualifyings(request, round)
    return render(request, 'qualifyings.html', {'qualifyings': qualifyings})


def race_results(request, round):
    raceResults = get_race_results(request, round)
    return render(request, 'race_results.html', {'raceResults': raceResults})


def pit_stops(request, round):
    pitStops = get_pit_stops(request, round)
    return render(request, 'pit_stops.html', {'pitStops': pitStops})


def lap_times(request, round):
    lapTimes = get_lap_times(request, round)
    return render(request, 'lap_times.html', {'lapTimes': lapTimes})


def driver_standings(request, round):
    driverStandings = get_driver_standings(request, round)
    return render(request, 'driver_standings.html', {'driverStandings': driverStandings})


def constructor_standings(request, round):
    constructorStandings = get_constructor_standings(request, round)
    return render(request, 'constructor_standings.html', {'constructorStandings': constructorStandings})

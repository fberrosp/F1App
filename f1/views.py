from django.conf import settings
from django.core.cache import cache
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_page

from .services import *

from functools import wraps

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

#caches the entire view
def cache_page_redis(timeout):
    def decorator(func):
        @wraps(func)
        def wrapper(request, *args, **kwargs):
            season = request.session.get('season', int(date.today().year))
            cache_key = f"{func.__name__}_{season}"
            response = cache.get(cache_key)
            if response is None:
                response = func(request, *args, **kwargs)
                cache.set(cache_key, response, timeout)
            return response
        return wrapper
    return decorator

@cache_page_redis(CACHE_TTL)
def index(request):
    season = request.session.get('season', int(date.today().year))
    return render(request, 'index.html', {'season': season})

@cache_page_redis(CACHE_TTL)
def drivers(request):
    season = request.session.get('season', int(date.today().year))
    drivers = cache.get(f"drivers_{season}")

    if drivers is None:
        drivers = get_drivers(request)
        cache.set(f"drivers_{season}", drivers, CACHE_TTL)

    return render(request, 'drivers.html', {'drivers': drivers, 'season': season})

@cache_page_redis(CACHE_TTL)
def constructors(request):
    season = request.session.get('season', int(date.today().year))
    constructors = cache.get(f"constructors_{season}")

    if constructors is None:
        constructors = get_constructors(request)
        cache.set(f"constructors_{season}", constructors, CACHE_TTL)

    return render(request, 'constructors.html', {'constructors': constructors, 'season': season})

@cache_page_redis(CACHE_TTL)
def circuits(request):
    season = request.session.get('season', int(date.today().year))
    circuits = cache.get(f"circuits_{season}")

    if circuits is None:
        circuits = get_circuits(request)
        cache.set(f"circuits_{season}", circuits, CACHE_TTL)

    return render(request, 'circuits.html', {'circuits': circuits, 'season': season})

@cache_page_redis(CACHE_TTL)
def races(request):
    season = request.session.get('season', int(date.today().year))
    races = cache.get(f"races_{season}")

    if races is None:
        races = get_races(request)
        cache.set(f"races_{season}", races, CACHE_TTL)

    return render(request, 'races.html', {'races': races, 'season': season})

#@cache_page(CACHE_TTL)
def qualifyings(request, round):
    qualifyings = get_qualifyings(request, round)
    return render(request, 'qualifyings.html', {'qualifyings': qualifyings})

#@cache_page(CACHE_TTL)
def race_results(request, round):
    raceResults = get_race_results(request, round)
    return render(request, 'race_results.html', {'raceResults': raceResults})

#@cache_page(CACHE_TTL)
def pit_stops(request, round):
    pitStops = get_pit_stops(request, round)
    return render(request, 'pit_stops.html', {'pitStops': pitStops})

#@cache_page(CACHE_TTL)
def lap_times(request, round):
    lapTimes = get_lap_times(request, round)
    return render(request, 'lap_times.html', {'lapTimes': lapTimes})

#@cache_page(CACHE_TTL)
def driver_standings(request, round):
    driverStandings = get_driver_standings(request, round)
    return render(request, 'driver_standings.html', {'driverStandings': driverStandings})

#@cache_page(CACHE_TTL)
def constructor_standings(request, round):
    constructorStandings = get_constructor_standings(request, round)
    return render(request, 'constructor_standings.html', {'constructorStandings': constructorStandings})

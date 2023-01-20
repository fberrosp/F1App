import os
import requests
import time
import json

from .models import Drivers, Qualifyings
from datetime import date
from collections import OrderedDict


# method to get F1 API data from Ergast API
def get_api_data(api_endpoint):
    url = 'https://ergast.com/api/f1/{}.json?limit=10000'.format(api_endpoint)
    response = requests.get(url).json()

    return response['MRData']


'''
try:
    get data from cache
except: data does not exist or data needs to be updated:
    try:
        get data from database unless its expired
        
        update cache
        
    except: not (is up to date)
        get data from api

        update database
        
        update cache
'''


def get_drivers(request):

    seasonDrivers = str(request.session['season'] - 1) + '/' + 'drivers'

    drivers = get_api_data(seasonDrivers)['DriverTable']['Drivers']

    '''
    for driver in drivers:

        try:
            driverNumber = driver['permanentNumber']
        except:
            driverNumber = None

        try:
            driverCode = driver['code']
        except:
            driverCode = None

        driver_data = Drivers(
            driverId=driver['driverId'],
            number=driverNumber,
            code=driverCode,
            forename=driver['givenName'],
            surname=driver['familyName'],
            dob=driver['dateOfBirth'],
            nationality=driver['nationality'],
            url=driver['url']
        )

        driver_data.save()

    all_drivers = Drivers.objects.all().order_by('driverId')
    '''

    return drivers


def get_constructors(request):
    seasonConstructors = str(
        request.session['season'] - 1) + '/' + 'constructors'
    constructors = get_api_data(seasonConstructors)[
        'ConstructorTable']['Constructors']
    return constructors


def get_circuits(request):
    seasonCircuits = str(request.session['season'] - 1) + '/' + 'circuits'
    circuits = get_api_data(seasonCircuits)['CircuitTable']['Circuits']
    return circuits


def get_races(request):
    seasonRaces = str(request.session['season'] - 1) + '/' + 'races'
    races = get_api_data(seasonRaces)['RaceTable']['Races']
    return races


def get_qualifyings(request, round):
    roundQualifyings = str(
        request.session['season'] - 1) + '/' + str(round) + '/' + 'qualifying'
    qualifyings = get_api_data(roundQualifyings)[
        'RaceTable']['Races']
    return qualifyings


def get_race_results(request, round):
    roundRaces = str(request.session['season'] - 1) + \
        '/' + str(round) + '/' + 'results'
    raceResults = get_api_data(roundRaces)['RaceTable']['Races']
    return raceResults


def get_pit_stops(request, round):
    roundPitStops = str(request.session['season'] - 1) + \
        '/' + str(round) + '/' + 'pitstops'
    pitStops = get_api_data(roundPitStops)['RaceTable']['Races']
    return pitStops


def get_lap_times(request, round):
    roundLapTimes = str(request.session['season'] - 1) + \
        '/' + str(round) + '/' + 'laps'
    lapTimes = get_api_data(roundLapTimes)['RaceTable']['Races']
    return lapTimes


def get_driver_standings(request, round):
    roundDriverStandings = str(request.session['season'] - 1) + \
        '/' + str(round) + '/' + 'driverStandings'
    driverStandings = get_api_data(roundDriverStandings)[
        'StandingsTable']['StandingsLists']
    return driverStandings


def get_constructor_standings(request, round):
    roundConstructorStandings = str(request.session['season'] - 1) + \
        '/' + str(round) + '/' + 'constructorStandings'
    constructorStandings = get_api_data(roundConstructorStandings)[
        'StandingsTable']['StandingsLists']
    return constructorStandings


def update_database():
    pass

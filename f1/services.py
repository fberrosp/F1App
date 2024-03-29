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
    if (data is up to date):
        get data from database unless its expired
        
    else: (not up to date)
        get data from api

        update database
        
    update cache
'''


def get_drivers(request):

    if False:  # data up to date

        # get data from database
        pass

    else:  # data not up to date

        # get data from api
        seasonDrivers = str(request.session['season']) + '/' + 'drivers'
        drivers = get_api_data(seasonDrivers)['DriverTable']['Drivers']

        # update database
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
                permanentNumber=driverNumber,
                code=driverCode,
                givenName=driver['givenName'],
                familyName=driver['familyName'],
                dateOfBirth=driver['dateOfBirth'],
                nationality=driver['nationality'],
                url=driver['url']
            )

            driver_data.save()

    # update cache
    # print(type(drivers))

    return drivers


def get_constructors(request):
    seasonConstructors = str(
        request.session['season']) + '/' + 'constructors'
    constructors = get_api_data(seasonConstructors)[
        'ConstructorTable']['Constructors']
    return constructors


def get_circuits(request):
    seasonCircuits = str(request.session['season']) + '/' + 'circuits'
    circuits = get_api_data(seasonCircuits)['CircuitTable']['Circuits']
    return circuits


def get_races(request):
    seasonRaces = str(request.session['season']) + '/' + 'races'
    races = get_api_data(seasonRaces)['RaceTable']['Races']
    return races


def get_qualifyings(request, round):
    roundQualifyings = str(
        request.session['season']) + '/' + str(round) + '/' + 'qualifying'
    qualifyings = get_api_data(roundQualifyings)[
        'RaceTable']['Races']
    return qualifyings


def get_race_results(request, round):
    roundRaces = str(request.session['season']) + \
        '/' + str(round) + '/' + 'results'
    raceResults = get_api_data(roundRaces)['RaceTable']['Races']
    return raceResults


def get_pit_stops(request, round):
    roundPitStops = str(request.session['season']) + \
        '/' + str(round) + '/' + 'pitstops'
    pitStops = get_api_data(roundPitStops)['RaceTable']['Races']
    return pitStops


def get_lap_times(request, round):
    roundLapTimes = str(request.session['season']) + \
        '/' + str(round) + '/' + 'laps'
    lapTimes = get_api_data(roundLapTimes)['RaceTable']['Races']
    return lapTimes


def get_driver_standings(request, round):
    roundDriverStandings = str(request.session['season']) + \
        '/' + str(round) + '/' + 'driverStandings'
    driverStandings = get_api_data(roundDriverStandings)[
        'StandingsTable']['StandingsLists']
    return driverStandings


def get_constructor_standings(request, round):
    roundConstructorStandings = str(request.session['season']) + \
        '/' + str(round) + '/' + 'constructorStandings'
    constructorStandings = get_api_data(roundConstructorStandings)[
        'StandingsTable']['StandingsLists']
    return constructorStandings

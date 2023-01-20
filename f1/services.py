import os
import requests
import pandas as pd
import time
import json

from bs4 import BeautifulSoup
from .models import Drivers, Qualifyings
from datetime import date
from collections import OrderedDict
from sqlalchemy import create_engine


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
    print(constructorStandings)
    return constructorStandings


def update_database():
    pass


def get_qualifying():
    all_qualifying = Qualifyings.objects.all().order_by('season')

    if all_qualifying:
        return all_qualifying
    else:
        qualifying_df = pd.DataFrame()

        for year in list(range(1983, 2023)):
            url = 'https://www.formula1.com/en/results.html/{}/races.html'
            response = requests.get(url.format(year))
            soup = BeautifulSoup(response.text, 'html.parser')

            yearLinks = []
            for page in soup.find_all('a', attrs={'class': "resultsarchive-filter-item-link FilterTrigger"}):
                pageLinks = page.get('href')
                if f'/en/results.html/{year}/races/' in pageLinks:
                    yearLinks.append(pageLinks)

            newUrl = 'https://www.formula1.com{}'
            yearQualifying_df = pd.DataFrame()

            for round, link in list(enumerate(yearLinks)):
                link = link.replace('race-result.html', 'starting-grid.html')

                raceResponse = requests.get(newUrl.format(link))
                df = pd.read_html(raceResponse.text)
                df = df[0]
                df['season'] = year
                df['round'] = round + 1

                driverName = df['Driver'].str.split()
                df['code'] = driverName.str[-1]
                df['forename'] = driverName.str[0]
                df['surname'] = driverName.str[1:-1]
                df['surname'] = [' '.join(map(str, l)) for l in df['surname']]

                df.drop(list(df.filter(regex='Unnamed')), axis=1, inplace=True)
                df.drop(['Driver'], axis=1, inplace=True)

                yearQualifying_df = pd.concat([yearQualifying_df, df])

            qualifying_df = pd.concat([qualifying_df, yearQualifying_df])

        qualifying_df.rename(columns={'Pos': 'grid', 'Car': 'car', 'Time': 'qualifyingTime',
                                      'No': 'number', 'round': 'race_round'}, inplace=True)

        engine = create_engine('sqlite:///db.sqlite3')
        qualifying_df.to_sql(Qualifyings._meta.db_table,
                             if_exists='replace', con=engine, index=True, index_label='qualifyId')

        all_qualifying = Qualifyings.objects.all().order_by('season')

        return all_qualifying

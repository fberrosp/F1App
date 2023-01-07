import os
import requests
import pandas as pd

from bs4 import BeautifulSoup
from .models import Drivers
from datetime import date


# method to get F1 API data from Ergast API


def get_api_data(api_endpoint):
    partialUrl = 'https://ergast.com/api/f1/{}.json'.format(api_endpoint)
    response = requests.get(partialUrl).json()
    #total = response['MRData']['total']
    #totalUrl = 'https://ergast.com/api/f1/{}.json?limit={}'.format(api_endpoint, total)
    #totalResponse = requests.get(totalUrl).json()

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


def update_database():
    pass


def get_circuits():
    circuits = get_api_data('circuits')['CircuitTable']['Circuits']
    return circuits


def get_constructors():
    constructors = get_api_data('constructors')[
        'ConstructorTable']['Constructors']
    return constructors


def get_drivers():
    '''
    # ----------------------Try cache------------------------------
    try:
        pass

    except:
        # -------------------Try API--------------------------
        try:
            # ---------------Update database--------------------
            pass
            # ---------------Update cache---------------------
        # -------------------Get database-----------------------
        except:
            pass
    '''
    drivers = get_api_data('drivers')['DriverTable']['Drivers']

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

    return all_drivers


def get_seasons():
    seasons = get_api_data('seasons')['SeasonTable']['Seasons']
    return seasons

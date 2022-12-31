import os
import requests
from .models import Drivers
from datetime import date

# method to get F1 API data from Ergast API


def get_api_data(api_endpoint):
    limitedUrl = 'https://ergast.com/api/f1/{}.json'.format(api_endpoint)
    response = requests.get(limitedUrl).json()
    total = response['MRData']['total']
    unlimitedUrl = 'https://ergast.com/api/f1/{}.json?limit={}'.format(
        api_endpoint, total)
    unlimitedResponse = requests.get(unlimitedUrl).json()

    return unlimitedResponse['MRData']


def get_drivers():
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

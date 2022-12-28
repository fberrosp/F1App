import os
import requests
from .models import Drivers
from datetime import date

# method to get F1 API data from Ergast API
def get_api_data(api_endpoint):
    limitedUrl = 'https://ergast.com/api/f1/{}.json'.format(api_endpoint)
    response = requests.get(limitedUrl).json()
    total = response['MRData']['total']
    unlimitedUrl = 'https://ergast.com/api/f1/{}?limit={}.json'.format(api_endpoint, total)
    #unlimitedResponse = requests.get(unlimitedUrl).json()

    return response['MRData']

def get_drivers():
    drivers = get_api_data('drivers')['DriverTable']['Drivers']
    print(drivers)
    
    for driver in drivers:
        print(driver)
        '''
        driver_data = Drivers(
            driverId = driver['driverId'],
            driverRef = driver['driverRef'],
            number = driver['permanentNumber'],
            code = driver['code'],
            forename = driver['givenName'],
            surename = driver['familyName'],
            dob = driver['dateOfBirth'],
            nationality = driver['nationality'],
            url = driver['url']
        )
        '''
        #driver_data.save()
        #all_drivers = Drivers.objects.all().order_by('driverId')
        all_drivers = drivers

    return all_drivers
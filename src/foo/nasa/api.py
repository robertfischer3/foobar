from urllib.parse import urljoin
from django.conf import settings
from datetime import datetime

import requests
from rest_framework import viewsets, permissions
from . import models

def get_api():
    return API(settings.NASA_API_SECRET)


class API:
    def __init__(self, api_key):
        self.api_key = api_key
        self.apod_url = 'planetary/apod'
        self.host = "https://api.nasa.gov/"


    def get_apod(self, date, hd=True):
        """Returns the JSON payload from the apod url.

        NASA API Documentation: https://api.nasa.gov/
        Requests Documentation: https://requests.readthedocs.io/en/master/user/quickstart/
        """
        # Use the `requests` library to call the API with the correct parameters and return the
        # JSON response.

        if date is not None:
            if not isinstance(date, (str, datetime)):
                raise TypeError('date parameter must be a string representing a date in YYYY-MM-DD format or a '
                                'datetime object.')

        if not isinstance(hd, bool):
            raise TypeError('hd parameter must be True or False (boolean).')

        if isinstance(date, datetime):
            date = date.strftime('%Y-%m-%d')

        url = urljoin(self.host, self.apod_url)

        r = requests.get(url,
                         params={
                             'api_key': self.api_key,
                             'date': date,
                             'hd': hd
                         })

        if r.status_code != 200:
            raise requests.exceptions.HTTPError(r.reason)

        else:
            self.__limit_remaining = r.headers['X-RateLimit-Remaining']
            return r.json()

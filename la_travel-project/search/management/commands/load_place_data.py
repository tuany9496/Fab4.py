from csv import DictReader
from datetime import datetime

from django.core.management import BaseCommand

from search.models import Place
from pytz import UTC


DATETIME_FORMAT = '%m/%d/%Y %H:%M'


ALREADY_LOADED_ERROR_MESSAGE = """
If you need to reload the place data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from load_place_data.csv into our Place model"

    def handle(self, *args, **options):
        if Place.objects.exists():
            print('Place data already loaded...exiting.')
            print(ALREADY_LOADED_ERROR_MESSAGE)
            return

        print("Loading place data for search")
        for row in DictReader(open('./place_data.csv')):

            place = Place()
            place.companyName = row['Company Name']
            place.addressName = row['Address']
            place.cityName = row['City']
            place.stateName = row['State']
            place.zipName = row['ZIP Code']
            place.countyName = row['County']
            place.neigborhoodName = row['Neighborhood']
            place.phoneNumber = row['Phone Number Combined']
            place.websiteLink = row['Website']
            place.SICDescription = row['Primary SIC Description']
            place.SICCode = row['SIC Code 1']
            place.CuisineCodeDescription = row['Cuisine Code Description']
            place.TuesdayOpen = row['Tuesday Open']
            place.TuesdayClose = row['Tuesday Close']
            place.WednesdayOpen = row['Wednesday Open']
            place.WednesdayClose = row['Wednesday Close']
            place.ThursdayOpen = row['Thursday Open']
            place.ThurdayClose = row['Thursday Close']
            place.FridayOpen = row['Friday Open']
            place.FridayClose = row['Friday Close']
            place.SatursdayOpen = row['Saturday Open']
            place.SaturdayClose = row['Saturday Close']
            place.SundayOpen = row['Sunday Open']
            place.SundayClose = row['Sunday Close']
            place.Twitter = row['Twitter']
            place.Facebook = row['Facebook']
            place.WhatTypes = row['WhatTypes']
            place.save()

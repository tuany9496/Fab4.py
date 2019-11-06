from django.shortcuts import render
from .forms import SearchForms
import json
import requests
import urllib.request
from django.http import HttpResponse
from .models import Place
from geopy.geocoders import Nominatim

# Create your views here.
def home (request):
# test
    # if request.method =='POST':
    #     filled_form = SearchForms(request.POST)
    #     if filled_form.is_valid():
    #         note = 'Searched Results for WHERE: %s WHEN: %s WHAT: %s' %(filled_form.form.cleaned_data['Where'], ['When'], ['What'])
    #         new_form = SearchForms()
    #         return render (request, 'search/searched.html', {'SearchForms': new_form, 'note':note})
    # else:
    #     form = SearchForms()
    #     return render (request, 'search/home.html', {'searchforms': form})
    #

   form = SearchForms()
   return render (request, 'search/home.html', {'searchforms':form})
def searched (request):
    if request.method =='POST':
        filled_form = SearchForms(request.POST)
        if filled_form.is_valid():

            #%(filled_form.cleaned_data['Where'], filled_form.cleaned_date['When'], filled_form.cleaned_date['What'],)
            #new_form = SearchForms()
            city = (filled_form.cleaned_data['Where'])
            source = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=139a58208c47093f3371eff8a42f640c'
            #source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q ='+ city +'&appid=139a58208c47093f3371eff8a42f640c').read()

            r = requests.get(source.format(city)).json()

            city_weather = {
                'city' : city,
                'temperature' : r['main']['temp'],
                'description' : r['weather'][0]['description'],
                'icon' : r['weather'][0]['icon'],
            }
            #print(city_weather)

            #places = Place.objects.all()
            if filled_form.cleaned_data['What'] == 'Sightseeing':
                places = Place.objects.all().filter(cityName = city, WhatTypes = 'Sightseeing')

            elif filled_form.cleaned_data['What'] == 'Restaurants':
                places = Place.objects.all().filter(cityName = city, WhatTypes = 'Restaurants')
            elif filled_form.cleaned_data['What'] == 'Hotels & Motels':
                places = Place.objects.all().filter(cityName = city, WhatTypes= 'Hotels')
                #places = Place.objects.all().filter(cityName = city, SICDescription = filled_form.cleaned_data['What'])




            #sunrise and Sunset
            location = Nominatim(user_agent="my-application").geocode(city)
            r = requests.get('https://api.sunrise-sunset.org/json', params={'lat': location.latitude, 'lng': location.longitude}).json()['results']

            note = 'HERE: %s    WHEN: %s to  %s      WHAT: %s    Current Weather: %s %s      Sunrise %s UTC  Sunset %s UTC ' %(filled_form.cleaned_data['Where'], filled_form.cleaned_data['WhenFr'], filled_form.cleaned_data['WhenTo'], filled_form.cleaned_data['What'], city_weather['temperature'], city_weather['description'], r['sunrise'],r['sunset'] )
            return render (request, 'search/searched.html', {'note': note, 'places': places})
            #return render (request, 'search/searched.html', {'places': places})
            #return render (request, 'search/searched.html', {'SearchForms': new_form, 'note':note})
    else:
        form = SearchForms()
        return render (request, 'search/searched.html')
def map (request):
    return render (request, 'search/map.html')

def weather(request):
    if request.method == 'POST':
        city = request.POST['city']
        ''' api key might be expired use your own api_key
            place api_key in place of appid ="your_api_key_here "  '''

        # source contain JSON data from API

        source = urllib.request.urlopen(
            'http://api.openweathermap.org/data/2.5/weather?q ='
                    + city + '&appid = 139a58208c47093f3371eff8a42f640c').read()

        # converting JSON data to a dictionary
        list_of_data = json.loads(source)

        # data for variable list_of_data
        data = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ' '
                        + str(list_of_data['coord']['lat']),
            "temp": str(list_of_data['main']['temp']) + 'k',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
        }
        print(data)
    else:
        data ={}
    return render(request, "search/searched.html", data)

from django.shortcuts import render
import requests

from WeatherApp.settings import API_KEY
from weather_forecast.models import City
from .forms import CityForm


def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&lang=ru&appid=' + API_KEY
    city_list = []

    if (request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    for city in City.objects.all():
        res = requests.get(url.format(city)).json()
        city_info = {
            'city': city.name,
            'temp': res["main"]["temp"],
            'description': res['weather'][0]['description'],
            'icon': res["weather"][0]["icon"],
        }

        city_list.append(city_info)

    context = {
        'title': 'Прогноз погоды',
        'city_list': city_list,
        'form': form,
    }

    return render(request, 'weather_forecast/index.html', context=context)

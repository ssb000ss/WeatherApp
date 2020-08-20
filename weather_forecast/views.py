from django.shortcuts import render


def index(request):
    context = {
        'title': 'Прогноз погоды',
    }
    return render(request, 'weather_forecast/index.html', context=context)

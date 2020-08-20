from django.forms import ModelForm, TextInput

from weather_forecast.models import City


class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {'name': TextInput(attrs={
            'class': 'form-control',
            'name': 'city',
            'id': 'city',
            'place-holder': ' Введите название города',
        })}

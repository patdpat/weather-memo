from rest_framework import serializers
from .models import Weather

class WeatherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Weather
        fields = ('added_date', 'text', 'temperature', 'descrip', 'icon', 'result', 'pm')
from rest_framework import viewsets

from .serializers import WeatherSerializer
from .models import Weather

class WeatherViewSet(viewsets.ModelViewSet):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer
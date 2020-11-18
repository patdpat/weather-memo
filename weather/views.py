from django.shortcuts import render, redirect
import requests
from .models import WH
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

def create_url(w_text):
    head = 'https://api.waqi.info/feed/'
    tail = '/?token=d66c4f6d02ad82aee0b65500bb015164280ac4a8'
    url = head + w_text+ tail
    return url

# Create your views here.
def list_w(request):
    weather = WH.objects.all().order_by('-added_date')
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=c812a2a33fd7892739ba5b4c09b2e499'

    for w in weather:
        r = requests.get(url.format(w.text)).json()
        city_weather = {'temperature': r['main']['temp'],
                    'description': r['weather'][0]['description'],
                    'icon': r['weather'][0]['icon'],
                    }
        r2 = requests.get(create_url(w.text)).json()
        city_weather['pm']= r2['data']['aqi']
        #append result part
        if float(city_weather['temperature']) < 13 or float(city_weather['temperature'])>31:
            city_weather['result']='Today is not safe for outdoor'
        else:
            city_weather['result']='Today is safe for outdoor'
            
        
        WH.objects.filter(text=w.text).update(temperature=city_weather['temperature'], descrip=city_weather['description'], icon=city_weather['icon'], result=city_weather['result'],pm=city_weather['pm'])

    return render(request, 'weather/index.html', {'weather': weather})

@csrf_exempt
def add_city(request):
    current_date = timezone.now()
    city = request.POST["content"]
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=c812a2a33fd7892739ba5b4c09b2e499'

    r = requests.get(url.format(city)).json()

    city_weather= {'city': city,
            'temperature': r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
    
                  }
    r2 = requests.get(create_url(city)).json()
    city_weather['pm']= r2['data']['aqi']
    #append result part
    if float(city_weather['temperature']) < 13 or float(city_weather['temperature'])>31:
            city_weather['result']='Today is not safe for outdoor'
    else:
        city_weather['result']='Today is safe for outdoor'
    WH.objects.create(added_date=current_date, text=city_weather['city'], temperature=city_weather['temperature'], descrip=city_weather['description'], icon=city_weather['icon'], result=city_weather['result'],pm=city_weather['pm'])
   
    return redirect('list_w')

@csrf_exempt
def delete_city(request,pk):
    WH.objects.filter(id=pk).delete()
    return redirect('list_w')

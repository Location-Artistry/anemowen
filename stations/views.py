from abc import abstractclassmethod
from django.http import response
from requests.api import request
from stations.models import Stations
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Stations
from .forms import AddForm
from django.urls import reverse_lazy
import requests


class HomeView(ListView):
    model = Stations
    template_name = 'home.html'

class AddStationView(CreateView):
    model = Stations
    form_class = AddForm
    template_name = "add_station.html"

class StationDetailView(DetailView):
    model = Stations
    template_name = "station_details.html"

class UpdateStationView(UpdateView):
    model = Stations
    template_name = 'update_stations.html'
    fields = ['site_id','label']

class DeleteStationView(DeleteView):
    model = Stations
    template_name = 'delete_station.html'
    success_url = reverse_lazy('home')

class StationDetailViewMap(DetailView):
    model = Stations
    template_name = "station_details_map.html"

class HomeMapView(ListView):
    model = Stations
    template_name = 'home_map.html'

class StationList(ListView):
    model = Stations
    template_name = 'station_list.html'

def StationListFunc(request):
    model = Stations
    queryset = Stations.objects.all()
    return render(request, 'station_list.html', {'response': queryset })

def nhbpSensorMap(request):
    response = requests.get('https://purpleairwidget.firebaseapp.com/purpleAirData/44439,41995,41993,42005,41907,97713,97553,97743,97679,91997,97559,95527,92021').json()
    return render(request, 'nhbp_sensor_map.html', {'response':response} )

def dashboard(request):
    liveStations = requests.get('https://purpleairwidget.firebaseapp.com/purpleAirData/44439,41995,41993,42005,41907,97713,97553,97743,97679,91997,97559,95527,92021').json()
    
    def getTime(t):
        totSec = t['seconds'] + (t['minute'] * 60) + (t['hour'] * 3600) + (t['day'] * 86400)
        return totSec

    def getSummary(data):
        avgPM25, avgAQI, avgSec = 0, 0, 0
        for x in data:
            avgPM25 = avgPM25 + x['properties']['PM2_5Value']
            avgAQI = avgAQI + x['properties']['AQI']
            avgSec = avgSec + getTime(x['properties']['formatSinceSeen'])
        avgPM25 = round(avgPM25 / len(data), 2)
        avgAQI = round(avgAQI / len(data))
        avgSec = avgSec / len(data)
        timeMin = round(avgSec / 60, 2)
        return [avgPM25, avgAQI, timeMin]

    summary = getSummary(liveStations['features'])
    avgPM25, avgAQI, timeMin = summary[0], summary[1], summary[2]
    stationData = Stations.objects.all()
    stationCount = Stations.objects.all().count()
    context = {'response': liveStations, 'stationData': stationData, 'stationCount': stationCount, 'avgPM25': avgPM25, 'avgAQI': avgAQI, 'timeMin': timeMin }
    return render(request, 'sensor_dashboard.html', context)


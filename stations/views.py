from django.http import response
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

def getLiveStations(request):
    response = requests.get('https://purpleairwidget.firebaseapp.com/purpleAirData/44439,41995,41993,42005,41907,97713,97553,97743,97679,91997,97559,95527,92021').json()
    return render(request, 'get_data.html', {'response':response} )

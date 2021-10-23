from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from stations.models import Stations
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

class LandingView(ListView):
    model = Stations
    template_name = 'landing.html'
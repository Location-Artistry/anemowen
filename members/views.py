from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from members.forms import EditProfileForm
from stations.models import Stations
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'user_edit.html'
    success_url = reverse_lazy('landing') 
    
    def get_object(self):
        return self.request.user

class LandingView(ListView):
    model = Stations
    template_name = 'landing.html'
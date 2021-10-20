from django.urls import path
from .views import LandingView, UserRegisterView
from . import views

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('', LandingView.as_view(), name='landing'),
   
]
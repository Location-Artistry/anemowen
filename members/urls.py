from django.urls import path
from . import views
from .views import LandingView, UserEditView, UserRegisterView


urlpatterns = [
    #path('', HomeView.as_view(), name='index'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('', LandingView.as_view(), name='landing'),
    path('user_edit/', UserEditView.as_view(), name='user-edit'),
   
]
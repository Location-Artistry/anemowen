from stations.forms import AddForm
from django.urls import path
from . import views
from .views import AddStationView, HomeView, StationDetailView, UpdateStationView, DeleteStationView, StationDetailViewMap, HomeMapView

urlpatterns = [
    # path('',views.home, name="home")
    path('', HomeView.as_view(), name='home'),
    path('station/<int:pk>', StationDetailView.as_view(), name='station-detail'),
    path('add_station/', AddStationView.as_view(), name='add_station'), 
    path('station/edit/<int:pk>', UpdateStationView.as_view(), name='update_station'),
    path('station/<int:pk>/remove', DeleteStationView.as_view(), name='delete_station'),
    path('stationmap/<int:pk>', StationDetailViewMap.as_view(), name='station-detail-map'),
    path('map/', HomeMapView.as_view(), name='home_map'),
    path('data', views.getLiveStations, name='get_data'),      
]
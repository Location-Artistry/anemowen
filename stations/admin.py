#from django.contrib import admin
from django.contrib.gis import admin
from .models import Stations
from leaflet.admin import LeafletGeoAdmin

admin.site.register(Stations, admin.OSMGeoAdmin)
#admin.site.register(Stations, LeafletGeoAdmin)


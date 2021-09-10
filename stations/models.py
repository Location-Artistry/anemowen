#from django.db import models
from django.contrib.gis.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.gis import forms

class Stations(models.Model):
    site_id = models.IntegerField(null=True)
    label = models.CharField(max_length=32,null=True)
    flagged_high = models.IntegerField(null=True)
    version = models.CharField(max_length=12,null=True)
    wifisignal = models.CharField(max_length=12,null=True)
    pm2_5value = models.CharField(max_length=8,null=True)
    pm2_5_1hour = models.FloatField(null=True)
    pm2_5_24hour = models.FloatField(null=True)
    pm2_5_1week = models.FloatField(null=True)
    sensordiff = models.CharField(max_length=8,null=True)
    aqi = models.IntegerField(null=True)
    aqitext = models.CharField(max_length=48,null=True)
    aqi1hour = models.IntegerField(null=True)
    aqi1hourtext = models.CharField(max_length=48,null=True)
    aqi24hour = models.IntegerField(null=True)
    aqi24hourtext = models.CharField(max_length=48,null=True)
    aqi1week = models.IntegerField(null=True)
    aqi1weektext = models.CharField(max_length=48,null=True)
    geom = models.PointField(srid=4326)
    
    def __str__(self):
        return str(self.site_id) + ' | ' + str(self.label)
    
    def get_absolute_url(self):
        return reverse('station-detail',args=[str(self.id)] )


# Auto-generated `LayerMapping` dictionary for Stations model
stations_mapping = {
    'site_id': 'ID',
    'label': 'label',
    'flagged_high': 'flagged_high',
    'version': 'version',
    'wifisignal': 'WiFiSignal',
    'pm2_5value': 'PM2_5Value',
    'pm2_5_1hour': 'PM2_5_1hour',
    'pm2_5_24hour': 'PM2_5_24hour',
    'pm2_5_1week': 'PM2_5_1week',
    'sensordiff': 'sensorDiff',
    'aqi': 'AQI',
    'aqitext': 'AQIText',
    'aqi1hour': 'AQI1Hour',
    'aqi1hourtext': 'AQI1HourText',
    'aqi24hour': 'AQI24Hour',
    'aqi24hourtext': 'AQI24HourText',
    'aqi1week': 'AQI1Week',
    'aqi1weektext': 'AQI1WeekText',
    'geom': 'POINT',
}
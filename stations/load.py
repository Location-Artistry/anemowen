import os
from django.contrib.gis.utils import LayerMapping
from .models import Stations

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


def run(verbose=True):
    stationPath = os.path.abspath(os.path.join(os.path.dirname(__file__),'data','stations.geojson'),)
    lm = LayerMapping(Stations, stationPath, stations_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)

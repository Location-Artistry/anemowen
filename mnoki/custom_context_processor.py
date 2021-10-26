from stations.models import Stations
import requests

from stations.views import StationList

def station_renderer(request):
    stationsList = Stations.objects.all()
    stationCount = len(stationsList)
    return { 'allStations': stationsList, 'stationCount': stationCount }

# static dataFile for landinf page test
def dashboardCP(request):
    import json
    import os
    stationPath = os.path.abspath(os.path.join(os.path.dirname(__file__),'data','testData.geojson'),)
    f = open(stationPath)
    liveStations = json.load(f)
    
    def getTime(t):
        totSec = t['seconds'] + (t['minute'] * 60) + (t['hour'] * 3600) + (t['day'] * 86400)
        return totSec

    def getSummary(data):
        avgPM25, avgAQI, avgSec, staNotSeen, staNum = 0, 0, 0, 0, len(data)
        for x in data:
            avgPM25 = avgPM25 + x['properties']['PM2_5Value']
            avgAQI = avgAQI + x['properties']['AQI']
            timeSec = getTime(x['properties']['formatSinceSeen'])
            avgSec = avgSec + timeSec
            staNotSeen = (staNotSeen+1) if timeSec > 3600 else staNotSeen
        
        avgPM25 = round(avgPM25 / len(data), 2)
        avgAQI = round(avgAQI / len(data))
        avgSec = avgSec / len(data)
        timeMin = round(avgSec / 60, 2)
        return {'avgPM25': [avgPM25,'STATION Avg PM2.5', (f'Average of PM2.5 from {staNum} NHBP Sensors')], 'avgAQI':[avgAQI,'STATION Avg AQI',(f'Average Air Quality Index from {staNum} NHBP Sensors')]}
    
    sum = getSummary(liveStations['features'])
    stationData = Stations.objects.all()
    stationCount = Stations.objects.all().count()
    return {'liveStationsCP': liveStations, 'stationDataCP': stationData, 'stationCountCP': stationCount, 'sumCP':sum}
    
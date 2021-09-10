# from django import forms
from django.contrib.gis import forms
from django.forms import fields, widgets
from .models import Stations



class AddForm(forms.ModelForm):
    class Meta:    
        model = Stations
        fields = ('site_id','label','geom')
        widgets = {
            'site_id': forms.NumberInput(attrs={'class':'form-control'}),
            'label': forms.TextInput(attrs={'class':'form-control'}),
            'geom': forms.OSMWidget(attrs={'map_height': 600,'map_width': 1200,'default_lat':43.5,'default_lon':-85,'default_zoom':7})
        }
  
           

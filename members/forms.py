from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.db.models import fields
from .models import Profile

class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email')
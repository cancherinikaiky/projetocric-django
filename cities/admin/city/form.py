from django.contrib import admin
from django import forms

from cities.models import City, Route

class CityAdminForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = '__all__'
        widgets = {
            'authors': forms.CheckboxSelectMultiple
        }
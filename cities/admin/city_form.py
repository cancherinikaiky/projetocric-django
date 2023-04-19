from django import forms

from cities.models import Route

class CityAdminForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = '__all__'
        widgets = {
            'authors': forms.CheckboxSelectMultiple
        }
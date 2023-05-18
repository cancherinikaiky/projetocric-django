from django import forms

from cities.models import City
from projetocric.utilities import validate_field

class CityAdminForm(forms.ModelForm):
    class Meta:
        model = City
        fields = '__all__'
        widgets = {
            'routes': forms.CheckboxSelectMultiple,
            'points': forms.CheckboxSelectMultiple
        }

    def clean_name(self):
        return validate_field(self, City, 'name', 'NOME já cadastrado!')
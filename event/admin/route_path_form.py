from django import forms
from event.models.route_path import RoutePath

from projetocric.utilities import validate_field

class RoutePathForm(forms.ModelForm):
    class Meta:
        model = RoutePath
        fields = '__all__'

    def clean_name(self):
        return validate_field(self, RoutePath, 'name', 'NOME já cadastrado')
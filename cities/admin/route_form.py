from django import forms
from colorfield.widgets import ColorWidget

from projetocric.utilities import validate_field


from cities.models import Route

class RouteAdminForm(forms.ModelForm):
    formfield_overrides = {
        ColorWidget: {'widget': ColorWidget},
    }

    def clean_name(self):
        return validate_field(self, Route, 'name', 'NOME da rota já cadastrada!')
    
    def clean_id_route(self):
        return validate_field(self, Route, 'id_route', 'ID da rota já cadastrado!')
    
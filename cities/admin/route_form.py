from django import forms
from colorfield.widgets import ColorWidget


from cities.models import Route

class RouteAdminForm(forms.ModelForm):
    formfield_overrides = {
        ColorWidget: {'widget': ColorWidget},
    }

    def clean_name(self):
        name = self.cleaned_data['name']
        if Route.objects.filter(name=name).exists():
            raise forms.ValidationError('NOME já registrado')
        return name
    
    def clean_id_route(self):
        id_route = self.cleaned_data['id_route']
        if Route.objects.filter(id_route=id_route).exists():
            raise forms.ValidationError('ID_ROUTE já registrado')
        return id_route
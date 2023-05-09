from django import forms
from colorfield.widgets import ColorWidget


from cities.models import Route

class RouteAdminForm(forms.ModelForm):
    formfield_overrides = {
        ColorWidget: {'widget': ColorWidget},
    }
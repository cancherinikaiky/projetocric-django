from django import forms
from event.models.route_path import RoutePath

class RoutePathForm(forms.ModelForm):
    class Meta:
        model = RoutePath
        fields = '__all__'

    def clean_name(self):
        name = self.cleaned_data['name']
        if RoutePath.objects.filter(name=name).exists():
            raise forms.ValidationError('NOME já registrado')
        return name
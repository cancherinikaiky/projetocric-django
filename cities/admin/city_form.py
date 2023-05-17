from django import forms

from cities.models import City

class CityAdminForm(forms.ModelForm):
    class Meta:
        model = City
        fields = '__all__'
        widgets = {
            'routes': forms.CheckboxSelectMultiple,
            'points': forms.CheckboxSelectMultiple
        }

    def clean_name(self):
        name = self.cleaned_data['name']
        if City.objects.filter(name=name).exists():
            raise forms.ValidationError('NOME já registrado')
        return name
from django.contrib import admin
from .models import Route, City
from django import forms

class RouteAdminForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = '__all__'
        widgets = {
            'authors': forms.CheckboxSelectMultiple
        }

class RouteAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'id_route', 'polilyne')
    list_display_links = ('id', 'name')


class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'visible')
    list_display_links = ('id', 'name')
    form = RouteAdminForm


admin.site.register(Route, RouteAdmin)
admin.site.register(City, CityAdmin)
from django.contrib import admin
from .models import Route, City
from django import forms
    
class CityAdminForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = '__all__'
        widgets = {
            'authors': forms.CheckboxSelectMultiple
        }

class RouteAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'id_route', 'active', 'polilyne')
    list_display_links = ('id', 'name', 'id_route', 'polilyne')
    readonly_fields = ('polilyne',)


class CityAdmin(admin.ModelAdmin):
    form = CityAdminForm
    list_display = ('id', 'name', 'visible')
    list_display_links = ('id', 'name')

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "routes":
            kwargs["queryset"] = Route.objects.filter(active=True)
        return super().formfield_for_manytomany(db_field, request, **kwargs)


admin.site.register(Route, RouteAdmin)
admin.site.register(City, CityAdmin)
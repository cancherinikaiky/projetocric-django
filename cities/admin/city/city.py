from django.contrib import admin

from cities.models import City, Route
from .form import CityAdminForm


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    form = CityAdminForm
    list_display = ('id', 'name', 'visible')
    list_display_links = ('id', 'name')

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "routes":
            kwargs["queryset"] = Route.objects.filter(active=True)
        return super().formfield_for_manytomany(db_field, request, **kwargs)
from django.contrib import admin
from .models import Route
from .models import City

class RouteAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'id_route', 'polilyne')
    list_display_links = ('id', 'name')


class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'visible')
    list_display_links = ('id', 'name')

admin.site.register(Route, RouteAdmin)
admin.site.register(City, CityAdmin)
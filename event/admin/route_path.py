from django.contrib import admin
from event.models.route_path import RoutePath
from .route_path_form import RoutePathForm

class RoutePathAdmin(admin.ModelAdmin):
    form = RoutePathForm
    list_display = ('name', 'route', 'time', 'departure_location',)
    list_display_links = ('name', 'route', 'time', 'departure_location',)
    ordering = ['name']

admin.site.register(RoutePath, RoutePathAdmin)
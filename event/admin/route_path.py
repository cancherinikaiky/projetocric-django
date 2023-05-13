from django.contrib import admin
from event.models.route_path import RoutePath

class RoutePathAdmin(admin.ModelAdmin):
    list_display = ('name', 'route')
    list_display_links = ('name', 'route')
    ordering = ['name']

admin.site.register(RoutePath, RoutePathAdmin)
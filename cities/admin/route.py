from django.contrib import admin

from cities.models import Route
from cities.admin import RouteAdminForm

class RouteAdmin(admin.ModelAdmin):
    form = RouteAdminForm
    list_display = ('id', 'name', 'id_route', 'active', 'polyline')
    list_display_links = ('id', 'name', 'id_route', 'polyline')
    readonly_fields = ('polyline',)


admin.site.register(Route, RouteAdmin)
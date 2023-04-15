from django.contrib import admin
from cities.models import Route

class RouteAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'id_route', 'active', 'polilyne')
    list_display_links = ('id', 'name', 'id_route', 'polilyne')
    readonly_fields = ('polilyne',)


admin.site.register(Route, RouteAdmin)
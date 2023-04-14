from django.contrib import admin
from .models import Home
from cities.models.city import City

from django.urls import reverse
from django.utils.html import format_html


class HomeAdmin(admin.ModelAdmin):
    # list_display = ('id', 'id_city', 'name_city', 'banner_photo_city', 'edit_city_link')

    # readonly_fields = ('id', 'name_city', 'banner_photo_city', 'edit_city_link')

    list_display = ('id', 'city', 'edit_city_link')


    def edit_city_link(self, obj):
         url = reverse('admin:cities_city_change', args=[obj.city.pk])
         return format_html('<a href="{}"> Editar cidade</a>', url)

    edit_city_link.short_description = 'Editar Cidade'


admin.site.register(Home, HomeAdmin)

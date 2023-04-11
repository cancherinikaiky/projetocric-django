from django.contrib import admin
from .models import Home
from cities.models.city import City

from django.urls import reverse
from django.utils.html import format_html


class HomeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_city', 'banner_photo_city')
    list_display_links = ('name_city',)


admin.site.register(Home, HomeAdmin)

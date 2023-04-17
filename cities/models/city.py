from django.db import models
from .route import Route
# from .city_manager import CityManager

class City(models.Model):
    PATH_IMAGES_CITIES_BANNER = 'cities/images/banner_photos/%Y/%m/%d'
    name = models.CharField(max_length=100, verbose_name='Nome')
    lat = models.CharField(max_length=50, default='-29.95')
    lng = models.CharField(max_length=50, default='-51.64')
    banner_photo = models.ImageField(upload_to=PATH_IMAGES_CITIES_BANNER, verbose_name="Imagem do Banner")
    routes = models.ManyToManyField(Route, blank=True, null=True)
    visible = models.BooleanField(default=False, verbose_name='Visível')

    # objects = CityManager()

    def __str__(self) -> str:
        return self.name
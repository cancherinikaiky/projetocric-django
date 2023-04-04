from django.db import models
from .route import Route

class City(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome')
    banner_photo = models.ImageField(upload_to='banner_img/%Y/%m/%d', verbose_name="Imagem do Banner")
    visible = models.BooleanField(default=False, verbose_name='Visível')
    routes = models.ManyToManyField(Route)

    def __str__(self) -> str:
        return self.name
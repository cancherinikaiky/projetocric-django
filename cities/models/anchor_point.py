from django.db import models
from cities.models.address_point import Address
from cities.models.category_point import Category

class AnchorPoint(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome')
    lat = models.CharField(max_length=20, verbose_name='Latitude')
    lng = models.CharField(max_length=20, verbose_name='Longitude')
    business_hours = models.CharField(max_length=120, verbose_name='Horário de funcionamento')
    phone = models.CharField(max_length=20, default='(51) ', verbose_name='Telefone')
    address = models.ForeignKey(Address, on_delete=models.CASCADE, verbose_name='Endereço')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Tipo do comérico')
    active = models.BooleanField(default=False, verbose_name="Ativo")

    def __str__(self):
        return self.name
    
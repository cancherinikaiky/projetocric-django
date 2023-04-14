from django.db import models
from cities.models import City

class Home(models.Model):
    id = models.AutoField(primary_key=True)
    city = models.OneToOneField(City, on_delete=models.CASCADE)
    # id_city = models.CharField(max_length=100, null=True, blank=True)
    # city = models.ForeignKey(City, on_delete=models.CASCADE)
    # name_city = models.CharField(max_length=100, verbose_name='Nome da Cidade', editable=False)
    # banner_photo_city = models.URLField(editable=False, default=None, verbose_name='Imagem do Banner')


    # def save(self, *args, **kwargs):
    #     self.id_city = self.city.id
    #     self.name_city = self.city.name
    #     self.banner_photo_city = self.city.banner_photo.url
    #     super().save(*args, **kwargs)


    # def __str__(self):
    #     return self.name_city
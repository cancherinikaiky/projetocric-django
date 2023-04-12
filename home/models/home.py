from django.db import models
from cities.models import City

class Home(models.Model):
    id = models.AutoField(primary_key=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    name_city = models.CharField(max_length=100, verbose_name='Nome da Cidade', editable=False)
    banner_photo_city = models.URLField(editable=False, default=None, verbose_name='Imagem do Banner')


    def save(self, *args, **kwargs):
        self.name_city = self.city.name
        self.banner_photo_city = self.city.banner_photo.url
        super().save(*args, **kwargs)

    # @staticmethod
    # def sync_cities():
    #     cities = City.objects.filter(visible=True)
    #     for city in cities:
    #         home, created = Home.objects.get_or_create(city=city)
    #         if created:
    #             home.name_city = city.name
    #             home.banner_photo_city = city.banner_photo.url
    #             home.save()

    def __str__(self):
        return self.name_city
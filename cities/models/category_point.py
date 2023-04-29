from django.db import models

class Category(models.Model):
    PATH_IMAGES_CATEGORIES = 'cities/categories/photos/%Y/%m/%d'
    name = models.CharField(max_length=50, verbose_name='Nome')
    image = models.FileField(upload_to=PATH_IMAGES_CATEGORIES)

    def __str__(self):
        return self.name
    
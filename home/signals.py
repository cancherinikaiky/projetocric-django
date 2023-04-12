from .models import Home
from cities.models import City

from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=City)
def create_home(sender, instance, created, **kwargs):
    if created and instance.visible:
        home = Home(city=instance, name_city=instance.name)
        home.save()

@receiver(post_save, sender=City)
def update_home(sender,instance, **kwargs):
    if instance.visible:
        home = Home.objects.filter(city_id=instance.id).first()
        if home:
            home.name_city = instance.name
            home.save()
        else: 
            Home.objects.create(city_id=instance.id, name_city=instance.name)
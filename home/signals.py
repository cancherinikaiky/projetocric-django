from .models import Home
from cities.models import City

from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=City)
def create_home(sender, instance, created, **kwargs):
    if created:
        home = Home(city=instance, name_city=instance.name)
        home.save()
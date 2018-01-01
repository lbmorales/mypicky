from django.db import models
from django.db.models.signals import pre_save
from .utils import unique_slug_generator
from .validators import validate_category

class RestaurantLocation(models.Model):
    name        = models.CharField(max_length=120)
    location    = models.CharField(max_length=120, null=True, blank=True)
    category    = models.CharField(max_length=120, null=True, blank=True, validators=[validate_category])
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    slug        = models.SlugField(null=True, blank=True)

    def __str__(self):
        return ('%s - %s ')% (self.name, self.category)

def restaurant_location_pre_save_receiver(sender, instance, *args, **kwargs):
    if instance.category:
        instance.category = instance.category.capitalize()
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
    print(instance.__dict__)

pre_save.connect(restaurant_location_pre_save_receiver, sender=RestaurantLocation)
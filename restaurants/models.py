from django.db import models

from django.db import models
from diet.models import DietaryOption
from django.contrib.gis.db import models as gis_models
from address.models import AddressField
from phonenumber_field.modelfields import PhoneNumberField


class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    location = gis_models.PointField(geography=True, srid=4326)  # WGS 84 (SRID 4326)
    address = AddressField()  # Using django-localflavor for address validation
    images = models.ImageField(upload_to='restaurant_images/')
    description = models.TextField(blank=True)
    phone_number = PhoneNumberField(blank=True)
    website = models.URLField(blank=True)
    dietary_options = models.ManyToManyField(DietaryOption, related_name='restaurants')

    def __str__(self):
        return self.name

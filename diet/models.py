from django.db import models
from colorfield.fields import ColorField


class DietaryOption(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='icons/')
    color_light = ColorField(default='#000000', help_text='Backgound color for light mode')
    color_dark = ColorField(default='#FFFFFF', help_text='Backgound color for dark mode')

    def __str__(self):
        return self.name

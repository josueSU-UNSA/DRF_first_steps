from django.db import models

# Create your models here.
class Drink(models.Model):
    name=models.CharField(max_length=255)
    description=models.CharField(max_length=510)

    def __str__(self):
        return f'{self.name}'
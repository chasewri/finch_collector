from django.db import models

# Create your models here.
class Finch(models.Model):
    name = models.CharField(max_length=100, unique=True)
    favorite_joke = models.CharField(max_length=300)
    image = models.CharField(max_length=200)
    birthday = models.DateField()
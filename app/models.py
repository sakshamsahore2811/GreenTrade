from django.db import models

# Create your models here.

class Item(models.Model):
    id = models.CharField(primary_key=True,max_length=200)
    name = models.CharField(max_length=75)
    description = models.CharField(max_length=300)
    price = models.CharField(max_length=50)
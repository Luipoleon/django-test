from django.db import models

# Create your models here.

class Menu(models.Model):
    name = models.CharField(max_length = 100)
    cousine = models.CharField(max_length = 100)
    price = models.IntegerField()
    
from django.db import models
from common.models import Country, State, City

class Store(models.Model):

    name = models.CharField(
        max_length=1024,
        verbose_name='Name'
    )

    social_name = models.CharField(
        max_length=1024,
        verbose_name='Social Name'
    )

    country = models.ForeignKey(
        Country, 
        on_delete=models.CASCADE, 
        verbose_name='Country'
    )

    state = models.ForeignKey(
        State, 
        on_delete=models.CASCADE, 
        verbose_name='State'
    )

    city = models.ForeignKey(
        City, 
        on_delete=models.CASCADE, 
        verbose_name='City'
    )

    adress = models.CharField(
        max_length=1024,
        verbose_name='Adress'
    )
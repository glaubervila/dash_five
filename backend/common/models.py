from django.db import models


class Country(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name='Name'
    )
    initials = models.CharField(
        max_length=5,
        verbose_name='Initials'
    )

class State(models.Model):
    # Relation With Contry
    contry = models.ForeignKey(
        Country, 
        on_delete=models.CASCADE, 
        verbose_name='Contry'
    )
    name = models.CharField(
        max_length=256,
        verbose_name='Name'
    )
    uf = models.CharField(
        max_length=5,
        verbose_name='UF'
    )

class City(models.Model):
    state = models.ForeignKey(
        State, 
        on_delete=models.CASCADE, 
        verbose_name='State'
    )
    name = models.CharField(
        max_length=256,
        verbose_name='Name'
    )
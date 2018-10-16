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

    def __str__(self):
        return self.name

class State(models.Model):
    # Relation With Contry
    country = models.ForeignKey(
        Country, 
        on_delete=models.CASCADE, 
        verbose_name='Country'
    )
    name = models.CharField(
        max_length=256,
        verbose_name='Name'
    )
    uf = models.CharField(
        max_length=5,
        verbose_name='UF'
    )

    def __str__(self):
        return self.name

class City(models.Model):
    # Relation With State
    state = models.ForeignKey(
        State, 
        on_delete=models.CASCADE, 
        verbose_name='State'
    )
    name = models.CharField(
        max_length=256,
        verbose_name='Name'
    )

    def __str__(self):
        return self.name



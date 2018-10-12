from django.contrib import admin

from .models import Country, State, City

@admin.register(Country)
class ContryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'initials')
    search_fields = ('name', 'initials')

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('id', 'contry', 'name', 'uf')
    search_fields = ('name', 'uf')

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'state', 'name')
    search_fields = ('name',)
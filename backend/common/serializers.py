from rest_framework import serializers
from .models import *


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = (
            'id',
            'name',
            'initials',
        )

class StateSerializer(serializers.ModelSerializer):
    country = serializers.PrimaryKeyRelatedField(
        queryset=Country.objects.all(), many=False)

    class Meta:
        model = State
        fields = (
            'id',
            'country',
            'name',
            'uf',
        )

class CitySerializer(serializers.ModelSerializer):
    state = serializers.PrimaryKeyRelatedField(
        queryset=State.objects.all(), many=False)

    class Meta:
        model = State
        fields = (
            'id',
            'state',
            'name',
        )
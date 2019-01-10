from rest_framework import serializers
from .models import *
from common.models import Country, State, City

# class StoreSerializer(serializers.ModelSerializer):
#     country = serializers.PrimaryKeyRelatedField(
#         queryset=Country.objects.all(), many=False)

#     state = serializers.PrimaryKeyRelatedField(
#         queryset=State.objects.all(), many=False)

#     city = serializers.PrimaryKeyRelatedField(
#         queryset=City.objects.all(), many=False)

#     class Meta:
#         model = Store
#         fields = (
#             'id',
#             'name',
#             'social_name',
#             'country',
#             'state',
#             'city',
#             'adress',
#         )


# class CheckoutSerializer(serializers.ModelSerializer):
#     store = serializers.PrimaryKeyRelatedField(
#         queryset=Store.objects.all(), many=False)

#     class Meta:
#         model = Checkout
#         fields = (
#             'id',
#             'store',
#             'number',
#         )

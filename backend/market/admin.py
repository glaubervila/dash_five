from django.contrib import admin

from .models import Store, Checkout

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'social_name', 'country', 'state', 'city')
    search_fields = ('name', 'social_name',)


@admin.register(Checkout)
class CheckoutAdmin(admin.ModelAdmin):
    list_display = ('id','store', 'number',)
    search_fields = ('number',)
from django.contrib import admin

from .models import Ticket, Payment

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'store', 'checkout', 'number', 'date', 'amount', 'discount', 'discount_percentage', 'is_canceled')
    search_fields = ('number',)

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'ticket', 'option', 'value', 'date_time', 'is_canceled')
    search_fields = ('ticket',)    
from django.contrib import admin

from .models import Transaction

# Register your models here.
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('transaction_time', 'user', 'transaction_method','transaction_amount')
    list_display_links = ('transaction_time',)
    ordering = ('-transaction_time',)
    filter_horizontal = ()
    list_filter = ('transaction_time', 'transaction_method')
    fieldsets = ()


admin.site.register(Transaction, TransactionAdmin)

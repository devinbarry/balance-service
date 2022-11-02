from django.contrib import admin
from .models import Transaction


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_filter = ('currency', )
    readonly_fields = ('created_date', 'modified_date', 'user', 'amount', 'currency', 'type', 'data')
    list_display = ('__str__', 'created_date', 'currency', 'type', 'amount')
    # actions = ['create_deposit']

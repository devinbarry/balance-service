from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .balance_utils import get_user_balance
from .models import Transaction


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_filter = ('currency', )
    readonly_fields = ('created_date', 'modified_date')
    list_display = ('__str__', 'created_date', 'currency', 'type', 'amount')
    # actions = ['create_deposit']


class BalanceUserAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_superuser', 'balance')
    list_filter = ('is_staff', 'is_superuser')
    search_fields = ('username', )

    def balance(self, obj):
        return get_user_balance(obj)


admin.site.unregister(User)
admin.site.register(User, BalanceUserAdmin)

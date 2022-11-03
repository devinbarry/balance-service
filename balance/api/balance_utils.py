from django.db.models import Sum

from .models import Transaction


def get_user_withdrawal_total(user):
    return Transaction.objects.filter(
        user=user, type=Transaction.TYPE.WITHDRAWAL).aggregate(Sum('amount'))['amount__sum'] or 0


def get_user_deposit_total(user):
    return Transaction.objects.filter(
        user=user, type=Transaction.TYPE.DEPOSIT).aggregate(Sum('amount'))['amount__sum'] or 0


def get_user_balance(user):
    return get_user_deposit_total(user) - get_user_withdrawal_total(user)

from decimal import Decimal

import factory
from factory.django import DjangoModelFactory

from django.contrib.auth.models import User

from .models import Transaction


class UserFactory(DjangoModelFactory):
    """
    Factory for generating User instances during testing.
    """
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f'user_{n}')
    email = factory.LazyAttribute(lambda o: '%s@example.org' % o.username)


class TransactionFactory(DjangoModelFactory):
    """
    Factory for generating Transaction instances during testing.
    """
    class Meta:
        model = Transaction

    currency = 'EUR'
    amount = Decimal('26.54')
    data = {}

    user = factory.SubFactory(UserFactory)
    type = Transaction.TYPE.DEPOSIT


class WithdrawalFactory(TransactionFactory):
    type = Transaction.TYPE.WITHDRAWAL


class DepositFactory(TransactionFactory):
    type = Transaction.TYPE.DEPOSIT

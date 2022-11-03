import logging
import uuid

from extended_choices import Choices

from django.conf import settings
from django.db import models, transaction

from common.validators import validate_positive

logger = logging.getLogger(__name__)


class Transaction(models.Model):
    """
    Transaction model
    """
    TYPE = Choices(
        ('DEPOSIT', 'deposit', 'Deposit'),
        ('WITHDRAWAL', 'withdrawal', 'Withdrawal'),
    )

    created_date = models.DateTimeField(auto_now_add=True, help_text='Transaction creation date.')
    modified_date = models.DateTimeField(auto_now=True)

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    currency = models.TextField(default='EUR', help_text='Currency of the transaction.')
    amount = models.DecimalField(max_digits=12, decimal_places=2, validators=[validate_positive])
    data = models.JSONField(default=dict, help_text='Additional data for the transaction.', blank=True)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='transactions')
    type = models.TextField(choices=TYPE, default=TYPE.DEPOSIT)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return f'{self.id}'

    @classmethod
    def create_deposit(cls, user, amount, currency='EUR', data=None):
        """
        Create a deposit transaction.
        """
        if data is None:
            data = {}
        return cls.objects.create(
            user=user,
            amount=amount,
            currency=currency,
            data=data,
            type=cls.TYPE.DEPOSIT,
        )

    @classmethod
    def create_withdrawal(cls, user, amount, currency='EUR', data=None):
        """
        Create a withdrawal transaction.
        """
        if data is None:
            data = {}
        return cls.objects.create(
            user=user,
            amount=amount,
            currency=currency,
            data=data,
            type=cls.TYPE.WITHDRAWAL,
        )


def create_transfer(user_from, user_to, amount, currency='EUR', data=None):
    """
    Create a pair of transactions (one withdrawal and one deposit)
    for a transfer between users.
    """
    with transaction.atomic():
        Transaction.create_withdrawal(user_from, amount, currency, data)
        Transaction.create_deposit(user_to, amount, currency, data)

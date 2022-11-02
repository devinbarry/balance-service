import logging
import uuid

from extended_choices import Choices

from django.db import models
from django.conf import settings

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
    data = models.JSONField()

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='transactions')
    type = models.TextField(choices=TYPE, default=TYPE.DEPOSIT)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return f'{self.id}'


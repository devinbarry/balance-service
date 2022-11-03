from decimal import Decimal

from django.test import TestCase

from ..balance_utils import get_user_balance, get_user_deposit_total, get_user_withdrawal_total
from ..factories import TransactionFactory, UserFactory
from ..models import Transaction


class BalanceUtilsTestCase(TestCase):
    """
    Test that balance utils work correctly
    """

    def test_get_user_withdrawal_total(self):
        user = UserFactory()
        TransactionFactory.create_batch(10, user=user, type=Transaction.TYPE.WITHDRAWAL, amount=Decimal('10.00'))
        total = get_user_withdrawal_total(user)
        self.assertEqual(total, Decimal('100.00'))

    def test_get_user_deposit_total(self):
        user = UserFactory()
        TransactionFactory.create_batch(10, user=user, type=Transaction.TYPE.DEPOSIT, amount=Decimal('10.00'))
        total = get_user_deposit_total(user)
        self.assertEqual(total, Decimal('100.00'))

    def test_get_user_balance_1(self):
        user = UserFactory()
        TransactionFactory.create_batch(10, user=user, type=Transaction.TYPE.DEPOSIT, amount=Decimal('10.00'))
        TransactionFactory.create_batch(10, user=user, type=Transaction.TYPE.WITHDRAWAL, amount=Decimal('10.00'))
        balance = get_user_balance(user)
        self.assertEqual(balance, Decimal('0.00'))

    def test_get_user_balance_2(self):
        user = UserFactory()
        TransactionFactory.create_batch(10, user=user, type=Transaction.TYPE.DEPOSIT, amount=Decimal('11.11'))
        TransactionFactory.create_batch(10, user=user, type=Transaction.TYPE.WITHDRAWAL, amount=Decimal('10.00'))
        balance = get_user_balance(user)
        self.assertEqual(balance, Decimal('11.10'))

    def test_get_user_balance_3(self):
        user = UserFactory()
        TransactionFactory.create_batch(10, user=user, type=Transaction.TYPE.DEPOSIT, amount=Decimal('11.11'))
        TransactionFactory.create_batch(10, user=user, type=Transaction.TYPE.WITHDRAWAL, amount=Decimal('123.00'))
        balance = get_user_balance(user)
        # 111.10 - 1230.00 = -1118.90
        self.assertEqual(balance, Decimal('-1118.90'))

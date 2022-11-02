from decimal import Decimal

from django.test import TestCase
from django.contrib.auth.models import User

from ..factories import UserFactory, TransactionFactory
from ..models import Transaction


class ModelFactoryTestCase(TestCase):
    """
    Test that are factories work as expected. They are crucial parts of the testing framework
    """
    def test_user_factory(self):
        user = UserFactory()
        self.assertIsInstance(user, User)

    def test_transaction_factory(self):
        tx = TransactionFactory()
        self.assertIsInstance(tx, Transaction)
        self.assertIsInstance(tx.user, User)
        self.assertIsInstance(tx.amount, Decimal)
        self.assertEqual(tx.type, Transaction.TYPE.DEPOSIT)

from decimal import Decimal

from rest_framework import status
from rest_framework.test import APITestCase

from django.urls import reverse

from ..factories import DepositFactory, UserFactory, WithdrawalFactory


class BalanceViewTestCase(APITestCase):

    def setUp(self):
        # Create an admin user because this is the only user that can auth against the API
        self.user = UserFactory(username='test_user', is_superuser=True, is_staff=True)
        self.client.force_authenticate(user=self.user)

    def test_get_self_by_id(self):
        DepositFactory(user=self.user, amount=1000)
        DepositFactory(user=self.user, amount=3000)

        url = reverse('api:balances', kwargs={'id': self.user.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, Decimal('4000.00'))

    def test_get_self_by_username(self):
        WithdrawalFactory(user=self.user, amount=1000)
        DepositFactory(user=self.user, amount=3000)

        url = reverse('api:balances') + f'?username={self.user.username}'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, Decimal('2000.00'))

    def test_get_user_by_id(self):
        user = UserFactory(username='foo')
        DepositFactory(user=user, amount=1000)
        DepositFactory(user=user, amount=9999.99)

        url = reverse('api:balances', kwargs={'id': user.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, Decimal('10999.99'))

    def test_get_user_by_username(self):
        user = UserFactory(username='bar')
        WithdrawalFactory(user=user, amount=5000)
        DepositFactory(user=user, amount=3000)

        url = reverse('api:balances') + f'?username={user.username}'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, Decimal('-2000.00'))

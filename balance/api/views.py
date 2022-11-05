from rest_framework import authentication, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from .balance_utils import get_user_balance


class BalanceView(APIView):
    """
    Get user balance
    """
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = [authentication.SessionAuthentication]

    def get(self, request, id=None, format=None):
        """
        Return a balance for a specific user.
        """
        if id:
            user = get_object_or_404(User, pk=id)
        else:
            username = request.GET.get('username')
            user = get_object_or_404(User, username=username)

        return Response(get_user_balance(user))

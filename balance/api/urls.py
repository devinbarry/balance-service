from rest_framework import routers

from django.urls import include, path

from .views import BalanceView

# TODO expose Transactions through this router
router = routers.DefaultRouter()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('balances/<int:id>/', BalanceView.as_view(), name='balances'),
    path('balances/', BalanceView.as_view(), name='balances'),
]

app_name = 'api'

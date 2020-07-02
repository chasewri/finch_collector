from rest_framework import routers
from .api import FinchViewSet

router = routers.DefaultRouter()

router.register('api/finch', FinchViewSet, 'finch')

urlpatterns = router.urls
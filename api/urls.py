from django.urls import path, include
from rest_framework import routers

from .api import DailyViewSet

router = routers.DefaultRouter()
router.register(r'dailies', DailyViewSet, basename = 'daily')

urlpatterns = router.urls

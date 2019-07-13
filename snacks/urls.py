from django.urls import path
from .views import SnackViewSet
from rest_framework.routers import DefaultRouter

app_name = 'snacks'

router = DefaultRouter()
router.register(r'snacks/snacks', SnackViewSet, base_name='snacks')

urlpatterns = router.urls


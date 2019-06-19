from django.urls import path
from .views import contratosViewSet
from rest_framework.routers import DefaultRouter

app_name = 'Empleados'

router = DefaultRouter()
router.register(r'empleados/contratos', contratosViewSet, basename="contratos")

urlpatterns = router.urls

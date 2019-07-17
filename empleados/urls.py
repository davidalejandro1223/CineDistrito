from django.urls import path
from .views import contratosViewSet,EmpleadosViewSet
from rest_framework.routers import DefaultRouter

app_name = 'Empleados'

router = DefaultRouter()
router.register(r'empleados/contratos', contratosViewSet, basename="contratos")
router.register(r'empleados/empleados', EmpleadosViewSet, basename="empleados")

urlpatterns = router.urls

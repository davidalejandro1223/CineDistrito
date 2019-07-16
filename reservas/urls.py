from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

app_name = 'Reservas'

router = DefaultRouter()

router.register(r'reservas/snack-reserva', SnackReservaViewSet, base_name='snack-reserva')

urlpatterns = [
    path('reservas/disponibilidad-sillas/<int:pk_funcion>/<int:pk_sala>/', DisponibilidadSillas.as_view(), name='disponibilidad-sillas'),
    path('reservas/factura/<int:pk_reserva>', Factura.as_view, name='factura'),
]+router.urls
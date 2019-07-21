from django.urls import path
from .views import *

app_name = 'Pagos'

urlpatterns = [
    path('pagos/factura/<int:pk_reserva>', Factura.as_view(), name='factura'),
    path('pagos/pago/<int:pk_reserva>', Pago.as_view(), name='pago')
]
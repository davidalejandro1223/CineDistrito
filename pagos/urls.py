from django.urls import path
from .views import *

app_name = 'Pagos'

urlpatterns = [
    path('pagos/factura/<int:pk_reserva>', FacturaView.as_view(), name='factura'),
    path('pagos/pago/<int:pk_reserva>', PagoView.as_view(), name='pago')
]
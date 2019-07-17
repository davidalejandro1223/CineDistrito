from django.urls import path
from .views import *

app_name = 'Pagos'

urlpatterns = [
    path('pagos/factura/<int:pk_reserva>', Factura.as_view(), name='factura'),
]
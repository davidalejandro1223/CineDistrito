from django.urls import path
from .views import DisponibilidadSillas

app_name = 'Reservas'

urlpatterns = [
    path('reservas/disponibilidad-sillas/<int:pk_funcion>/<int:pk_sala>/', DisponibilidadSillas.as_view(), name='disponibilidad-sillas'),
]

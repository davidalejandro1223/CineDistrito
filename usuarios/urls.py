from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import listPersonas, ClienteViewSet
app_name = 'usuarios'


router = DefaultRouter()
router.register(r'usuarios/clientes', ClienteViewSet, basename="clientes")
urlpatterns = [
    path('usuarios/personas', listPersonas.as_view(), name='lista-usuarios')
]+router.urls
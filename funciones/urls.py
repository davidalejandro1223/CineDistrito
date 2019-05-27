from django.urls import path
from .views import PeliculaViewSet, FuncionViewSet
from rest_framework.routers import DefaultRouter

app_name = 'funciones'

router = DefaultRouter()
router.register(r'funciones/peliculas', PeliculaViewSet, basename="peliculas")
router.register(r'funciones/funciones', FuncionViewSet, basename="funciones")

urlpatterns = router.urls

"""
urlpatterns = [
    path('funciones/peliculas', PeliculaViewSet.as_view({'get':'list', 'post':'create'}), name='PeliculaViewSet'),
    path('funciones/funciones', FuncionViewSet.as_view({'get':'list', 'post':'create'}), name='FuncionViewSet'),
] """


from django.urls import path
from .views import PeliculaViewSet, FuncionViewSet, FuncionSalaViewSet, MultiplexPeliculasView, FuncionesMultiplexView
from rest_framework.routers import DefaultRouter

app_name = 'funciones'

router = DefaultRouter()
router.register(r'funciones/peliculas', PeliculaViewSet, basename="peliculas")
router.register(r'funciones/funciones', FuncionViewSet, basename="funciones")
router.register(r'funciones/funciones-sala', FuncionSalaViewSet, base_name="funcion-sala")

urlpatterns = [
    path('funciones/peliculas-multiplex/<int:pk_pelicula>/', MultiplexPeliculasView.as_view(),name='peliculas-multiplex' ),
    path('funciones/funciones-multiplex/<int:pk_pelicula>/<int:pk_multiplex>/', FuncionesMultiplexView.as_view(), name='funciones-multiplex')
]+router.urls   
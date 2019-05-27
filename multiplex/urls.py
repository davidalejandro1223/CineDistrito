from django.urls import path
from .views import MultiplexViewSet, SalaViewSet, SillaViewSet
from rest_framework.routers import DefaultRouter

app_name = 'multiplex'

router = DefaultRouter()
router.register(r'multiplex/multiplex', MultiplexViewSet, base_name="multiplex")
router.register(r'multiplex/salas', SalaViewSet, base_name='salas')
router.register(r'multiplex/sillas', SillaViewSet, base_name='sillas')

urlpatterns = router.urls

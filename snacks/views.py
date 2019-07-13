from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import SnackSerializer
from .models import Snack
# Create your views here.

class SnackViewSet(ModelViewSet):
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer

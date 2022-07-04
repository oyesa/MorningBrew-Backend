from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializer import *

# Create your views here.
class ServiceViewSet(ModelViewSet):
    serializer_class=ServiceSerializer
    queryset=Service.objects.all()

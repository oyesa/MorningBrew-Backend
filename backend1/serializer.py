from dataclasses import fields
from statistics import mode
from rest_framework.serializers import ModelSerializer
from .models import *

class ServiceSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'
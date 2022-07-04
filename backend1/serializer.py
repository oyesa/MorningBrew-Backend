from dataclasses import fields
from statistics import mode
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = [
#             'username', 
#             'first_name', 
#             'last_name', 
#             'id',
#         ]

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        # fields = '__all__'
        fields = ['title','image','user','description']
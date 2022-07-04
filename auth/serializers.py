from django.forms import ValidationError
from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate
from rest_framework.validators import UniqueValidator

# Request and create a new user
class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=150,
        min_length=8,
        write_only=True, 
        required=True
    )
    email = serializers.EmailField(
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message='user with this email already exists'
            )
        ]
    )
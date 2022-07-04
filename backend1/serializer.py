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

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        # fields = '__all__'
        fields = ['title','image','user','description','post_date']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        # fields = ['title','image','user','description']

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        # fields = '__all__'
        fields = ['category','image','description']

class TestimonialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonials
        # fields = '__all__'
        fields = ['user','title','description','date_posted']
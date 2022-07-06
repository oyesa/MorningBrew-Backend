from dataclasses import fields
from statistics import mode
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
import enum

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username', 
            'first_name', 
            'last_name', 
        ]

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        # fields = '__all__'
        fields = ['title','image','description']

class CommentSerializer(serializers.ModelSerializer):

    user = UserSerializer()
    # post = PostSerializer()
    class Meta:
        model = Comment
        fields = ['user']
        # fields = ['title','image','user','description']

class PostSerializer(serializers.ModelSerializer):
    comment = CommentSerializer()
    class Meta:
        model = Post
        # fields = '__all__'
        fields = ['title','image','description','post_date','comment']

class GroupSerializer(serializers.ModelSerializer):
    class Category(enum.Enum):
        wellbeing= 'wellbeing'
        singleparentwithchildrenwithadditionalneeds = 'singleparentwithchildrenwithadditionalneeds(can)'
        singleparentfathers = 'singleparentfathers'
        
        def __str__(self):
            return self.value
        
    categorys = [cat.value for cat in Category]
    categories = serializers.ChoiceField(choices=categorys,required=True)

    class Meta:
        model = Group
        # fields = '__all__'
        fields = ['image','description','categories']

class TestimonialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonials
        # fields = '__all__'
        fields = ['title','description','date_posted']
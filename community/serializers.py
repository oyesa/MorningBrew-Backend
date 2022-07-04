from rest_framework import serializers
from .models import *


class CommunitySerializer(serializers.ModelSerializer):
    class Meta:
        model=Community
        fields=['image','description','category']

class HoodSerializer(serializers.ModelSerializer):
    class Meta:
        model=Hood
        fields=['name','description','location']

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model=Event
        fields=['title','image','description','date']
        
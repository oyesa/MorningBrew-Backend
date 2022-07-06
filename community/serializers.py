from rest_framework import serializers
from .models import *
import enum


class CommunitySerializer(serializers.ModelSerializer):
    class Category(enum.Enum):
        Shareyourexperience = 'Shareyourexperience'
        Joinmzazispaceevent = 'Joinmzazispaceevent'
        Supportandservices = 'Supportandservices'
        Singleparentgroups = 'Singleparentgroups'
        def __str__(self):
            return self.value
        
    categorys = [cat.value for cat in Category]
    categories = serializers.ChoiceField(choices=categorys,required=True)

    class Meta:
        model=Community
        fields=['image','description','categories']

class HoodSerializer(serializers.ModelSerializer):
    class Meta:
        model=Hood
        fields=['name','description','location']

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model=Event
        fields=['title','image','description','date']
        
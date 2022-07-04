from rest_framework import serializers
from .models import *


class CommunitySerializer(serializers.ModelSerializer):
    class Meta:
        model=Community
        fields=['image','description','category']
        
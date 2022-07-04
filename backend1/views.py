from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializer import *

# Create your views here.
class ServiceViewSet(ModelViewSet):
    serializer_class=ServiceSerializer
    queryset=Service.objects.all()


class PostViewSet(ModelViewSet):
    serializer_class=PostSerializer
    queryset=Post.objects.all()


class CommentViewSet(ModelViewSet):
    serializer_class=CommentSerializer
    queryset=Comment.objects.all()

class GroupViewSet(ModelViewSet):
    serializer_class=GroupSerializer
    queryset=Group.objects.all()
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializer import *
from rest_framework.permissions import AllowAny, IsAuthenticated


# Create your views here.
class ServiceViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)

    serializer_class=ServiceSerializer
    queryset=Service.objects.all()


class PostViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)

    serializer_class=PostSerializer
    queryset=Post.objects.all()


class CommentViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)

    serializer_class=CommentSerializer
    queryset=Comment.objects.all()

class GroupViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)

    serializer_class=GroupSerializer
    queryset=Group.objects.all()

class TestimonialsViewSet(ModelViewSet):
    serializer_class=TestimonialsSerializer
    queryset=Testimonials.objects.all()
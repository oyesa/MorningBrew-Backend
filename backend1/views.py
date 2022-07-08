from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializer import *
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import GenericAPIView,ListAPIView
from rest_framework.response import Response
from rest_framework import status
import json

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
    permission_classes = (IsAuthenticated,)
    serializer_class=TestimonialsSerializer
    queryset=Testimonials.objects.all()

class TestimonialsListView(ListAPIView):
    """
    A class for getting all testimonials
    """
    permission_classes = (AllowAny,)
    serializer_class =  TestimonialsSerializer
    queryset = Testimonials.objects.all()

    def list(self, request):
        queryset = self.queryset.filter()
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'testimonials': serializer.data
        }, status=status.HTTP_200_OK)

class ServicesListView(ListAPIView):
    """
    A class for getting all srvices
    """
    permission_classes = (AllowAny,)
    serializer_class =  ServiceSerializer
    queryset = Service.objects.all()

    def list(self, request):
        queryset = self.queryset.filter()
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'services': serializer.data
        }, status=status.HTTP_200_OK)

class PostsListView(ListAPIView):
    """
    A class for getting all posts
    """
    permission_classes = (AllowAny,)
    serializer_class =  PostSerializer
    queryset = Post.objects.all()

    def list(self, request):
        queryset = self.queryset.filter()
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'posts': serializer.data
        }, status=status.HTTP_200_OK)

class GroupsListView(ListAPIView):
    """
    A class for getting all groups
    """
    permission_classes = (AllowAny,)
    serializer_class =  GroupSerializer
    queryset = Group.objects.all()

    def list(self, request):
        queryset = self.queryset.filter()
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'groups': serializer.data
        }, status=status.HTTP_200_OK)

class CommentsListView(ListAPIView):
    """
    A class for getting all comments
    """
    permission_classes = (AllowAny,)
    serializer_class =  CommentSerializer
    queryset = Comment.objects.all()

    def list(self, request):
        queryset = self.queryset.filter()
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'comments': serializer.data
        }, status=status.HTTP_200_OK)

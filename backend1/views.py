from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializer import *
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import GenericAPIView,ListAPIView
from rest_framework.response import Response
from rest_framework import status

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

class ServiceListView(ListAPIView):
    """
    A class for getting all services
    """
    permission_classes = (AllowAny,)
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()

    def list(self, request):
        queryset = self.queryset.filter()
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'service': serializer.data
        }, status=status.HTTP_200_OK)

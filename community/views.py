from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import GenericAPIView,ListAPIView


# Create your views here.
class CommunityViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer
class CommunityList(APIView):
    def get(self, request, format=None):
        all_communities = Community.objects.all()
        serializers = CommunitySerializer(all_communities, many=True)
        return Response(serializers.data)
    def post(self, request, format=None):
        serializers = CommunitySerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)

@api_view(['GET','PUT', 'DELETE'])
def showcommunity(request, pk):
    """
    Retrieve, update or delete a code contact.
    """
    try:
       community= Community.objects.get(id=pk)
    except Community.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer =CommunitySerializer(Community)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CommunitySerializer(Community, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        Community.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class HoodViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Hood.objects.all()
    serializer_class = HoodSerializer


class EventViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class CommunitysListView(ListAPIView):
    """
    A class for getting all groups
    """
    permission_classes = (AllowAny,)
    serializer_class =  CommunitySerializer
    queryset = Community.objects.all()

    def list(self, request):
        queryset = self.queryset.filter()
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'communities': serializer.data
        }, status=status.HTTP_200_OK)

class HoodsListView(ListAPIView):
    """
    A class for getting all groups
    """
    permission_classes = (AllowAny,)
    serializer_class =  HoodSerializer
    queryset = Hood.objects.all()

    def list(self, request):
        queryset = self.queryset.filter()
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'hoods': serializer.data
        }, status=status.HTTP_200_OK)

class EventsListView(ListAPIView):
    """
    A class for getting all groups
    """
    permission_classes = (AllowAny,)
    serializer_class =  EventSerializer
    queryset = Event.objects.all()

    def list(self, request):
        queryset = self.queryset.filter()
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'events': serializer.data
        }, status=status.HTTP_200_OK)



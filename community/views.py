from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated



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
        serializer = CommunitySerializer(Portfolio, data=request.data)
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



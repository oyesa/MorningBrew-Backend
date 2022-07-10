from django.urls import path,include
from rest_framework import routers
from django.conf import settings
from .views import *
from . import views


router = routers.DefaultRouter()
router.register('community', views.CommunityViewSet)
router.register('hood', views.HoodViewSet)
router.register('event', views.EventViewSet)



urlpatterns = [
    path('api/',include(router.urls)),
    path('communitys/',  CommunitysListView.as_view(), name='list_communitys'),
    path('hoods/',  HoodsListView.as_view(), name='list_hoods'),
    path('events/',  EventsListView.as_view(), name='list_events'),
    path('api/community/<int:pk>/',views.showcommunity, name='community'),

]
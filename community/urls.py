from django.urls import path,include
from rest_framework import routers
from django.conf import settings
from .views import *
from . import views


router = routers.DefaultRouter()
router.register('community', views.CommunityViewSet)

urlpatterns = [
    path('api/',include(router.urls)),
    path('api/community/<int:pk>/',views.showcommunity, name='community')

]
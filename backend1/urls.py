from rest_framework.routers import DefaultRouter
from .views import *
from django.urls import path,include

router = DefaultRouter()
router.register('service',ServiceViewSet)


urlpatterns = [
    path('api/',include(router.urls)),
]
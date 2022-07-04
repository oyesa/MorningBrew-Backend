from rest_framework.routers import DefaultRouter
from .views import *
from django.urls import path,include

router = DefaultRouter()
router.register('service',ServiceViewSet)
router.register('post',PostViewSet)
router.register('comment',CommentViewSet)

urlpatterns = [
    path('api/',include(router.urls)),
]
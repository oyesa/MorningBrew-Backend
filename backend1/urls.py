from rest_framework.routers import DefaultRouter
from .views import *
from django.urls import path,include

router = DefaultRouter()
router.register('service',ServiceViewSet)
router.register('post',PostViewSet)
router.register('comment',CommentViewSet)
router.register('group',GroupViewSet)
router.register('testimonial',TestimonialsViewSet)

urlpatterns = [
    path('api/',include(router.urls)),
    path('testimonials/', TestimonialsListView.as_view(), name='list_testimonials'),
    path('services/',  ServicesListView.as_view(), name='list_services'),
    path('posts/',  PostsListView.as_view(), name='list_posts'),
    path('groups/',  GroupsListView.as_view(), name='list_groups'),
    path('comments/',  CommentsListView.as_view(), name='list_comments'),
]
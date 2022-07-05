from .views import *
from django.urls import path

urlpatterns = [
    path('register/', RegistrationAPIView.as_view(), name='register'),
    path('login/', LoginApiView.as_view(), name='login') 
    

]
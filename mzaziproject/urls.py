
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('request/',include('backend1.urls')), 
    path('auth/', include('mzaziauth.urls')),
    path('request/',include('community.urls')),
    
]

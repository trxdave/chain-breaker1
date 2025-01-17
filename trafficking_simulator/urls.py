from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),       
    path('about/', include('about.urls')), 
    path('resources/', include('resources.urls')),
    path('results/', include('results.urls')),
    path('simulator/', include('simulator.urls')),
]

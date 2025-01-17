from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),  # Include the URLs for the home app
    path('about/', include('about.urls')),  # Include the URLs for the about app
    path('simulator/', include('simulator.urls')),  # Include the URLs for the simulation app
    path('resources/', include('resources.urls')),  # Include the URLs for the resources app
    path('results/', include('results.urls')),  # Include the URLs for the results app
]

# Serve static and media files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

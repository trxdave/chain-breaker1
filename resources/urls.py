from django.urls import path
from . import views

urlpatterns = [
    path('', views.resources, name='resources'),  # Define the 'about' URL pattern
]
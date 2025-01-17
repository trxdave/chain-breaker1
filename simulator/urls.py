from django.urls import path
from . import views

urlpatterns = [
    path('', views.simulator, name='simulator'),  # Define the 'about' URL pattern
]
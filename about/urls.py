# about/urls.py
from django.urls import path
from . import views  # Make sure this is correctly importing the views module

urlpatterns = [
    path('', views.about_view, name='about'),  # Ensure this is correct
]

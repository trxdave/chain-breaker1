from django.urls import path
from . import views

urlpatterns = [
    path('', views.about_view, name='about'),
    path('meet-the-team/', views.meet_the_team, name='meet_the_team'),
]

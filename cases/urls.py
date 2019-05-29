from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='case-home'),
    path('clients/', views.add_client, name='clients'),
]
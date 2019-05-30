from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='cases-home'),
    path('clients/', views.client_tabs, name='client-tabs'),
    path('court/', views.court_tabs, name='court-tabs'),

]
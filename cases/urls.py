from django.urls import path
from . import views
from .views import ClientListView
from django_filters.views import FilterView
from .filters import ClientsFilter

urlpatterns = [
    path('', ClientListView.as_view(), name='cases-home'),
    path('clients/', views.client_tabs, name='client-tabs'),
    path('court/', views.court_tabs, name='court-tabs'),
    path('clients_form/', views.clients, name='clients'),
    path('search/', FilterView.as_view(filterset_class=ClientsFilter), name='search')
]
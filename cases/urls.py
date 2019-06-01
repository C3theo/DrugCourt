from django.urls import path
from . import views
from .views import ClientListView, ReferralsCreate, ReferralsDelete, ReferralsUpdate, ReferralsListView
from django_filters.views import FilterView
from .filters import ClientsFilter

urlpatterns = [
    path('', ReferralsListView.as_view(), name='cases-home'),
    path('clients/', views.client_tabs, name='client-tabs'),
    path('search/', FilterView.as_view(filterset_class=ClientsFilter), name='search'),
    path('referrals/add/', ReferralsCreate.as_view(), name='referrals-add'),
    path('referrals/<int:pk>/', ReferralsUpdate.as_view(), name='referrals-update'),
    path('referrals/<int:pk>/delete/', ReferralsDelete.as_view(), name='referrals-delete'),
]
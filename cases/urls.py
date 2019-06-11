from django.urls import path
from . import views
from .views import ClientListView, ReferralsCreate, ReferralsDelete, ReferralsUpdate, ReferralsListView
from django_filters.views import FilterView
from .filters import ClientsFilter
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.home, name='cases-home'),
    path('search/', login_required(FilterView.as_view(filterset_class=ClientsFilter)), name='search'),
    path('referrals/all/', ReferralsListView.as_view(), name='referrals-all'),
    path('referrals/add/', ReferralsCreate.as_view(), name='referrals-add'),
    path('referrals/<int:pk>/', ReferralsUpdate.as_view(), name='referrals-update'),
    path('referrals/<int:pk>/delete/', ReferralsDelete.as_view(), name='referrals-delete'),
]
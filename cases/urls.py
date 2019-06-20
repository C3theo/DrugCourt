from django.urls import path
from . import views
from .views import ReferralsCreate, ReferralsDelete, ReferralsUpdate, ReferralsListView, IntakeView
from django_filters.views import FilterView
from .filters import ClientsFilter
from django.contrib.auth.decorators import login_required


app_name = 'cases'
urlpatterns = [

    path('', views.home , name='home'),
    path('intake/', IntakeView.as_view(), name='intake'),
    # path('search/', login_required(FilterView.as_view(filterset_class=ClientsFilter)), name='search'),
    path('all/', ReferralsListView.as_view(), name='all'),
    path('add/', ReferralsCreate.as_view(), name='add'),
    path('<int:pk>/', ReferralsUpdate.as_view(), name='update'),
    path('<int:pk>/delete/', ReferralsDelete.as_view(), name='delete'),
]
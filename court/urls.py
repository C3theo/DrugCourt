from django.contrib.auth.decorators import login_required
from django.urls import include, path, re_path
from django.views import generic

from . import views
from .views import (CourtDateUpdateView, CourtDateListView, CourtDateView)

app_name = 'court'

urlpatterns = [
    path('', CourtDateView.as_view(), name='add'),
    path('court/<int:pk>', CourtDateUpdateView.as_view(), name='detail'),
    path('court/all', CourtDateListView.as_view(), name='dates'),
    # path('court/filter', views.court_date_client_list, name='court-filter'),
]


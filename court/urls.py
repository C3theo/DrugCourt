from django.contrib.auth.decorators import login_required
from django.urls import include, path, re_path
from django.views import generic

from . import views
from .views import (CourtDateUpdateView, CourtDateListView, CourtDateView)

app_name = 'court'

urlpatterns = [
    path('', CourtDateView.as_view(), name='add'),
    path('dates/<int:pk>', CourtDateUpdateView.as_view(), name='detail'),
    path('dates/', CourtDateListView.as_view(), name='dates'),
    path('filter/', views.court_date_client_list, name='filter'),
    path('dates/list', views.court_date_list, name='list'),
    path('dates/create', views.court_date_create, name='create'),
    path('dates/<int:pk>/update', views.court_date_update, name='update'),
]


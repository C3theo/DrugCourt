from django.contrib.auth.decorators import login_required
from django.urls import include, path, re_path
from django.views import generic

from . import views

app_name = 'intake'

# AJAX Views
urlpatterns = [
    path('client/list', views.client_list, name='list'),
    path('client/create', views.client_create, name='create'),
    path('client/<int:pk>/update', views.client_update, name='update'),
    path('client/<int:pk>/evaluate', views.client_evaluate, name='eval'),
    path('client/<int:pk>/note', views.client_note, name='note'),
]

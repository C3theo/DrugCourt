from django.contrib.auth.decorators import login_required
from django.urls import include, path, re_path
from django.views import generic

from . import views


app_name = 'court'

urlpatterns = [   
    path('dates/list', views.court_date_list, name='list'),
    path('dates/create', views.court_date_create, name='create'),
    path('dates/<int:pk>/update', views.court_date_update, name='update'),
    path('dates/<int:pk>/note', views.court_date_note, name='note'),
    path('phase/list', views.phase_list, name='phase'),
    path('phase/create', views.phase_create, name='phase-create'),
    path('phase/<int:pk>/update', views.phase_update, name='phase-update'),
]


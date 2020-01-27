from django.urls import include, path, re_path

from . import views

app_name = 'intake'

urlpatterns = [

path('list/', views.treatment_list, name='list'),
path('create/', views.treatment_create, name='create'),
path('<int:pk>/update', views.treatment_update, name='update'),
]

from django.contrib.auth.decorators import login_required
from django.urls import include, path, re_path
from django.views import generic
from . import views
app_name = 'treatment'
urlpatterns = [
    path('', views.sessions, name='sessions'),
]
 
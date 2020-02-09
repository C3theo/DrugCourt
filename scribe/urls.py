from django.contrib.auth.decorators import login_required
from django.urls import include, path, re_path
from django.views import generic

from . import views
from .views import NoteListView

app_name = 'scribe'

urlpatterns = [

    # path('', NoteListView.as_view(), name='all'),

]


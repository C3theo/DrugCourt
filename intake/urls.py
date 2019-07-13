from django.urls import path
from . import views
from .views import IntakeFormView, ClientListView, NoteListView
from django.contrib.auth.decorators import login_required

app_name = 'intake'
urlpatterns = [
    path('new/', IntakeFormView.as_view(), name='new'),
    path('clients/', ClientListView.as_view(), name='clients'),
    path('notes/', NoteListView.as_view(), name='notes'),
]

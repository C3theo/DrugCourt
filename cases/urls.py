from django.urls import path
from . import views
from .views import ReferralsCreate, ReferralsDelete, ReferralsUpdate, ReferralsListView, IntakeFormView, ClientListView, NoteListView
from django.contrib.auth.decorators import login_required


app_name = 'cases'
urlpatterns = [

    path('', views.home, name='home'),
    path('intake/', IntakeFormView.as_view(), name='intake'),
    path('intake/client', ClientListView.as_view(), name='clients'),
    path('intake/notes', NoteListView.as_view(), name='notes'),
    path('all/', ReferralsListView.as_view(), name='all'),
    path('add/', ReferralsCreate.as_view(), name='add'),
    path('<int:pk>/', ReferralsUpdate.as_view(), name='update'),
    path('<int:pk>/delete/', ReferralsDelete.as_view(), name='delete'),
]

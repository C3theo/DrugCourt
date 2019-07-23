from django.contrib.auth.decorators import login_required
from django.urls import include, path, re_path
from django.views import generic

from . import views
from .views import (ClientDetailView, ClientListView, ClientNoteCreateView,
                    CourtDateDetailView, CourtDateListView, CourtDateView,
                    CriminalBackgroundCreateView, DecisionCreateView,
                    IntakeFormView, NoteListView, ReferralCreateView,
                    ReferralDetailView)

app_name = 'intake'

urlpatterns = [
    path('', IntakeFormView.as_view(), name='new'),
    path('new/', IntakeFormView.as_view(), name='new'),
    path('clients/', ClientListView.as_view(), name='clients'),
    path('client/<int:pk>', ClientDetailView.as_view(), name='detail'),
    path('notes/', ClientNoteCreateView.as_view(), name='note-add'),
    path('notes/all', NoteListView.as_view(), name='notes'),
    path('referral', ReferralCreateView.as_view(), name='referral'),
    path('referral/<int:pk>', ReferralDetailView.as_view(), name='referral-detail'),
    path('referral/decision', DecisionCreateView.as_view(), name='decision'),
    path('notes/all', NoteListView.as_view(), name='notes'),
    path('court/', CourtDateView.as_view(), name='court'),
    path('court/<int:pk>', CourtDateDetailView.as_view(), name='court-detail'),
    path('court/all', CourtDateListView.as_view(), name='dates'),
    path('court/filter', views.court_date_client_list, name='court-filter'),
    path('legal/', CriminalBackgroundCreateView.as_view(), name='legal'),
]

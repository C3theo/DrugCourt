from django.contrib.auth.decorators import login_required
from django.urls import include, path, re_path
from django.views import generic

from . import views
from .views import (ClientUpdateView, ClientListView, ClientNoteCreateView,
                    CourtDateUpdateView, CourtDateListView, CourtDateView,
                    CriminalBackgroundCreateView, ReferralDecisionUpdateView,
                    NoteListView, ClientReferralCreateView, ClientReferralUpdateView, IntakeFilterView)

app_name = 'intake'

urlpatterns = [
    path('', IntakeFilterView.as_view(), name='start'),
    path('referral', ClientReferralCreateView.as_view(), name='referral-add'),
    path('referral/<int:pk>', ClientReferralUpdateView.as_view(), name='referral-detail'),
    path('referral/decision/<int:pk>', ReferralDecisionUpdateView.as_view(), name='decision'),
    path('clients/', ClientListView.as_view(), name='clients'),
    path('client/<int:pk>', ClientUpdateView.as_view(), name='client-detail'),
    path('notes/', ClientNoteCreateView.as_view(), name='note-add'),
    path('notes/all', NoteListView.as_view(), name='notes'),
    path('notes/all', NoteListView.as_view(), name='notes'),
    path('court/', CourtDateView.as_view(), name='court'),
    path('court/<int:pk>', CourtDateUpdateView.as_view(), name='court-detail'),
    path('court/all', CourtDateListView.as_view(), name='dates'),
    path('court/filter', views.court_date_client_list, name='court-filter'),
    path('legal/', CriminalBackgroundCreateView.as_view(), name='legal'),
]

# Home page Intake Module Card
#  <a href="{% url 'intake:note-add' %}" class="list-group-item list-group-item-action">Notes</a>
#                 <a href="{% url 'intake:legal' %}" class="list-group-item list-group-item-action">Crimes</a>
#                 <a href="{% url 'intake:referral-add' %}" id="referral-add" class="list-group-item list-group-item-action">Referrals</a>
#                 <a href="{% url 'intake:decision' %}" class="list-group-item list-group-item-action">Decsions</a>

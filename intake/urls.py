from django.contrib.auth.decorators import login_required
from django.urls import include, path, re_path
from django.views import generic

from . import views
from .views import (ClientUpdateView, ClientListView, ClientNoteCreateView,
                    CriminalBackgroundCreateView, ReferralDecisionUpdateView,
                    ClientReferralCreateView, ClientReferralUpdateView, IntakeFilterView)

app_name = 'intake'

urlpatterns = [
    path('', IntakeFilterView.as_view(), name='start'),
    path('referral', ClientReferralCreateView.as_view(), name='referral-add'),
    path('referral/<int:pk>', ClientReferralUpdateView.as_view(),
         name='referral-detail'),
    path('referral/decision/<int:pk>',
         ReferralDecisionUpdateView.as_view(), name='decision'),
    path('criminalhistory/', CriminalBackgroundCreateView.as_view(), name='crimes'),
    path('notes/', ClientNoteCreateView.as_view(), name='note-add'),
    path('clients/', ClientListView.as_view(), name='clients'),
    path('client/<int:pk>', ClientUpdateView.as_view(), name='client-detail'),

    path('client/list', views.client_list, name='list'),
    path('client/create', views.client_create, name='create'),
    path('client/<int:pk>/update', views.client_update, name='update'),
    path('client/<int:pk>/evaluate', views.client_evaluate, name='eval'),
]

from django.contrib.auth.decorators import login_required
from django.urls import include, path, re_path
from django.views import generic
from material.frontend import urls as frontend_urls
from viewflow.flow.viewset import FlowViewSet

from intake.models.bpmn.flows import DecisionFlow

from . import views
from .views import (ClientDetailView, ClientListView, ClientNoteCreateView,
                    CourtDateDetailView, CourtDateListView, CourtDateView,
                    DecisionCreateView, IntakeFormView, NoteListView)

app_name = 'intake'
urlpatterns = [
    path('new/', IntakeFormView.as_view(), name='new'),
    path('clients/', ClientListView.as_view(), name='clients'),
    path('client/<int:pk>', ClientDetailView.as_view(), name='detail'),
    path('notes/add', ClientNoteCreateView.as_view(), name='note-add'),
    path('notes/', NoteListView.as_view(), name='notes'),
    path('court/', CourtDateView.as_view(), name='court'),
    path('court/<int:pk>', CourtDateDetailView.as_view(), name='court-detail'),
    path('court/all', CourtDateListView.as_view(), name='dates'),
    path('court/filter', views.court_date_client_list, name='court-filter'),
    path('', generic.TemplateView.as_view(
        template_name="intake/index.html"), name="index")
    # path('decision/', DecisionView.as_view(), name='decision'),
    # re_path(r'^decision/', FlowViewSet(DecisionFlow).urls, name='decisions')
]

# urlpatterns += FlowViewSet(DecisionFlow).urls

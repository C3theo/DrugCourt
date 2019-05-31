from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import FormView

from django_filters.views import FilterView
from django_tables2.views import SingleTableView

from .forms import ClientsForm, ClientsTabForm, CourtTabForm
from .models import Clients
from .filters import ClientsFilter
from .tables import ClientsTable


@login_required
def home(request):
    return render(request, 'cases/home.html', context={'current':'(current)'})

@login_required()
def client_tabs(request):
    form = ClientsTabForm()
    return render(request, 'cases/client_tabs.html', {'form': form})

@login_required()
def court_tabs(request):
    form = CourtTabForm()
    return render(request, 'cases/court_tabs.html', {'form': form})

@login_required
def clients(request):
    form = ClientsForm
    return render(request, 'cases/client_tabs.html', {'form': form})

class ClientListView(SingleTableView, LoginRequiredMixin):
    model = Clients
    table_class = ClientsTable
    template_name = 'cases/clients_listing.html'
    context_object_name = 'clients'

class FilteredClientsListView(FilterView, SingleTableView):
    table_class = ClientsTable
    model = Clients
    template_name = 'cases/clients_filter.html'

    filterset_class = ClientsFilter


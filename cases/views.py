from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import FormView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy, reverse

from django_filters.views import FilterView
from django_tables2.views import SingleTableView

from .forms import ClientsForm, ClientsTabForm, ReferralsTabs
from .models import Clients, Referrals
from .filters import ClientsFilter
from .tables import ClientsTable, ReferralsTable


@login_required
def home(request):
    return render(request, 'cases/home.html', context={'current':'(current)'})

@login_required()
def client_tabs(request):
    form = ClientsTabForm()
    return render(request, 'cases/client_tabs.html', {'form': form})

class ReferralsCreate(CreateView, LoginRequiredMixin):
    model = Referrals
    form_class = ReferralsTabs
    # success_url = reverse('client-tabs')
    template_name ='cases/referrals_tabs.html'

    def form_valid(self, form):
        # form.instance.created_by = self.request.user
        # super() and pass new form instance
        return self.render_to_response(self.get_context_data(form=form))

class ReferralsUpdate(UpdateView, LoginRequiredMixin):
    model = Referrals
    form_class = ReferralsTabs
    
    template_name ='cases/referrals_tabs.html'

class ReferralsDelete(DeleteView, LoginRequiredMixin):
    model = Referrals
    success_url = reverse_lazy('referrals-list')
    template_name ='cases/referrals_tabs.html'

class ReferralsListView(SingleTableView, LoginRequiredMixin):
    model = Referrals
    table_class = ReferralsTable
    template_name = 'cases/clients_listing.html'
    context_object_name = 'referrals'

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


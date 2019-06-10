from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse, reverse_lazy, path
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from django.views.generic.edit import (CreateView, DeleteView, FormView,
                                       UpdateView)

from django_filters.views import FilterView
from django_tables2.views import SingleTableView

from .filters import ClientsFilter
from .forms import ClientsForm, ClientsTabForm, ReferralsTabs
from .models import Clients, Referrals
from .tables import ClientsTable, ReferralsTable


@login_required
def home(request):
    return render(request, 'cases/home.html')

class ReferralsCreate(LoginRequiredMixin, CreateView):
    model = Referrals
    form_class = ReferralsTabs
    template_name ='cases/referrals_tabs.html'

# Did this when I created Detail View with dad
    def form_valid(self, form):
        # form.instance.created_by = self.request.user
        # super() and pass new form instance
        return self.render_to_response(self.get_context_data(form=form))


class ReferralsUpdate(LoginRequiredMixin, UpdateView):
    model = Referrals
    form_class = ReferralsTabs
    template_name = 'cases/referrals_tabs.html'

    def form_valid(self, form):
        if 'approved' in form.data:
            form.instance.approve_referral()
        
        return super().form_valid(form)


def approve_ref(request):
    template_name = 'cases/referrals_tabs.html'
    if request.POST.get('name') == 'approve':
        return render(request, template_name=template_name, status=302,  )
    else:
        return HttpResponseRedirect('/')


class ReferralsDelete(LoginRequiredMixin, DeleteView):
    model = Referrals
    success_url = reverse_lazy('referrals-list')
    template_name ='cases/referrals_tabs.html'

class ReferralsListView(LoginRequiredMixin, SingleTableView):
    model = Referrals
    table_class = ReferralsTable
    template_name = 'cases/clients_listing.html'
    context_object_name = 'referrals'

class ClientListView(LoginRequiredMixin, SingleTableView):
    model = Clients
    table_class = ClientsTable
    template_name = 'cases/clients_listing.html'
    context_object_name = 'clients'

# login required not working for filtered view
class FilteredClientsListView(LoginRequiredMixin, FilterView):
    table_class = ClientsTable
    model = Clients
    template_name = 'cases/clients_filter.html'
    filterset_class = ClientsFilter

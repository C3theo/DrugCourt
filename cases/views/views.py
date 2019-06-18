
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import path, reverse, reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.utils import timezone

from django_filters.views import FilterView
from django_tables2.views import SingleTableView

from ..filters import ClientsFilter
from ..forms import ClientForm, ReferralsTabs
from ..models import Clients, Referrals, TransitionNotAllowed, Client
from ..tables import ClientsTable, ReferralsTable

# TODO: add logging

@login_required
def home(request):
    return render(request, 'cases/home.html')

class ReferralsCreate(LoginRequiredMixin, CreateView):
    model = Referrals
    form_class = ReferralsTabs
    template_name = 'cases/forms_base.html'

    def form_valid(self, form):

        if not form.instance.userid:
            form.instance.userid = self.request.user.username

        if not form.instance.created:
            form.instance.created = timezone.now()

        if form.instance.clientid == '':
            form.instance.clientid = form.instance.create_clientid()
        
        if not form.instance.status:
            form.instance.add_referral()

        return super().form_valid(form)

class ReferralsUpdate(LoginRequiredMixin, UpdateView):
    model = Referrals
    form_class = ReferralsTabs
    template_name = 'cases/forms_base_update.html'

# TODO: move this to a Mixin
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        if 'approve' in self.request.POST:
            try:
                self.object.approve_referral()
                self.object.save()
                return HttpResponseRedirect(self.object.get_absolute_url())
            except TransitionNotAllowed:
                return HttpResponseRedirect('/')
        
        if 'add' in self.request.POST:
            self.object.add_referral()
            self.object.save()
            return HttpResponseRedirect(self.object.get_absolute_url())

        return super().post(self, request, *args, **kwargs)

class ReferralsDelete(LoginRequiredMixin, DeleteView):
    model = Referrals
    success_url = reverse_lazy('referrals-list')
    template_name = 'cases/forms_base.html'


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

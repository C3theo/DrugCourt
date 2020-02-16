from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db import transaction
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import render_to_string
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, TemplateView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django_tables2.views import MultiTableMixin, SingleTableView
from indexed import IndexedOrderedDict

from core.helpers import (add_forms_to_context, get_ajax_search_results,
                          paginate_model, save_ajax_form)
from scribe.forms import NoteForm
from scribe.models import Note
from scribe.tables import NoteTable

from ..forms import (ClientForm, ClientFormset, CriminalBackgroundForm,
                     DecisionForm, ReferralForm, ReferralQueryForm)
from ..models import Client, CriminalBackground, Decision, Referral
from .filters import ClientFilter, ReferralFilter
from .tables import ClientCourtTable, ClientTable


def client_list(request):
    
    context = get_ajax_search_results(request, Client)
    if request.is_ajax():
        html = render_to_string(
            template_name='intake/includes/partial_client_list.html',
            context=context
        )

        data_dict = {"html_model_list": html}
        return JsonResponse(data=data_dict, safe=False)
    else:
        return render(request, 'intake/client_list.html', context)


def client_create(request):
    """
        Handle GET/POST requests and instantiate forms.
    """

    if request.method == 'POST':
        client_form = ClientForm(request.POST)
        referral_form = ReferralForm(request.POST)
    else:
        client_form = ClientForm()
        referral_form = ReferralForm()

    forms = (client_form, referral_form)
    context = IndexedOrderedDict()
    context['client'] = client_form.instance
    context = add_forms_to_context(forms, context)

    return save_ajax_form(
        request, context=context, list_template='intake/includes/partial_client_list.html', form_template='intake/includes/partial_client_create.html')


def client_update(request, pk):
    """
    """

<<<<<<< HEAD
    model = Referral
    form_class = ClientReferralMultiForm
    template_name = 'intake/1_client_referral.html'

    def get_context_data(self, **kwargs):
        """
            Initialize NoteForm with client and pass to context
        """

        note_form = NoteForm(prefix='note')
        context = {'note_form': note_form}
        return super().get_context_data(**context)

    def post(self, request, *args, **kwargs):
        """
            Submit NoteForm separately from Referral/ClientForm.
        """

        referral = self.get_object()
        self.success_url = referral.get_absolute_url()  # ???
        note_form = _get_form_submit(
            request, NoteForm, prefix='note')
        if note_form.is_bound and note_form.is_valid():
            note_form.instance.author = self.request.user
            note_form.instance.client = referral.client
            instance = note_form.save()
            messages.success(
                request, f'Note for {instance.client.full_name} ID: {instance.client.id}  saved successfully!')
            return self.form_valid(note_form)

        return super().post(request, *args, **kwargs)

    def get_form_kwargs(self):
        """
            Return the keyword arguments for instantiating client and referral forms.
        """

        kwargs = super(ClientReferralUpdateView, self).get_form_kwargs()
        kwargs.update(instance={
            'client': self.object.client,
            'referral': self.object
        })
=======
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        client_form = ClientForm(request.POST, instance=client)
        referral_form = ReferralForm(request.POST, instance=client.referral)
>>>>>>> origin/Dev-3

    else:  # GET Request (loadForm)

        client_form = ClientForm(instance=client)
        referral_form = ReferralForm(instance=client.referral)

    forms = (client_form, referral_form)
    context = IndexedOrderedDict()
    context['client'] = client
    context = add_forms_to_context(forms, context)

    return save_ajax_form(request, context=context, list_template='intake/includes/partial_client_list.html', form_template='intake/includes/partial_client_update.html')


def client_evaluate(request, pk):
    """
    """

    referral = get_object_or_404(Referral, pk=pk)
    decisions = referral.decisions
    
    if request.method == 'POST':

        forms = (DecisionForm(request.POST, instance=decision)
                 for decision in decisions)
    else:
        forms = (DecisionForm(instance=decision) for decision in decisions)
    context = IndexedOrderedDict()
    context['client'] = referral.client
    context['referral'] = referral
    context['forms'] = forms

    return save_ajax_form(request, context=context, list_template='intake/includes/partial_client_list.html', form_template='intake/includes/partial_client_evaluate.html')


def client_note(request, pk):

    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        form = NoteForm(request.POST, initial={'note_type': 'General'})
    else:
        form = NoteForm(initial={'note_type': 'General'})
    context = IndexedOrderedDict()
    context['client'] = client
    context['forms'] = {'note_form': form}

    return save_ajax_form(request, list_template='intake/includes/partial_client_list.html', form_template='intake/includes/partial_client_note.html', context=context)

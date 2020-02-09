from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, TemplateView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.http import JsonResponse
from django.template.loader import render_to_string
from django_tables2.views import SingleTableView, MultiTableMixin

from scribe.forms import NoteForm, NoteFormSet
from scribe.models import Note
from scribe.tables import NoteTable

from core.helpers import save_ajax_form, paginate_model

from .filters import ClientFilter, ReferralFilter
from ..forms import (ClientForm, ClientFormset, ClientReferralMultiForm,
                     CriminalBackgroundForm, DecisionForm,
                     ReferralDecisionMultiForm, ReferralForm, ReferralQueryForm)
from ..models import Client, CriminalBackground, Decision, Referral
from .tables import ClientTable, ClientCourtTable

from collections import OrderedDict
from indexed import IndexedOrderedDict 


def client_list(request):
    clients = paginate_model(request, Client)
    # import pdb; pdb.set_trace()

    return render(request, 'intake/client_list.html', {'clients': clients})


def add_forms_to_context(forms, context):
    """
        Add multiple different forms to context, with
        model name as prefix.
    """

    context['forms'] = {f'{form.instance._meta.model_name}_form': form for form in forms}

    return context


def client_create(request):
    """
        Handle GET/POST requests and instantiate forms.
    """

    if request.method == 'POST':
        # form = ClientReferralMultiForm(request.POST)
        client_form = ClientForm(request.POST)
        referral_form = ReferralForm(request.POST)
    else:
        # form = ClientReferralMultiForm()
        client_form = ClientForm()
        referral_form = ReferralForm()
    
    forms = (client_form, referral_form)
    context = IndexedOrderedDict()
    context['client'] = None
    context = add_forms_to_context(forms, context)

    return save_ajax_form(
        request, context=context, list_template='intake/includes/partial_client_list.html', form_template='intake/includes/partial_client_create.html')


def client_update(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        client_form = ClientForm(request.POST, instance=client)
        referral_form = ReferralForm(request.POST, instance=client.referral)

    else:  # GET Request (loadForm)

        client_form = ClientForm(instance=client)
        referral_form = ReferralForm(instance=client.referral)

    forms = (client_form, referral_form)
    context = IndexedOrderedDict()
    context['client'] = client
    context = add_forms_to_context(forms, context)

    return save_ajax_form(request, context=context, list_template='intake/includes/partial_client_list.html', form_template='intake/includes/partial_client_update.html')


def client_evaluate(request, pk):

    referral = get_object_or_404(Referral, pk=pk)
    decisions = referral.decisions
    if request.method == 'POST':

        forms = (DecisionForm(request.POST, instance=decision)
                 for decision in decisions)

    else:
        forms = (DecisionForm(instance=decision) for decision in decisions)
    context = IndexedOrderedDict()
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

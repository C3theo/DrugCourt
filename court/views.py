from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.template.loader import render_to_string
from django.views.generic.edit import CreateView, UpdateView
from django_tables2.views import SingleTableView
from indexed import IndexedOrderedDict

from core.helpers import (add_forms_to_context, paginate_model, render_ajax,
                          save_ajax_form)
from court.filters import CourtDateFilter
from court.forms import CourtDateForm, PhaseHistoryForm
from court.models import CourtDates, PhaseHistory
from court.tables import CourtDateTable
from intake.models import Client, IntakeStatus
from scribe.forms import NoteForm


def court_date_list(request):
    """
    """
    court_dates = paginate_model(request, CourtDates)
    return render(request, 'court/court_date_list.html', {'court_dates': court_dates})


def court_date_create(request):
    """
    """
    if request.method == 'POST':
        form = CourtDateForm(request.POST)
    else:
        form = CourtDateForm()
    context = IndexedOrderedDict()
    context['court_date'] = form.instance
    context = add_forms_to_context((form,), context)
    data = save_ajax_form(request, context=context)
    return render_ajax(request, context, data,
                          list_template='court/includes/partial_court_list.html',
                          form_template='court/includes/partial_court_create.html')


def court_date_update(request, pk):
    court = get_object_or_404(CourtDates, pk=pk)

    if request.method == 'POST':
        form = CourtDateForm(request.POST, instance=court)
    else:
        form = CourtDateForm(instance=court)
    context = IndexedOrderedDict()
    context['court_date'] = form.instance
    context = add_forms_to_context((form,), context)
    data = save_ajax_form(request, context=context)
    return render_ajax(request, context, data,
                          list_template='court/includes/partial_court_list.html',
                          form_template='court/includes/partial_court_update.html')


def court_date_note(request, pk):

    client = get_object_or_404(Client, pk=pk)
    initial = {'client': client, 'note_type': 'Court'}
    if request.method == 'POST':
        form = NoteForm(request.POST, initial=initial)
    else:
        form = NoteForm(initial=initial)
    context = IndexedOrderedDict()
    context['court_date'] = form.instance
    context['client'] = client
    context = add_forms_to_context((form,), context)
    data = save_ajax_form(request, context=context)
    return render_ajax(request, context, data,
                          list_template='court/includes/partial_court_list.html',
                          form_template='intake/includes/partial_client_note.html')



def phase_list(request):
    """
    """
    phases = paginate_model(request, PhaseHistory)
    return render(request, 'court/phase_list.html', {'phases': phases})


def phase_create(request):
    """
    """

    if request.method == 'POST':
        form = PhaseHistoryForm(request.POST)
    else:
        form = PhaseHistoryForm()
    context = IndexedOrderedDict()
    context['phase'] = form.instance
    context = add_forms_to_context((form,), context)
    data = save_ajax_form(request, context=context)
    return render_ajax(request, context, data,
                          list_template='court/includes/partial_phase_list.html',
                          form_template='court/includes/partial_phase_create.html')


def phase_update(request, pk):
    phase = get_object_or_404(PhaseHistory, pk=pk)

    if request.method == 'POST':
        form = PhaseHistoryForm(request.POST, instance=court)
    else:
        form = PhaseHistoryForm(instance=court)
    context = IndexedOrderedDict()
    context['phase'] = form.instance
    context = add_forms_to_context((form,), context)
    data = save_ajax_form(request, context=context)
    return render_ajax(request, context, data,
                          list_template='court/includes/partial_phase_list.html',
                          form_template='court/includes/partial_phase_update.html')



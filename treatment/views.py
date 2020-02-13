from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.template.loader import render_to_string
from indexed import IndexedOrderedDict

from core.helpers import add_forms_to_context, paginate_model, save_ajax_form, get_ajax_search_results
from intake.models import Client
from scribe.forms import NoteForm

from .forms import TxAttendanceForm, ObjectivesForm
from .models import TxAttendance, Objectives

# Create your views here.

def objectives_list(request):
    context = get_ajax_search_results(request, model=Objectives)
    
    
    return render(request, 'treatment/objectives_list.html', context)

def objective_create(request):
    if request.method == 'POST':
        form = ObjectivesForm(request.POST)
    else:
        form = ObjectivesForm()
    context = IndexedOrderedDict()
    context['objectives'] = form.instance
    context = add_forms_to_context((form,), context)
    return save_ajax_form(request, context=context,
                          form_template='treatment/includes/partial_objectives_create.html',
                          list_template='treatment/includes/partial_objectives_list.html')

def objective_update(request, pk):
    objectives = get_object_or_404(Objectives, pk=pk)
    if request.method == 'POST':
        form = ObjectivesForm(request.POST, instance=objectives)
    else:
        form = ObjectivesForm(instance=objectives)

    context = IndexedOrderedDict()
    context['objectives'] = form.instance
    context = add_forms_to_context((form,), context)
    return save_ajax_form(request, context=context,
                          form_template='treatment/includes/partial_objectives_update.html',
                          list_template='treatment/includes/partial_objectives_list.html')


def objective_note(request, pk):

    client = get_object_or_404(Client, pk=pk)
    context = {'client': client, 'note_type': 'Treatment'}
    if request.method == 'POST':
        form = NoteForm(request.POST, initial=context)
    else:
        form = NoteForm(initial=context)

    context = IndexedOrderedDict()
    context['client'] = client
    context['forms'] = {'note_form': form}

    return save_ajax_form(request, list_template='treatment/includes/partial_objectives_list.html',
                          form_template='intake/includes/partial_client_note.html',
                          context=context)




def treatment_list(request):

    treatment_list = paginate_model(request, TxAttendance)

    return render(request, 'treatment/treatment_list.html', {'tx_attendances': treatment_list})


def treatment_create(request):
    if request.method == 'POST':
        form = TxAttendanceForm(request.POST)
    else:
        form = TxAttendanceForm()
    context = IndexedOrderedDict()
    context['treatment'] = form.instance
    context = add_forms_to_context((form,), context)
    return save_ajax_form(request, context=context,
                          form_template='treatment/includes/partial_treatment_create.html',
                          list_template='treatment/includes/partial_treatment_list.html')


def treatment_update(request, pk):
    treatment = get_object_or_404(TxAttendance, pk=pk)
    if request.method == 'POST':
        form = TxAttendanceForm(request.POST, instance=treatment)
    else:
        form = TxAttendanceForm(instance=treatment)

    context = IndexedOrderedDict()
    context['treatment'] = form.instance
    context = add_forms_to_context((form,), context)
    return save_ajax_form(request, context=context,
                          form_template='treatment/includes/partial_treatment_update.html',
                          list_template='treatment/includes/partial_treatment_list.html')


def treatment_note(request, pk):

    client = get_object_or_404(Client, pk=pk)
    context = {'client': client, 'note_type': 'Treatment'}
    if request.method == 'POST':
        form = NoteForm(request.POST, initial=context)
    else:
        form = NoteForm(initial=context)

    context = IndexedOrderedDict()
    context['client'] = client
    context['forms'] = {'note_form': form}

    return save_ajax_form(request, list_template='intake/includes/partial_client_list.html',
                          form_template='intake/includes/partial_client_note.html',
                          context=context)

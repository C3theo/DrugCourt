from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.template.loader import render_to_string
from indexed import IndexedOrderedDict
from rest_framework import viewsets

from core.helpers import (add_forms_to_context, get_ajax_search_results,
                          paginate_model, render_ajax, save_ajax_form)
from intake.models import Client
from scribe.forms import NoteForm

from .forms import ObjectivesForm, ProbGoalsForm, TxAttendanceForm
from .models import Objectives, TxAttendance, ProbGoals
from .serializers import ObjectivesSerializer, ProbGoalsSerializer


class ClientObjectivesList(viewsets.ModelViewSet):
    """
    API endpoint that allows objectives to be viewed or edited.
    """

    # queryset = Objectives.objects.all().order_by('-obj_target')
    serializer_class = ObjectivesSerializer

    def get_queryset(self):
        client_pk = self.kwargs['pk']
        return Objectives.objects.filter(client__pk=client_pk)


class ObjectivesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Objectives.objects.all().order_by('-obj_target')
    serializer_class = ObjectivesSerializer

    # def get_queryset(self):
    #     client_pk = self.kwargs['pk']
    #     return Purchase.objects.filter(client__pk=client_pk)


class ProbGoalsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = ProbGoals.objects.all()
    serializer_class = ProbGoalsSerializer


def goal_create(request, pk):
    """
    """
    objective = get_object_or_404(Objectives, pk=pk)

    initial = {'objective': objective, 'client': objective.client}
    if request.method == 'POST':
        form = ProbGoalsForm(request.POST, initial=initial)
    else:
        form = ProbGoalsForm(initial=initial)
    context = IndexedOrderedDict()
    context['goal'] = form.instance
    context['objective'] = objective
    context['initial'] = initial
    context = add_forms_to_context((form,), context)
    data = save_ajax_form(request, context=context)
    return render_ajax(request, context, data,
                       form_template='treatment/includes/partial_goal_create.html',
                       list_template='treatment/includes/partial_objectives_list.html')


def goal_update(request, pk):
    goal = get_object_or_404(ProbGoals, pk=pk)
    if request.method == 'POST':
        form = ProbGoalsForm(request.POST, instance=goal)
    else:
        form = ProbGoalsForm(instance=goal)
    # import pdb; pdb.set_trace()
    context = IndexedOrderedDict()
    context['goal'] = form.instance
    context['objective'] = goal.objective
    initial = {'objective': goal.objective, 'client': goal.objective.client}
    context['initial'] = initial
    context = add_forms_to_context((form,), context)
    data = save_ajax_form(request, context=context)
    return render_ajax(request, context, data,
                       form_template='treatment/includes/partial_goal_update.html',
                       list_template='treatment/includes/partial_objectives_list.html')


def objectives_list(request):
    context = get_ajax_search_results(request, model=Objectives)

    return render(request, 'treatment/objectives_list.html', context)


def objective_create(request, id):
    """
    """

    if request.method == 'POST':
        form = ObjectivesForm(request.POST)
    else:
        form = ObjectivesForm()
    if id:
        client = get_object_or_404(Client, pk=id)
        initial = {'client': client}

    context = IndexedOrderedDict()
    context['objective'] = form.instance
    context['initial'] = initial
    context['client'] = client
    context = add_forms_to_context((form,), context)
    data = save_ajax_form(request, context=context)
    return render_ajax(request, context, data,
                       form_template='treatment/includes/partial_objectives_create.html',)


def objective_update(request, pk):
    objectives = get_object_or_404(Objectives, pk=pk)
    if request.method == 'POST':
        form = ObjectivesForm(request.POST, instance=objectives)
    else:
        form = ObjectivesForm(instance=objectives)

    context = IndexedOrderedDict()
    context['objectives'] = form.instance
    context = add_forms_to_context((form,), context)
    data = save_ajax_form(request, context=context)
    return render_ajax(request, context, data,
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
    data = save_ajax_form(request, context=context)
    return render_ajax(request, context, data,
                       list_template='treatment/includes/partial_objectives_list.html',
                       form_template='intake/includes/partial_client_note.html',)


def treatment_list(request):

    treatment_list = paginate_model(request, TxAttendance)

    return render(request, 'treatment/treatment_list.html', {'tx_attendances': treatment_list})


def treatment_create(request, id):
    """
    """
    if request.method == 'POST':
        form = TxAttendanceForm(request.POST)
    else:
        form = TxAttendanceForm()

    client = get_object_or_404(Client, pk=id)
    initial = {'client': client}
    context = IndexedOrderedDict()
    context['treatment'] = form.instance
    context['initial'] = initial
    context['client'] = client
    context = add_forms_to_context((form,), context)
    data = save_ajax_form(request, context=context)
    return render_ajax(request, context, data,
                       form_template='treatment/includes/partial_treatment_create.html',)
    #    list_template='treatment/includes/partial_treatment_list.html')


def treatment_update(request, pk):
    treatment = get_object_or_404(TxAttendance, pk=pk)
    if request.method == 'POST':
        form = TxAttendanceForm(request.POST, instance=treatment)
    else:
        form = TxAttendanceForm(instance=treatment)

    context = IndexedOrderedDict()
    context['treatment'] = form.instance
    context = add_forms_to_context((form,), context)
    data = save_ajax_form(request, context=context)
    return render_ajax(request, context, data,
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
    data = save_ajax_form(request, context=context)
    return render_ajax(request, context, data,
                       list_template='intake/includes/partial_client_list.html',
                       form_template='intake/includes/partial_client_note.html',)

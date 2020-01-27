from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template.loader import render_to_string

from intake.models import Client
from scribe.forms import NoteForm

from .models import TxAttendance
from .forms import TxAttendanceForm

# Create your views here.


def treatment_list(request):

    treatment_list = TxAttendance.objects.all()

    page = request.GET.get('page', 1)

    paginator = Paginator(treatment_list, 25)
    try:
        treatment = paginator.page(page)
    except PageNotAnInteger:
        treatment = paginator.page(1)
    except EmptyPage:
        treatment = paginator.page(paginator.num_pages)

    return render(request, 'treatment/treatment_list.html', {'treatment': treatment})


def save_treatment_form(request, form, template_name, context=None):
    data = dict()

    if request.method == 'POST':

        if form.is_valid():
            try:
                note = form.save(commit=False)
                note.client = context['client']
                note.author = request.user
                note.save()
                
            except KeyError:
                form.save()

            data['form_is_valid'] = True
            
            treatment_list = TxAttendance.objects.all()
            page = request.GET.get('page', 1)

            paginator = Paginator(treatment_list, 25)
            try:
                treatment = paginator.page(page)
            except PageNotAnInteger:
                treatment = paginator.page(1)
            except EmptyPage:
                treatment = paginator.page(paginator.num_pages)

            # TODO
            data['html_treatment_list'] = render_to_string(
                'treatment/includes/partial_treatment_list.html', {'treatment': treatment})
        else:
            data['form_is_valid'] = False
    
    if context:
        context['form'] = form
    else:
        context = {"form": form}

    data['html_form'] = render_to_string(template_name,
                                         context,
                                         request=request
                                         )
    return JsonResponse(data)


def treatment_create(request):
    if request.method == 'POST':
        form = TxAttendanceForm(request.POST)
    else:
        form = TxAttendanceForm()
    return save_treatment_form(request, form, 'treatment/includes/partial_treatment_create.html')


def treatment_update(request, pk):
    treatment = get_object_or_404(TxAttendance, pk=pk)
    if request.method == 'POST':
        form = TxAttendanceForm(request.POST, instance=treatment)
    else:
        form = TxAttendanceForm(instance=treatment)

    return save_treatment_form(request, form, 'treatment/includes/partial_treatment_update.html')


def treatment_note(request, pk):

    client = get_object_or_404(Client, pk=pk)
    context = {'client': client, 'note_type': 'Treatment'}
    if request.method == 'POST':
        form = NoteForm(request.POST, initial=context)
    else:
        form = NoteForm(initial=context)

    return save_treatment_form(request, form, 'treatment/includes/partial_treatment_note.html', context=context)

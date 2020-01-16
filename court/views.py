# Create your views here.
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django_tables2.views import SingleTableView
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string

from court.models import CourtDates
from court.forms import CourtDateForm
from court.tables import CourtDateTable
from court.filters import CourtDateFilter

from intake.models import IntakeStatus, Client
from scribe.forms import NoteForm


def court_date_list(request):
    court_dates = CourtDates.objects.all()
    return render(request, 'court/court_date_list.html', {'court_dates': court_dates})


def save_court_form(request, form, template_name):
    data = dict()

    if request.method == 'POST':

        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            court_dates = CourtDates.objects.all()
            data['html_court_list'] = render_to_string('court/includes/partial_court_list.html', {'court_dates': court_dates})
        else:
            data['form_is_valid'] = False

    context = {'form': form}
    data['html_form'] = render_to_string(template_name,
                                         context,
                                         request=request
                                         )
    return JsonResponse(data)

def court_date_create(request):
    if request.method == 'POST':
        form = CourtDateForm(request.POST)
    else:
        form = CourtDateForm()
    return save_court_form(request, form, 'court/includes/partial_court_create.html')

def court_date_update(request, pk):
    court = get_object_or_404(CourtDates, pk=pk)
    
    if request.method == 'POST':
        form = CourtDateForm(request.POST, instance=court)
    else:
        form = CourtDateForm(instance=court)
    return save_court_form(request, form, 'court/includes/partial_court_update.html')


class ClientCourtDateView(LoginRequiredMixin, SingleTableView):
    """
        View to display CourtDate data
    """

    template_name = 'intake/court_date_table.html'
    table_class = CourtDateTable
    filterset_class = CourtDateFilter
    model = Client


def court_date_client_list(request):

    qs = CourtDates.objects.filter(
        client__status__contains=IntakeStatus.STATUS_ACCEPTED)
    table = CourtDateTable(qs)
    f = CourtDateFilter(request.GET, queryset=qs)

    return render(request, 'court/court_filter.html', {'filter': f, 'table': table})


class CourtDateView(CreateView):
    model = CourtDates
    form_class = CourtDateForm
    template_name = 'court/court_date_form.html'

# TODO: remove Client Drop Down


class CourtDateUpdateView(UpdateView):
    model = CourtDates
    form_class = CourtDateForm
    template_name = 'court/court_date_form.html'

    def get_context_data(self, **kwargs):
        """
            Initialize NoteForm with Client and pass to context.
        """

        note_form = NoteForm(prefix='note')

        context = {'note_form': note_form}
        return super().get_context_data(**context)


class CourtDateListView(LoginRequiredMixin, SingleTableView):
    model = CourtDates
    table_class = CourtDateTable
    template_name = 'court/court_date_table.html'
    context_object_name = 'court_date'

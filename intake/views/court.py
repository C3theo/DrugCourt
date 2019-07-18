from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django_tables2.views import SingleTableView
from django.shortcuts import render

from intake.models import CourtDate
from intake.forms import CourtDateForm

from .tables import CourtDateTable
from .filters import CourtDateFilter

def court_date_client_list(request):
    f = CourtDateFilter(request.GET, queryset=CourtDate.objects.all())
    return render(request, 'intake/court_filter.html', {'filter': f}) 

class CourtDateView(CreateView):
    model = CourtDate
    form_class = CourtDateForm
    template_name = 'intake/court_date_form.html'

class CourtDateDetailView(UpdateView):
    model = CourtDate
    form_class = CourtDateForm
    template_name = 'intake/court_date_form.html'

class CourtDateListView(LoginRequiredMixin, SingleTableView):
    model = CourtDate
    table_class = CourtDateTable
    template_name = 'intake/court_date_table.html'
    context_object_name = 'court_date'
# Create your views here.
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django_tables2.views import SingleTableView
from django.shortcuts import render

from court.models import CourtDates
from court.forms import CourtDateForm

from .tables import CourtDateTable
from .filters import CourtDateFilter

def court_date_client_list(request):
    f = CourtDateFilter(request.GET, queryset=CourtDates.objects.all())
    return render(request, 'court/court_filter.html', {'filter': f}) 

class CourtDateView(CreateView):
    model = CourtDates
    form_class = CourtDateForm
    template_name = 'court/court_date_form.html'

class CourtDateUpdateView(UpdateView):
    model = CourtDates
    form_class = CourtDateForm
    template_name = 'court/court_date_form.html'

    def get_context_data(self, **kwargs):
        """
            Initialize NoteForm with Client and pass to context
        """
        
        note_form = NoteForm(prefix='note')
        context = {'note_form': note_form}
        return super().get_context_data(**context)
    
class CourtDateListView(LoginRequiredMixin, SingleTableView):
    model = CourtDates
    table_class = CourtDateTable
    template_name = 'court/court_date_table.html'
    context_object_name = 'court_date'
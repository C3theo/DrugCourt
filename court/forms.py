from crispy_forms import bootstrap
from crispy_forms.helper import FormHelper
from crispy_forms.layout import (HTML, Button, Div, Field, Fieldset, Layout,
                                 Row, Submit)
from django.forms import ModelForm
from django.forms.widgets import CheckboxInput, DateInput

from court.models import CourtDates, PhaseHistory


class CourtDateForm(ModelForm):
    court_date = DateInput(attrs={'type': 'date'})

    def __init__(self, *args, **kwargs):
        super(CourtDateForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_tag = False

    class Meta:
        model = CourtDates
        fields = ['court_date', 'client', 'event',
                  'court_date_type', 'attendance']

        widgets = {'attendance': CheckboxInput,
                   'court_date': DateInput(attrs={'type': 'date'})}


class PhaseHistoryForm(ModelForm):
    start_date = DateInput(attrs={'type': 'date'})
    complete_date = DateInput(attrs={'type': 'date'})

    def __init__(self, *args, **kwargs):
        super(PhaseHistoryForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_tag = False

    class Meta:
        model = PhaseHistory
        fields = ['client', 'phase', 'start_date',
                  'complete_date', 'complete', 'total_days']

        widgets = {'start_date': DateInput(attrs={'type': 'date'}),
                   'complete_date': DateInput(attrs={'type': 'date'})}

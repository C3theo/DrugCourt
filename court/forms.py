from django.forms import ModelForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Button, Submit, Div, Field, Row, HTML
from crispy_forms import bootstrap
from django.forms.widgets import CheckboxInput
from court.models import CourtDates


class CourtDateForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(CourtDateForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_tag = False

    class Meta:
        model = CourtDates
        fields = ['court_date', 'client_ID', 'event',
                  'court_date_type', 'attendance']

        widgets = {'attendance': CheckboxInput}

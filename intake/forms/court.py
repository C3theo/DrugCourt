from django.forms import ModelForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Button, Submit, Div, Field, Row, HTML
from crispy_forms import bootstrap

from intake.models import CourtDate


class CourtDateForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(CourtDateForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_tag = False

    class Meta:
        model = CourtDate
        fields = ['court_date', 'client', 'event',
                  'court_date_type', 'attendance']

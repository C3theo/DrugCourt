
from braces.forms import UserKwargModelFormMixin
from crispy_forms import bootstrap
from crispy_forms.helper import FormHelper
from crispy_forms.layout import (HTML, TEMPLATE_PACK, Button, Div, Field,
                                 Fieldset, Layout, LayoutObject, Row, Submit, ButtonHolder)
from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from django.template.loader import render_to_string
from django_fsm import TransitionNotAllowed

from .custom_formset import Formset
from intake.models import Client, Decision, Note, Referral, CriminalBackground


class ClientFormset(ModelForm):

    def __init__(self, *args, **kwargs):
        super(ClientFormset, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3 create-label'
        self.helper.field_class = 'col-md-9'
        self.helper.layout = Layout(
            Div(
                Field('birth_date'),
                Field('first_name'),
                Field('last_name'),
                HTML('<hr pb-1>'),
                Fieldset('Add Notes',
                         Formset('client_notes')),
                ButtonHolder(Submit('submit', 'Save')),
            ))

    class Meta:
        model = Client
        fields = ['birth_date', 'gender', 'first_name',
                  'middle_initial', 'last_name']

        labels = {
            'middle_initial': 'M.I.'
        }


class ClientForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_tag = False

    class Meta:
        model = Client
        fields = ['birth_date', 'gender', 'first_name',
                  'middle_initial', 'last_name']

        labels = {
            'middle_initial': 'M.I.'
        }


class NoteForm(ModelForm):

    class Meta:
        model = Note
        fields = ['text', 'note_type']

        labels = {
            'text': 'Client Notes', }


NoteFormSet = inlineformset_factory(
    Client, Note, form=NoteForm, extra=1, fields=['text', 'note_type'])


class ReferralForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(ReferralForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_tag = False

    class Meta:
        model = Referral
        fields = ['referrer', 'provider']


# ReferralDecisonFormset = inlineformset_factory(
#     Referral, Decision, extra=3, fields=['status'])


class DecisionForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(DecisionForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_tag = False

    class Meta:
        model = Decision
        fields = ['date_received', 'date_completed', 'referral', 'verdict']

        labels = {
            'verdict': 'Approved', }


class CriminalBackgroundForm(ModelForm):
    """
        Form for CriminalBackground Model
    """

    def __init__(self, *args, **kwargs):
        super(CriminalBackgroundForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_tag = False

    class Meta:
        model = CriminalBackground
        fields = [
            'client',
            'arrests',
            'felonies',
            'misdemeanors',
            'firstarrestyear']
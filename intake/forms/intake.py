
from braces.forms import UserKwargModelFormMixin
from crispy_forms import bootstrap
from crispy_forms.helper import FormHelper
from crispy_forms.layout import (HTML, TEMPLATE_PACK, Button, ButtonHolder,
                                 Div, Field, Fieldset, Layout, LayoutObject,
                                 Row, Submit)
from django.forms import ModelChoiceField, ModelForm, ModelMultipleChoiceField
from django.forms.models import inlineformset_factory
from django.forms.widgets import TextInput, DateInput
from django.template.loader import render_to_string
from django_fsm import TransitionNotAllowed


from intake.models import Client, CriminalBackground, Decision, Referral
from scribe.models import Note
from scribe.forms import NoteForm

from .custom_formset import Formset


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
            'middle_initial': 'M.I.',
        }


class ClientForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_tag = False

    class Meta:
        model = Client
        fields = ['birth_date', 'gender', 'first_name', 'status',
                  'middle_initial', 'last_name', 'ssn']

        labels = {
            'middle_initial': 'M.I.',
            'ssn': 'SSN'
        }


class ReferralForm(ModelForm):
    date_received = DateInput(attrs={'type': 'date'})

    def __init__(self, *args, **kwargs):
        super(ReferralForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_tag = False

    class Meta:
        model = Referral
        fields = ('client', 'referrer', 'provider', 'date_received')
        widgets = {'date_received': DateInput(attrs={
                'type': 'date'
            })}


class ReferralEvalForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(ReferralEvalForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_tag = False

    class Meta:
        model = Referral
        fields = ['provider',
                  'date_received', 'date_completed']



class DecisionForm(ModelForm):

    date_received = DateInput(attrs={'type': 'date'})

    def __init__(self, *args, **kwargs):
        """
            Change made_by field to readonly
        """
        super(DecisionForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['made_by'].widget.attrs['readonly'] = True
        self.helper = FormHelper(self)
        self.helper.form_tag = False

    class Meta:
        model = Decision
        fields = ['made_by', 'date_received', 'verdict']
        widgets = {
            'made_by': TextInput(),
            'date_received': DateInput(attrs={
                'type': 'date'
            })
        }

        labels = {
            'verdict': 'Decision',
            'made_by': 'Deciding Party'}


# class ReferralDecisionMultiForm(MultiModelForm):
#     form_classes = {
#         'referral': ReferralEvalForm,
#         'pre_decision': DecisionForm,
#         'da_decision': DecisionForm,
#         'dc_decision': DecisionForm,
#     }

#     def save(self, commit=True):
#         """
#             Save decisions before Referral
#         """
        
    
#         objects = super(ReferralDecisionMultiForm, self).save(commit=True)
#         if commit:
#             referral = objects['referral']
#             if referral.all_decisions_approved():
#                 referral.approve()
#             referral.save()
#         return objects


# ReferralDecisonFormset = inlineformset_factory(
#     Referral, Decision, extra=3, fields=['status'])

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
            'first_arrest_year']


class ReferralQueryForm(ModelForm):

    client = ModelMultipleChoiceField(queryset=None)

    def __init__(self, client=None, *args, **kwargs):
        super(ReferralQueryForm, self).__init__(*args, **kwargs)
        self.fields['client'].queryset = Client.objects.filter(pk=client.id)

    class Meta:
        model = Referral
        fields = ['client', 'status', 'referrer',
                  'date_received', 'date_completed']

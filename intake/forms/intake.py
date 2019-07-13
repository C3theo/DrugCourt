
from django.forms.models import formset_factory
from django.forms import ModelForm

from braces.forms import UserKwargModelFormMixin
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Button, Submit, Div, Field, Row, HTML
from crispy_forms import bootstrap
from django_fsm import TransitionNotAllowed

from ..models import Client, Referral, Note, Decision


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


class ReferralForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(ReferralForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_tag = False


    class Meta:
        model = Referral
        fields = ['referrer', 'client']

# What is this braces mixin doing?
class NoteForm(UserKwargModelFormMixin, ModelForm):

    def __init__(self, *args, **kwargs):
        super(NoteForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_tag = False

    def save(self, *args, **kwargs):

        if not self.instance.pk:
            self.instance.author = self.user

        return super().save()

    class Meta:
        model = Note
        fields = ['text', 'created_date', 'client']

        labels = {
            'text': 'Client Notes', }


class DecisionForm(UserKwargModelFormMixin, ModelForm):

    def __init__(self, *args, **kwargs):
        super(DecisionForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_tag = False

    #TODO: Save logged in user
    def save(self, *args, **kwargs):

        return super().save()

    class Meta:
        model = Decision
        fields = ['date_received', 'date_completed', 'referral', 'verdict']

        # labels = {
        #     'text': 'Client Decisions', }


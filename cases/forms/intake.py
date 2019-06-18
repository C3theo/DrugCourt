
from django.forms.models import formset_factory
from django.forms import ModelForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Button, Submit, Div, Field, Row, HTML
from crispy_forms import bootstrap
from django_fsm import TransitionNotAllowed

from ..models import Client, Referral, Note


class ClientForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)

        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)
        self.helper.form_tag = False

        # You can dynamically adjust your layout

    class Meta:
        model = Client
        exclude = ['client_id', 'status', 'created_date']

        labels = {
            'middle_initial': 'M.I.'
        }


class ReferralForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(ReferralForm, self).__init__(*args, **kwargs)

        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)

        # You can dynamically adjust your layout

    class Meta:
        model = Referral
        # exclude = ['status']
        fields = '__all__'


class NoteForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(NoteForm, self).__init__(*args, **kwargs)

        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)
        self.helper.form_tag = False

        # You can dynamically adjust your layout
    
    def save(self, *args, **kwargs):

        if not self.instance.pk:
            self.author = self.request.user
        super().save()

    class Meta:
        model = Note
        fields = ['text', 'created_date']

        labels = {
            'text': 'Client Notes', }

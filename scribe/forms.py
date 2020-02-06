"""
    Forms for Scribe app
"""
from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from django.forms.widgets import TextInput

from crispy_forms.helper import FormHelper

from intake.models import Client
from .models import Note


class NoteForm(ModelForm):

    def __init__(self, *args, **kwargs):
        """
            Change client field to readonly, and add
        """

        # self.client = kwargs.pop('client')
        super(NoteForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance:
            self.fields['note_type'].widget.attrs['readonly'] = True
        self.helper = FormHelper(self)
        self.helper.form_tag = False

    class Meta:
        model = Note
        fields = ['client', 'text', 'note_type']
        widgets = {
            'note_type': TextInput(),}
        labels = {
            'text': 'Client Notes', }

NoteFormSet = inlineformset_factory(
    Client, Note, form=NoteForm, extra=1, fields=['text'])

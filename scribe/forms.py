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
            Change client field to readonly
        """
        super(NoteForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['client'].widget.attrs['readonly'] = True
        self.helper = FormHelper(self)
        self.helper.form_tag = False

    class Meta:
        model = Note
        fields = ['client', 'text', 'note_type']

        labels = {
            'text': 'Client Notes', }
        
        # widgets = {
        #     'client': TextInput()
        # } 


NoteFormSet = inlineformset_factory(
    Client, Note, form=NoteForm, extra=1, fields=['text'])

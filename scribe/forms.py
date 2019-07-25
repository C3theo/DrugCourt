"""
    Scribe Forms
"""
from django.forms import ModelForm
from django.forms.models import inlineformset_factory

from intake.models import Client

from .models import Note


class NoteForm(ModelForm):

    class Meta:
        model = Note
        fields = ['text', 'note_type']

        labels = {
            'text': 'Client Notes', }


NoteFormSet = inlineformset_factory(
    Client, Note, form=NoteForm, extra=1, fields=['text', 'note_type'])

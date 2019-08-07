import django_tables2 as tables
from django_tables2.utils import A

from .models import Note

class NoteTable(tables.Table):

    class Meta:

        model = Note
        template_name = 'django_tables2/bootstrap4.html'
        fields = ['author', 'text', 'created_date', 'client']
        attrs = {'th': {'class': 'table-light'},
                 'class': 'table table-striped table-light'
                 }

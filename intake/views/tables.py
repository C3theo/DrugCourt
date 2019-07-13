import django_tables2 as tables
from django_tables2.utils import A

from intake.models import Client, Note


class ClientTable(tables.Table):
    # client_id = tables.LinkColumn('referrals-update', args=[A('clientid')])

    class Meta:
        model = Client
        template_name = 'django_tables2/bootstrap4.html'
        fields = ['client_id', 'first_name', 'last_name']


class NoteTable(tables.Table):

    class Meta:
        
        model = Note
        template_name = 'django_tables2/bootstrap4.html'
        fields = ['author', 'text', 'created_date', 'client']
        attrs = {'th': {'class': 'table-light'},
        'class': 'table table-striped table-light'
        }

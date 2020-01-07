import django_tables2 as tables
from django_tables2.utils import A
from django_tables2.columns import Column

from intake.models import Client


class ClientTable(tables.Table):
    pk = tables.LinkColumn('intake:detail', args=[A('pk')])

    class Meta:
        model = Client
        template_name = 'django_tables2/bootstrap4.html'
        fields = ['pk', 'client_id', 'first_name', 'last_name']


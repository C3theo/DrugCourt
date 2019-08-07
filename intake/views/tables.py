import django_tables2 as tables
from django_tables2.utils import A

from intake.models import Client, CourtDate


class ClientTable(tables.Table):
    pk = tables.LinkColumn('intake:detail', args=[A('pk')])

    class Meta:
        model = Client
        template_name = 'django_tables2/bootstrap4.html'
        fields = ['pk', 'client_id', 'first_name', 'last_name']

class CourtDateTable(tables.Table):

    class Meta:
        model = CourtDate
        template_name = 'django_tables2/bootstrap4.html'
        fields = ['court_date', 'client', 'event',
                  'court_date_type', 'attendance']
        attrs = {'th': {'class': 'table-light'},
                 'class': 'table table-striped table-light'
                 }

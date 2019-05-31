import django_tables2 as tables
from .models import Clients

class ClientsTable(tables.Table):

    class Meta:
        model = Clients
        template_name = 'django_tables2/bootstrap4.html'
        fields = ['clientid', 'startdate', 'dischargedate']

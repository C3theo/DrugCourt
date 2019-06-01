import django_tables2 as tables
from django_tables2.utils import A
from .models import Clients, Referrals

class ClientsTable(tables.Table):
    clientid = tables.LinkColumn('referrals-update', args=[A('clientid')])
    class Meta:
        model = Clients
        template_name = 'django_tables2/bootstrap4.html'
        fields = ['clientid', 'startdate', 'dischargedate']


class ReferralsTable(tables.Table):
    firstname = tables.LinkColumn('referrals-update', args=[A('refid')])
    class Meta:
        model = Referrals
        template_name = 'django_tables2/bootstrap4.html'
        fields = ['refid', 'clientid', 'firstname', 'middlename', 'lastname']
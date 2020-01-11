import django_tables2 as tables
from django_tables2.utils import A
from django_tables2.columns import Column

from intake.models import Client, CourtDate


class ClientTable(tables.Table):
    # import pdb; pdb.set_trace()
    
    # pk = tables.LinkColumn('intake:referral-detail', args=[A('client.pk')])
    referral = Column(linkify=True)
    # referral = Column(linkify=("intake:referral-detail", (A("client.referral"), )))
    
    class Meta:
        model = Client
        template_name = 'django_tables2/bootstrap4.html'
        fields = ('referral', 'first_name', 'last_name', 'status')


class CourtDateTable(tables.Table):
    court_date = Column(linkify=True)
    class Meta:
        model = CourtDate
        template_name = 'django_tables2/bootstrap4.html'
        fields = ['court_date', 'client', 'event',
                  'court_date_type', 'attendance']
        attrs = {'th': {'class': 'table-light'},
                 'class': 'table table-striped table-light'
                 }

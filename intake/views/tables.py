import django_tables2 as tables
from django_tables2.utils import A
from django_tables2.columns import Column

from intake.models import Client


class ClientTable(tables.Table):
    # import pdb; pdb.set_trace()
    
    # pk = tables.LinkColumn('intake:referral-detail', args=[A('client.pk')])
    referral = Column(linkify=True)
    # referral = Column(linkify=("intake:referral-detail", (A("client.referral"), )))
    
    class Meta:
        model = Client
        template_name = 'django_tables2/bootstrap4.html'
        fields = ('referral', 'first_name', 'last_name', 'status')



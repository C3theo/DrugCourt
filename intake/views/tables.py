import django_tables2 as tables
from django_tables2.utils import A
from django_tables2.columns import Column

from intake.models import Client


class ClientTable(tables.Table):

    referral = Column('C', linkify=True)
    
    class Meta:
        model = Client
        template_name = 'django_tables2/bootstrap4.html'
        fields = ('referral', 'first_name', 'last_name', 'status')
        attrs = {'th': {'class': 'table-light'},
                 'class': 'table table-striped table-light'
                 }


class ClientCourtTable(tables.Table):
    class Meta:
        model = Client
        template_name = 'django_tables2/bootstrap4.html'
        fields = ('first_name', 'last_name', 'status')



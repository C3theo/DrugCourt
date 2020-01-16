import django_tables2 as tables
from django_tables2.utils import A
from django_tables2.columns import Column

from court.models import CourtDates



class CourtDateTable(tables.Table):
    court_date = Column(linkify=True)
    
    class Meta:
        model = CourtDates
        template_name = 'django_tables2/bootstrap4.html'
        fields = ['client__full_name', 'court_date', 'event',
                  'court_date_type', 'attendance']
        attrs = {'th': {'class': 'table-light'},
                 'class': 'table table-striped table-light'
                 }

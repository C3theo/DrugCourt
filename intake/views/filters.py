import django_filters
from intake.models import Client, CourtDate

class ClientFilter(django_filters.FilterSet):
    class Meta:
        model = Client
        fields = ['client_id']
    
class CourtDateFilter(django_filters.FilterSet):
    # court_date = django_filters.NumberFilter()
    # court_date__gt = django_filters.NumberFilter(field_name='court_date', lookup_expr='date__gt')
    # court_date__lt = django_filters.NumberFilter(field_name='court_date', lookup_expr='date__lt')
    
    class Meta:
        model = CourtDate
        fields = ['client']



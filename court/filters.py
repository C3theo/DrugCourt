from django_filters import FilterSet, ModelChoiceFilter

from court.models import CourtDates

class CourtDateFilter(FilterSet):
    # court_date = django_filters.NumberFilter()
    # court_date__gt = django_filters.NumberFilter(field_name='court_date', lookup_expr='date__gt')
    # court_date__lt = django_filters.NumberFilter(field_name='court_date', lookup_expr='date__lt')
    
    class Meta:
        model = CourtDates
        fields = ['client_ID']



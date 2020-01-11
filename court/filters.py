from django_filters import FilterSet, ModelChoiceFilter, CharFilter

from court.models import CourtDates

class CourtDateFilter(FilterSet):

    # client__status = CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = CourtDates
        fields = ['client']
        # fields = ['client__first_name']



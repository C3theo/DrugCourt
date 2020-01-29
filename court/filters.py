from django_filters import FilterSet, ModelChoiceFilter, CharFilter

from court.models import CourtDates

class CourtDateFilter(FilterSet):
    
    class Meta:
        model = CourtDates
        # fields = ['client']
        fields = ['client__first_name', 'client__last_name']



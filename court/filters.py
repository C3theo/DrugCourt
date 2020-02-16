from django_filters import FilterSet, ModelChoiceFilter, CharFilter

from court.models import CourtDate

class CourtDateFilter(FilterSet):
    
    class Meta:
        model = CourtDate
        # fields = ['client']
        fields = ['client__first_name', 'client__last_name']



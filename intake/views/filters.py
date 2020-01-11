from django_filters import FilterSet, ModelChoiceFilter

from intake.models import Client, CourtDate, Referral


class ReferralFilter(FilterSet):
    client = ModelChoiceFilter(queryset=Client.objects.all())

    class Meta:
        model = Referral
        fields = ['client']


class ClientFilter(FilterSet):
    class Meta:
        model = Client
        fields = ['client_id']
    
class CourtDateFilter(FilterSet):
    # court_date = django_filters.NumberFilter()
    # court_date__gt = django_filters.NumberFilter(field_name='court_date', lookup_expr='date__gt')
    # court_date__lt = django_filters.NumberFilter(field_name='court_date', lookup_expr='date__lt')
    class Meta:
        model = CourtDate
        fields = ['client']



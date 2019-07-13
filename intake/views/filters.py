import django_filters
from intake.models import Client

class ClientFilter(django_filters.FilterSet):
    class Meta:
        model = Client
        fields = ['client_id']



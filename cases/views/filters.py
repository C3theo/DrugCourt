import django_filters
from .models import Clients

class ClientFilter(django_filters.FilterSet):
    class Meta:
        model = Clients
        fields = ['client_id']



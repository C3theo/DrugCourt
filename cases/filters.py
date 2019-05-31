import django_filters
from .models import Clients

class ClientsFilter(django_filters.FilterSet):
    class Meta:
        model = Clients
        fields = ['clientid', 'userid']
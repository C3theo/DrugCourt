from django_filters import FilterSet, ModelChoiceFilter

from intake.models import Client, Referral


class ReferralFilter(FilterSet):
    client = ModelChoiceFilter(queryset=Client.objects.all())

    class Meta:
        model = Referral
        fields = ['client']

class ClientFilter(FilterSet):
    class Meta:
        model = Client
        fields = ['client_id']


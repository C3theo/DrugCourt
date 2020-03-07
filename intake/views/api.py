from rest_framework import viewsets

from intake.serializers import ClientSerializer, ReferralSerializer
from intake.models import Client, Referral


class ClientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Client.objects.all().order_by('status')
    serializer_class = ClientSerializer


class ReferralViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Referral.objects.all()
    serializer_class = ReferralSerializer

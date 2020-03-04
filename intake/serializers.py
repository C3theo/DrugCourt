from rest_framework import serializers

from .models import Client, Referral

class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ['birth_date', 'gender', 'first_name', 'status',
                  'middle_initial', 'last_name', 'ssn']

class ReferralSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Referral
        fields = ('client', 'referrer', 'provider', 'date_received')
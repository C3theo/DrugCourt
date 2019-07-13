import logging
from datetime import date
from random import randrange

from django.utils import timezone

import factory
from factory import DjangoModelFactory

from ..intake import Client, Referral, GenderOption
import string


class ClientFactory(DjangoModelFactory):

    class Meta:
        model = Client
        django_get_or_create = ('client_id', 'birth_date',
                                'created_date', 'gender', 'first_name', 'middle_initial', 'last_name',
                                )

    client_id = factory.Sequence(lambda n: f'{int(2019000) + n}')
    # TODO: figure out how to generate this based off decisions
    # status = factory.Faker('random_element', elements=[
    #                        x[0] for x in IntakeStatus.CHOICES])
    birth_date = factory.Faker('date_of_birth')
    created_date = timezone.now()
    gender = factory.Faker('random_element', elements=[
                           x[0] for x in GenderOption.CHOICES])
    first_name = factory.Faker('first_name')
    middle_initial = factory.Faker('random_element', elements=list(string.ascii_uppercase))
    last_name = factory.Faker('last_name')

    @classmethod
    def _setup_next_sequence(cls):
        try:
            return Client.objects.latest('pk').pk + 1
        except Client.DoesNotExist:
            return 1



import logging
from datetime import date
from random import randrange

from django.utils import timezone
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save

import factory
from factory import DjangoModelFactory

from ..intake import GenderOption
from intake.models import Client, Referral
from court.models import Phase
from intake.models.intake import IntakeStatus
# from profiles.models import Profile
from scribe.models import Note
import string

User = get_user_model()
tzinfo = timezone.get_current_timezone()

def delete_factory_inventory(factory_cls):

    model = factory_cls._meta.model
    inventory = model.objects.all()
    for each in inventory:
        each.delete()

    return f'{len(inventory)} objects deleted'


# @factory.django.mute_signals(post_save)
# class ProfileFactory(DjangoModelFactory):

#     class Meta:
#         model = Profile
#         # django_get_or_create = ('user', 'user_role')

#     user = factory.SubFactory(
#         'intake.models.factories.UserFactory', profile=None)
#     user_role = factory.Faker('random_element', elements=[
#         x[0] for x in Profile.USER_ROLES])


@factory.django.mute_signals(post_save)
class UserFactory(DjangoModelFactory):

    class Meta:
        model = User
        # django_get_or_create = ('username', 'password')

    username = factory.Sequence(lambda n: f'username{n}')
    password = factory.Sequence(lambda n: f'password{n}')

    # profile = factory.RelatedFactory(ProfileFactory, 'user')

    @classmethod
    def _setup_next_sequence(cls):
        # import pdb
        # pdb.set_trace()
        try:
            return User.objects.latest('pk').pk + 1
        except User.DoesNotExist:
            return 1


@factory.django.mute_signals(post_save)
class NoteFactory(DjangoModelFactory):

    class Meta:
        model = Note
        # django_get_or_create = ('author',
        #                         'text',
        #                         'created_date',
        #                         'note_type',
        #                         )

    # author = factory.SubFactory(ProfileFactory)
    text = factory.Faker('paragraph')
    created_date = factory.Faker('date_time_this_month', tzinfo=tzinfo)
    note_type = 'Court'
    client = factory.SubFactory('intake.models.factories.ClientFactory')


@factory.django.mute_signals(post_save)
class PhaseFactory(DjangoModelFactory):

    class Meta:
        model = Phase
        # django_get_or_create = ('phase_id',
        #                         'screens_per_week',
        #                         'meetings_per_week',
        #                         'fees',
        #                         'notes',
        #                         'review_frequency')

    phase_id = factory.Iterator(Phase.CHOICES)
    screens_per_week = factory.Faker('random_element', elements=[
        x for x in range(1, 20)])
    meetings_per_week = factory.Faker('random_element', elements=[
        x for x in range(1, 20)])
    fees = '$25.00'
    # notes = factory.SubFactory('intake.models.factories.NoteFactory')
    review_frequency = factory.Faker('random_element', elements=[
        x for x in range(1, 20)])

    @classmethod
    def _setup_next_sequence(cls):
        try:
            return Phase.objects.latest('pk').pk + 1
        except Phase.DoesNotExist:
            return 1


@factory.django.mute_signals(post_save)
class ClientFactory(DjangoModelFactory):

    class Meta:
        model = Client
        # django_get_or_create = ('client_id', 'birth_date',
        #                         'created_date', 'gender', 'first_name', 'middle_initial', 'last_name', 'phase'
        #                         )

    client_num = factory.Sequence(lambda n: f'{int(2019000) + n}')
    status = IntakeStatus.STATUS_PENDING
    birth_date = factory.Faker('date_of_birth')
    created_date = timezone.now()
    gender = factory.Faker('random_element', elements=[
                           x[0] for x in GenderOption.CHOICES])
    first_name = factory.Faker('first_name')
    middle_initial = factory.Faker(
        'random_element', elements=list(string.ascii_uppercase))
    last_name = factory.Faker('last_name')
    # phase = factory.RelatedFactory('intake.models.factories.PhaseFactory')

    @classmethod
    def _setup_next_sequence(cls):
        try:
            return Client.objects.latest('pk').pk + 1
        except Client.DoesNotExist:
            return 1


@factory.django.mute_signals(post_save)
class ReferralFactory(DjangoModelFactory):

    class Meta:
        model = Referral

    status = factory.Faker('random_element', elements=[
                           x[0] for x in Referral.STATUS_CHOICES])
    client = factory.SubFactory('intake.models.factories.ClientFactory')
    referrer = factory.Faker('name')
    # TODO: Make SubFactory
    date_received = factory.Faker('date_this_decade', before_today=True, after_today=False)
    date_completed = factory.Faker('date_this_decade', before_today=False, after_today=True)
    # provider = factory.SubFactory('intake.models.factories.Provider')

# with factory.debug():
#     obj = ClientFactory()

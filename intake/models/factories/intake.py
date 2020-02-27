import logging
import string
from datetime import date
from random import randrange

import factory
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.utils import timezone
from factory import DjangoModelFactory

from court.models import CourtDates, Phase
from intake.models import Client, Referral
from intake.models.intake import IntakeStatus
# from profiles.models import Profile
from scribe.models import Note
from treatment.models import Objectives

from ..intake import GenderOption

User = get_user_model()
tzinfo = timezone.get_current_timezone()


@factory.django.mute_signals(post_save)
class ReferralFactory(DjangoModelFactory):

    class Meta:
        model = Referral

    status = factory.Faker('random_element', elements=[
                           x[0] for x in Referral.STATUS_CHOICES])
    client = factory.SubFactory('intake.models.factories.ClientFactory')
    referrer = factory.Faker('name')
    # TODO: Make SubFactory
    date_received = factory.Faker(
        'date_this_decade', before_today=True, after_today=False)
    date_completed = factory.Faker(
        'date_this_decade', before_today=False, after_today=True)
    # provider = factory.SubFactory('intake.models.factories.Provider')

    # make_objectives = factory.PostGeneration(
    #         lambda obj, create=True,)


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

    client_id = factory.Sequence(lambda n: f'{n}')
    status = IntakeStatus.STATUS_PENDING
    birth_date = factory.Faker('date_of_birth')
    created_date = timezone.now()
    gender = factory.Faker('random_element', elements=[
                           x[0] for x in GenderOption.CHOICES])
    first_name = factory.Faker('first_name')
    middle_initial = factory.Faker(
        'random_element', elements=list(string.ascii_uppercase))
    last_name = factory.Faker('last_name')

    referral = factory.RelatedFactory(
        'intake.models.factories.ReferralFactory', 'client')
    objectives = factory.RelatedFactory(
        'intake.models.factories.ObjectivesFactory', 'client')
    # phase = factory.RelatedFactory('intake.models.factories.PhaseFactory')

    @classmethod
    def _setup_next_sequence(cls):
        try:
            return Client.objects.latest('pk').pk + 1
        except Client.DoesNotExist:
            return 1

    @factory.helpers.post_generation
    def court_dates(self, create, extracted, **kwargs):
        import pdb; pdb.set_trace()
        if not create:
            return

        if extracted:
            assert isinstance(extracted, int)
            CourtDatesFactory.create_batch(
                size=extracted, client=self, **kwargs)
        else:
            import random
            number_of_units = random.randint(1, 5)
            for n in range(number_of_units):
                CourtDatesFactory(client=self)


@factory.django.mute_signals(post_save)
class ObjectivesFactory(DjangoModelFactory):
    class Meta:
        model = Objectives
    client = factory.SubFactory('intake.models.factories.ClientFactory')
    description = factory.Faker('sentences', nb=3, ext_word_list=None)
    obj_num = factory.Faker('random_element', elements=[
        x for x in range(1, 10)])
    obj_target = factory.Faker(
        'date_this_decade', before_today=False, after_today=True)
    closed = factory.Faker('boolean', chance_of_getting_true=50)
    met = factory.Faker('boolean', chance_of_getting_true=50)
    met_date = factory.Faker(
        'date_this_decade', before_today=False, after_today=True)
    tx_rating = factory.Faker('random_element', elements=[
        x for x in range(1, 10)])
    client_rating = factory.Faker('random_element', elements=[
        x for x in range(1, 10)])


@factory.django.mute_signals(post_save)
class CourtDatesFactory(DjangoModelFactory):
    class Meta:
        model = CourtDates
    client = factory.SubFactory('intake.models.factories.ClientFactory')
    court_date = factory.Faker(
        'date_this_decade', before_today=False, after_today=True)
    event = factory.Faker('random_element', elements=[
        x[0] for x in CourtDates.EVENT_CHOICES])
    court_date_type = factory.Faker('random_element', elements=[
        x[0] for x in CourtDates.TYPE_CHOICES])
    phase = factory.Faker('random_element', elements=[
        str(x) for x in range(1, 10)])
    attendance = factory.Faker('boolean', chance_of_getting_true=50)
    notes = factory.Faker('sentences', nb=1, ext_word_list=None)

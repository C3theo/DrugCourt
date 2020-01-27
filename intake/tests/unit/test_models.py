import os
import pdb
from datetime import date
from unittest.mock import MagicMock, patch

import pytest
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.test import TestCase, TransactionTestCase
from django.utils import timezone
from django_fsm import TransitionNotAllowed
from dotenv import load_dotenv
from faker import Faker

from intake.models import Client, Decision, Referral, factories
from scribe.models import Note

User = get_user_model()
tzinfo = timezone.get_current_timezone()
load_dotenv()


class ClientModelTest(TestCase):

    def test_client_id_created_automatically(self):

        client = Client(first_name='Jane',
                        middle_initial='D',
                        last_name='Doe',
                        birth_date='1970-07-07',
                        )

        client.save()

        self.assertIsNotNone(client.client_num)
        self.assertIsNot(client.client_num, '')
        self.assertEqual(client.client_num, '20190001')

    def test_client_id_unique(self):

        client_1 = Client(first_name='Jane',
                          middle_initial='D',
                          last_name='Doe',
                          birth_date='1970-07-07',
                          )

        client_2 = Client(first_name='Jane',
                          middle_initial='D',
                          last_name='Doe',
                          birth_date='1970-07-07',
                          )

        client_1.save()
        client_2.save()

        self.assertNotEqual(client_1.client_num, client_2.client_num)


@pytest.mark.skip()
class NoteModelTest(TestCase):

    def setUp(self):
        self.client = factories.ClientFactory.create()
        self.note = Note(text='...', client=self.client)
        # self.note.save()

    def test_note_requires_client(self):
        n = Note(text='...')
        self.assertRaises(IntegrityError, n.save)

    def test_note_linked_to_client(self):

        self.assertEqual(self.note.client.client_num, self.client.client_num)

    def test_note_time_stamped(self):

        self.assertIsNotNone(self.note.created_date)


class ReferralModelTest(TestCase):

    def setUp(self):
        self.client = factories.ClientFactory.create()
        self.referral = Referral(client=self.client)
        self.referral.save()

    @pytest.mark.skip(reason='Need to check on Referral Model required fields.')
    def test_referral_requires_client(self):
        r = Referral()
        self.assertRaises(IntegrityError, r.save)

    def test_referral_status_start(self):

        assert self.referral.status == Referral.STATUS_PENDING
    
    def test_decisions_created_condition(self):
        
        self.assertTrue(self.referral.decisions_created())
        self.referral.save()
        self.assertEqual(3, self.referral.decision_count)
        
    def test_approve_all_decisions(self):
        self.referral.approve_all_decisions()
        self.assertTrue(self.referral.all_decisions_approved())

    def test_referral_changes_with_decisions(self):
        self.referral.approve_all_decisions()
        self.referral.approve()
        
        self.assertEqual(self.referral.status, 'Approved')

    def test_referral_cant_approve_without_decisions(self):
        self.assertRaises(TransitionNotAllowed, self.referral.approve)

    def test_approved_referral_adds_client_to_phase_one(self):
        self.referral.approve_all_decisions()
        self.referral.approve()

        assert self.referral.client.phase != None
        assert self.referral.client.phase.phase_id == 'Phase One'


@pytest.mark.skip(reason='Decision model under construction')
class DecisionModelTest(TestCase):
    def setUp(self):
        client = factories.ClientFactory.create()
        self.referral = Referral(client=client)
        self.username = os.environ['TEST_USERNAME']
        self.password = os.environ['TEST_PASSWORD']
        self.email = 'test@drugcourt.com'
        user = User.objects.create(
            username=self.username, password=self.password, email=self.email)

        self.referral.save()
        user.save()

        self.decision = Decision(referral=self.referral,
                                 date_received='2019-06-08',
                                 date_completed='2019-06-09',)
        self.decision.save()

    def test_decision_requires_user_and_referral(self):
        d = Decision(date_received='2019-06-08',
                     date_completed='2019-06-09',)
        self.assertRaises(IntegrityError, d.save)

    @patch('intake.models.intake.models.query.QuerySet.values_list', autospec=True, return_value=[])
    def test_appprove_decision_condition(self, mock_query):
        condition = self.decision.one_decision_per_role()
        self.assertEqual(condition, True)


class PhaseModelTestCase(TestCase):

    def setUp(self):
        # self.client = factories.ClientFactory.create()
        self.referral = factories.ReferralFactory.create()
        # self.referral = Referral(client=self.client)
        # self.referral.save()


# @pytest.mark.skip()
# class ReferralsModelTest(TransactionTestCase):
#     @classmethod
#     def setUpClass(cls):
#         cls.referrals = factories.ReferralsFactory.create_batch(20)

#     def test_first_name_label(self):
#         referral = Referrals.objects.get(refid=1)
#         field_label = referral._meta.get_field('firstname').verbose_name
#         self.assertEqual(field_label, 'firstname')

#     def test_get_absolute_url(self):
#         # referral = Referrals.objects.get(refid=1)
#         referral = factories.ReferralsFactory()
#         self.assertEqual(referral.get_absolute_url(),
#                          f'/cases/referrals/{referral.refid}/')

#     def test_pending_to_active(self):
#         factories.ReferralsFactory(refid=1000, status='Pending',
#                          dadecision='Approved', defensedecision='Approved', teamdecision='Approved')
#         r = Referrals.objects.get(refid=1000)
#         r.approve_client()
#         self.assertEqual(r.status, 'Active')

#         r.defensedecision = 'Rejected'
#         r.status = 'Pending'
#         self.assertRaises(TransitionNotAllowed, r.approve_client)

# TODO: add other FSM states

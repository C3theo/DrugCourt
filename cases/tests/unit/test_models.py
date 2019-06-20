import pdb
from datetime import date

import pytest
from django.contrib.auth.models import User
from django.test import TestCase, TransactionTestCase

from cases.models import Clients, Referrals, factories
from django_fsm import TransitionNotAllowed


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

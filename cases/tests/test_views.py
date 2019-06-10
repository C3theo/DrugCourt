from cases.views import ReferralsCreate, ReferralsDetail
from django.test import Client, TestCase, SimpleTestCase, TransactionTestCase
from cases.models import Referrals
from .factories import ReferralsFactory
from unittest.mock import patch
import pytest
from .forms import ReferralsTabs


# unitttests

def setup_viewTest(view, request, *args, **kwargs):
    """
        Mimic as_view() returned callable, but returns view instance

        args and kwargs are as if you would pass to 'reverse()'
    """
    view.request = request
    view.args = args
    view.kwargs = kwargs
    return view

class ReferralsDetailTest(TestCase):

    def setUp(self):
        self.request = RequestFactory().get('/fake-path')
        self.view = ReferralsDetail
        self.view = setup_viewTest(self.view, self.request)

        self.client = Client()

# TODO: Test every action of methods

    # @patch(target='cases.forms.ReferralsDetail.post', autospec=True, ) # mock model imported from views.py
    def post_approve_button(self):
         # check if post with different name attributes are handled differently
        
        # this is going to throw a db access error
        form = ReferralsTabs()
        r = ReferralsFactory(refid=1000, status='Pending',
                         dadecision='Approved', defensedecision='Approved', teamdecision='Approved')
        
        # GET detail page response
        get_response = self.client.get(f'/referrals/{r.refid}')
        self.assertEqual(get_response.status, 200)

        post_response = self.client.post(f'/referrals/{r.refid}', {'id': 'submit-id-approve'})
        self.assertEqual(post_response.status, 200)
        # check decisions and status changed
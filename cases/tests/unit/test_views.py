import pdb
from unittest.mock import patch

import pytest
from django.contrib.auth.models import User
from django.test import TestCase, RequestFactory, SimpleTestCase
from django.urls import resolve
from django.http.request import QueryDict

from cases.forms import ReferralsTabs
from cases.models import Referrals
from cases.models.factories import ReferralsFactory
from cases.views import ReferralsCreate, ReferralsUpdate, IntakeView, intake
from mysite.urls import RedirectView

from django_webtest import WebTest


# TODO: utils.py
def setup_viewTest(view, request, *args, **kwargs):
    """
        Mimic as_view() returned callable, but returns view instance

        args and kwargs are as if you would pass to 'reverse()'
    """

    view.request = request
    view.args = args
    view.kwargs = kwargs
    return view


# pytestmark = pytest.mark.django_db

# @pytest.mark.django_db
class HomePageTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_root_url_redirects_to_cases_home(self):
        # Test not important
        pass
        # request = self.factory.get('')
        # self.assertEqual(response.status_code, 302)
        # self.assertRedirects(response, '/cases')


class IntakeViewTest(SimpleTestCase):

    def setUp(self):
        self.view = IntakeView()

    @patch('cases.views.intake.NoteForm', autospec=True, return_value='note_form')
    @patch('cases.views.intake.ReferralForm', autospec=True, return_value='referral_form')
    @patch('cases.views.intake.ClientForm', autospec=True, return_value='client_form')
    def test_get_all_forms_rendered(self, mock_client_form,
                                    mock_referral_form,
                                    mock_note_form):
        """
            Test that all forms are added to context data.
        """

        self.view.get_context_data()

        mock_client_form.assert_called_once()
        mock_referral_form.assert_called_once()
        mock_note_form.assert_called_once()

        # self.assertIsNotNone(self.view.extra_context)

    @patch('cases.views.intake.TemplateView.render_to_response', autospec=True)
    @patch('cases.views.intake._get_form', autospec=True)
    def test_post_valid_form_saved(self, mock_get, mock_response):
        """
            Test whether form instance is saved depending on form validation.
        """

        mock_get.return_value.is_bound = True
        mock_get.return_value.is_valid.return_value = True
        mock_get.return_value.save.return_value = True

        request = RequestFactory().post('/fake-path')
        view = setup_viewTest(self.view, request)
        view.post(request)

        self.assertEqual(mock_get.call_count, 3)
        mock_get.return_value.is_valid.assert_called_once()
        mock_get.return_value.save.assert_called_once()
        mock_response.assert_called_once()

        mock_get.return_value.is_bound = False
        mock_get.return_value.is_valid.return_value = False
        mock_get.return_value.save.reset_mock()

        view.post(request)

        mock_get.return_value.save.assert_not_called()

    @patch('cases.views.intake.ClientForm', autospec=True, return_value=True)
    def test_get_form(self, mock_form):
        """
            Test that form is bound if prefix in POST QueryDict.
        """

        request = RequestFactory().post('/fake-path', {'pre-text': ['Test']})
        prefix = 'pre'

        intake._get_form(request, mock_form, prefix)
        # pdb.set_trace()

        self.assertNotIn(None, mock_form.call_args)
        self.assertIsInstance(mock_form.call_args[0][0], QueryDict)



        # TODO: Have to pass self to render_to_response to get this to pass
        # kwargs = {'client_form': mock_get.return_value, 'note_form': mock_get.return_value,
        #                                 'referral_form': mock_get.return_value}
        # mock_response.assert_called_once_with(kwargs)

        # @pytest.mark.django_db
        # class ReferralsDetailTest(WebTest):

        #     def setUp(self):
        #         self.request = RequestFactory().get('/fake-path')
        #         self.view = ReferralsUpdate
        #         self.view = setup_viewTest(self.view, self.request)

        #         self.client = Client()
        #         self.user = User.objects.create_user('john', 'johnpassword')
        #         # self.client.force_login(self.user)
        #         self.app.set_user(self.user)

        # # TODO: Test every action of methods

        #     # @patch(target='cases.forms.ReferralsDetail.post', autospec=True, ) # mock model imported from views.py
        #     def test_post_approve_button(self):
        #          # check if post with different name attributes are handled differently

        #         # this is going to throw a db access error
        #         form = ReferralsTabs()
        #         r = ReferralsFactory(refid=1000, status='Pending',
        #                              dadecision='Approved', defensedecision='Approved', teamdecision='Approved')

        #         # GET detail page response
        #         # get_response = self.client.get(f'/referrals/{r.refid}')
        #         # self.assertEqual(get_response.status, 200)

        #         # post_response = self.client.post(f'/referrals/{r.refid}', {'id': 'submit-id-approve'})
        #         # self.assertEqual(post_response.status, 200)
        #         # check decisions and status changed

        #     def test_post_approve(self):
        #         r = ReferralsFactory(pretrialdecision='Approved')
        #         response = self.app.get(r.get_absolute_url(), user='john')

        #         self.assertNotEqual(response.status_code, 404)

        #         form = self.app.get(r.get_absolute_url(), user='john').form
        #         form['dadecision'] = 'Approved'
        #         submit_form = form.submit('approve')
        #         pdb.set_trace()

        #         self.assertRedirects(submit_form, r.get_absolute_url())

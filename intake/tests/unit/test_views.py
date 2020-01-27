from unittest.mock import MagicMock, patch

import pytest
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http.request import QueryDict
from django.test import RequestFactory, SimpleTestCase, TestCase
from django.urls import resolve
from django_webtest import WebTest

from intake.views import (ClientListView, ClientReferralCreateView,
                          ClientReferralUpdateView, ClientUpdateView,
                          CriminalBackgroundCreateView, DecisionCreateView,
                          IntakeFilterView, ReferralDecisionUpdateView, ClientReferralMultiForm)
from mysite.urls import RedirectView


def setup_viewTest(view, request, *args, **kwargs):
    """
        Mimic as_view() returned callable, but returns view instance

        args and kwargs are as if you would pass to 'reverse()'
    """

    view.request = request
    view.args = args
    view.kwargs = kwargs
    return view

# TODO:
# (ClientUpdateView, ClientListView, ClientNoteCreateView,
    # CourtDateUpdateView, CourtDateListView, CourtDateView,
    # CriminalBackgroundCreateView,  )


class IntakeFilterViewTest(SimpleTestCase):
    """
        Intake Module Step: 0
    """

    def setUp(self):
        self.view = IntakeFilterView()

    @patch('intake.views.views.TemplateView.render_to_response', auto_spec=True)
    # @patch('intake.views.views.ReferralFilter', auto_spec=True)
    def test_get(self, mock_render):
        """
            Test that GET request creates and renders ReferralFilter Object in context.
        """
        # referral_filter = ReferralFilter(
        #     request.GET)
        # return self.render_to_response({'filter': referral_filter})

        request = RequestFactory().get('/fake-path')
        view = setup_viewTest(self.view, request)
        response = view.get(request)

        # mock_filter.assert_called_once()
        mock_render.assert_called_once()
        # import pdb
        # pdb.set_trace()
        # self.assertDictContainsSubset({'filter': mock_filter}, response)


class ClientReferralCreateViewTest(SimpleTestCase):
    """
        Intake Module Step: 1a
    """

    def setUp(self):
        self.view = ClientReferralCreateView()

    @patch('django.views.generic.edit.FormMixin.get_form', autospec=True)
    @patch('intake.views.views.ClientReferralMultiForm', auto_spec=True)
    def test_get_multi_forms(self, mock_forms, mock_get_form):

        mock_get_form.return_value = mock_forms

        view = ClientReferralCreateView()
        request = RequestFactory().get('/fake-path')
        view = setup_viewTest(view, request)
        response = view.get(request)

        self.assertDictContainsSubset(
            {'form': mock_forms}, response.context_data)

    def test_post_multi_forms(self):
        """
            Test MultiForm save method called.
            Happens in 
        """
        self.fail()
        mock_forms.save.assert_called_once()

    def test_login_required_mixin(self):
        """
            Test is LoginRequiredMixin is in View.__mro__
        """
        self.assertIn(LoginRequiredMixin, self.view.__class__.__mro__)

    def test_post_success_url(self):
        """
            Test reverse_lazy called when valid form data posted.
        """
        self.fail()


class ClientReferralUpdateViewTest(SimpleTestCase):
    """
        Intake Module Step: 1b
    """

    def setUp(self):
        self.view = ClientReferralUpdateView()

    def test_login_required_mixin(self):
        """
            Test is LoginRequiredMixin is in View.__mro__
        """
        self.assertIn(LoginRequiredMixin, self.view.__class__.__mro__)


class ReferralDecisionUpdateViewTest(SimpleTestCase):
    """
        Intake Module Step: 2

    """

    def setUp(self):
        self.view = ReferralDecisionUpdateView()

    def test_login_required_mixin(self):
        """
            Test is LoginRequiredMixin is in View.__mro__
        """
        self.assertIn(LoginRequiredMixin, self.view.__class__.__mro__)

    @patch('intake.views.Referral', autospec=True)
    @patch('django.views.generic.detail.SingleObjectMixin.get_object', autospec=True)
    def test_get_form_kwargs(self, mock_get_object, mock_model):
        """
            Test that instances are in context
        """
        mock_get_object.return_value = mock_model
        mock_model.decisions.return_value = [
            'decision_0', 'decision_1', 'decision_2']

        request = RequestFactory().get('/fake-path')
        view = setup_viewTest(self.view, request)
        response = view.get(request)

        objects = response.context_data['form'].instances
        mock_objects = {
            'referral': mock_model,
            'pre_decision': mock_model.decisions[0],
            'da_decision': mock_model.decisions[1],
            'dc_decision': mock_model.decisions[2],
        }

        self.assertEqual(mock_objects, objects)

    # def test_referral_approve_called(self):


class ReferralCreateViewTest(SimpleTestCase):
    """
        CreateView
    """

    def setUp(self):
        self.view = ClientReferralCreateView()

    def test_login_required_mixin(self):
        """
            Test is LoginRequiredMixin is in View.__mro__
        """
        self.assertIn(LoginRequiredMixin, self.view.__class__.__mro__)

    @patch('django.views.generic.edit.FormMixin.get_form', autospec=True)
    @patch('intake.views.views.ReferralForm', autospec=True)
    def test_get(self, mock_form, mock_get_form):
        """
            BasUpdateView:
            def get(self, request, *args, **kwargs):
                self.object = self.get_object()
                return super().get(request, *args, **kwargs)

            ProcessFormView:
            def get(self, request, *args, **kwargs):
                "Handle GET requests: instantiate a blank version of the form."
                return self.render_to_response(self.get_context_data())
        """
        mock_get_form.return_value = mock_form

        request = RequestFactory().get('/fake-path')
        view = setup_viewTest(self.view, request)
        response = view.get(request)
        self.assertDictContainsSubset(
            {'form': mock_form}, response.context_data)

    @patch('intake.views.views.CreateView', autospec=True)
    @patch('intake.views.views.ReferralForm', autospec=True, return_value=True)
    def test_post_valid_form(self, mock_form, mock_view):
        """
        BaseCreateView:

        def post(self, request, *args, **kwargs):
            self.object = None
            return super().post(request, *args, **kwargs)

        ProcessFormView:

        def post(self, request, *args, **kwargs):
            form = self.get_form()
            if form.is_valid():
                return self.form_valid(form)
            else:
                return self.form_invalid(form)
        """

        mock_form.is_valid.return_value = True
        mock_view.get_form.return_value = mock_form
        mock_view.form_valid.return_value = True

        request = RequestFactory().get('/fake-path')
        view = setup_viewTest(self.view, request)
        response = view.post(request)

        self.assertTrue(response)


class ReferralUpdateViewTest(SimpleTestCase):
    """ UpdateView """

    def setUp(self):
        self.view = ClientReferralUpdateView()

    def test_login_required_mixin(self):
        """
            Test is LoginRequiredMixin is in View.__mro__
        """
        self.assertIn(LoginRequiredMixin, self.view.__class__.__mro__)

    @patch('intake.views.views.ClientReferralUpdateView.get_object', autospec=True)
    @patch('intake.views.views.Referral', autospec=True)
    def test_get(self, mock_object, mock_get_object):
        """
            BasUpdateView:
            def get(self, request, *args, **kwargs):
                self.object = self.get_object()
                return super().get(request, *args, **kwargs)

            ProcessFormView:
            def get(self, request, *args, **kwargs):
                "Handle GET requests: instantiate a blank version of the form."
                return self.render_to_response(self.get_context_data())
        """

        mock_get_object.return_value = mock_object
        request = RequestFactory().get('/fake-path')
        view = setup_viewTest(self.view, request)
        response = view.get(request)
        self.assertDictContainsSubset(
            {'object': mock_object}, response.context_data)

    @patch('intake.views.views.UpdateView', autospec=True)
    @patch('intake.views.views.ReferralForm', autospec=True, return_value=True)
    @patch('intake.views.views.Referral', autospec=True)
    @patch('intake.views.views.ClientReferralUpdateView.get_object', autospec=True)
    def test_post_valid_form(self, mock_get_object, mock_object, mock_form, mock_view):
        """
            BaseUpdateView:
            def post(self, request, *args, **kwargs):
                self.object = self.get_object()
                return super().post(request, *args, **kwargs)

            ProcessFormView:
            def post(self, request, *args, **kwargs):
                "Handle POST requests: instantiate a form instance with the passed
                POST variables and then check if it's valid."
                form = self.get_form()
                if form.is_valid():
                    return self.form_valid(form)
                else:
                    return self.form_invalid(form)

        """
        mock_get_object.return_value = mock_object
        mock_form.is_valid.return_value = True
        mock_view.get_form.return_value = mock_form
        mock_view.form_valid.return_value = True

        request = RequestFactory().get('/fake-path')
        view = setup_viewTest(self.view, request)
        response = view.post(request)

        self.assertTrue(response)


class ClientListViewTest(SimpleTestCase):
    """ SingleTableView """

    def setUp(self):
        self.view = ClientListView()

    def test_login_required_mixin(self):
        """
            Test is LoginRequiredMixin is in View.__mro__
        """
        self.assertIn(LoginRequiredMixin, self.view.__class__.__mro__)


class ClientUpdateViewTest(SimpleTestCase):
    """
        UpdateView
    """

    def setUp(self):
        self.view = ClientUpdateView()

    def test_login_required_mixin(self):
        """
            Test is LoginRequiredMixin is in View.__mro__
        """
        self.assertIn(LoginRequiredMixin, self.view.__class__.__mro__)

    @patch('intake.views.views.ClientUpdateView.get_object', autospec=True)
    @patch('intake.views.views.Client', autospec=True)
    def test_get(self, mock_client, mock_get_object):
        """
            BasUpdateView:
            def get(self, request, *args, **kwargs):
                self.object = self.get_object()
                return super().get(request, *args, **kwargs)

            ProcessFormView:
            def get(self, request, *args, **kwargs):
                "Handle GET requests: instantiate a blank version of the form."
                return self.render_to_response(self.get_context_data())
        """
        mock_get_object.return_value = mock_client
        request = RequestFactory().get('/fake-path')
        view = setup_viewTest(self.view, request)
        response = view.get(request)
        self.assertDictContainsSubset(
            {'object': mock_client}, response.context_data)

    @patch('intake.views.views.UpdateView', autospec=True)
    @patch('intake.views.views.ClientForm', autospec=True, return_value=True)
    @patch('intake.views.views.Referral', autospec=True)
    @patch('intake.views.views.ClientUpdateView.get_object', autospec=True)
    def test_post_valid_form(self, mock_get_object, mock_object, mock_form, mock_view):
        """
            BaseUpdateView:
            def post(self, request, *args, **kwargs):
                self.object = self.get_object()
                return super().post(request, *args, **kwargs)

            ProcessFormView:
            def post(self, request, *args, **kwargs):
                "Handle POST requests: instantiate a form instance with the passed
                POST variables and then check if it's valid."
                form = self.get_form()
                if form.is_valid():
                    return self.form_valid(form)
                else:
                    return self.form_invalid(form)

        """
        mock_get_object.return_value = mock_object
        mock_form.is_valid.return_value = True
        mock_view.get_form.return_value = mock_form
        mock_view.form_valid.return_value = True

        request = RequestFactory().get('/fake-path')
        view = setup_viewTest(self.view, request)
        response = view.post(request)

        self.assertTrue(response)


class DecisionCreateViewTest(SimpleTestCase):

    def setUp(self):
        self.view = DecisionCreateView()

    def test_login_required_mixin(self):
        """
            Test is LoginRequiredMixin is in View.__mro__
        """
        self.assertIn(LoginRequiredMixin, self.view.__class__.__mro__)

    @patch('django.views.generic.edit.FormMixin.get_form', autospec=True)
    @patch('intake.views.views.DecisionForm', autospec=True, return_value='legal_form')
    def test_get(self, mock_decision_form, mock_get_form):
        mock_get_form.return_value = mock_decision_form

        request = RequestFactory().get('/fake-path')
        view = setup_viewTest(self.view, request)
        response = view.get(request)
        self.assertDictContainsSubset(
            {'form': mock_decision_form}, response.context_data)

    @patch('intake.views.views.CreateView', autospec=True)
    @patch('intake.views.views.DecisionForm', autospec=True, return_value=True)
    def test_post_valid_form(self, mock_decision_form, mock_view):
        """
        BaseCreateView:

        def post(self, request, *args, **kwargs):
            self.object = None
            return super().post(request, *args, **kwargs)

        ProcessFormView:

        def post(self, request, *args, **kwargs):
            form = self.get_form()
            if form.is_valid():
                return self.form_valid(form)
            else:
                return self.form_invalid(form)
        """
        mock_decision_form.is_valid.return_value = True
        mock_view.get_form.return_value = mock_decision_form
        mock_view.form_valid.return_value = True

        request = RequestFactory().get('/fake-path')
        view = setup_viewTest(self.view, request)
        response = view.post(request)

        self.assertTrue(response)


class CriminalBackgroundCreateViewTest(SimpleTestCase):

    def setUp(self):
        self.view = CriminalBackgroundCreateView()

    def test_login_required_mixin(self):
        """
            Test is LoginRequiredMixin is in View.__mro__
        """
        self.assertIn(LoginRequiredMixin, self.view.__class__.__mro__)

    @patch('django.views.generic.edit.FormMixin.get_form', autospec=True)
    @patch('intake.forms.CriminalBackgroundForm', autospec=True, return_value='legal_form')
    def test_get(self, mock_legal_form, mock_get_form):
        mock_get_form.return_value = mock_legal_form

        request = RequestFactory().get('/fake-path')
        view = setup_viewTest(self.view, request)
        response = view.get(request)
        self.assertDictContainsSubset(
            {'form': mock_legal_form}, response.context_data)

    @patch('intake.views.views.CreateView', autospec=True)
    @patch('intake.views.views.CriminalBackgroundForm', autospec=True, return_value=True)
    def test_post_valid_form(self, mock_legal_form, mock_view):
        """
        BaseCreateView:

        def post(self, request, *args, **kwargs):
            self.object = None
            return super().post(request, *args, **kwargs)

        ProcessFormView:

        def post(self, request, *args, **kwargs):
            form = self.get_form()
            if form.is_valid():
                return self.form_valid(form)
            else:
                return self.form_invalid(form)
        """

        mock_legal_form.is_valid.return_value = True
        mock_view.get_form.return_value = mock_legal_form
        mock_view.form_valid.return_value = True

        request = RequestFactory().get('/fake-path')
        view = setup_viewTest(self.view, request)
        response = view.post(request)

        self.assertTrue(response)


@pytest.mark.skip(reason='Not currently using this view')
class IntakeFormViewTest(SimpleTestCase):

    def setUp(self):
        self.view = IntakeFormView()

    def test_login_required_mixin(self):
        """
            Test is LoginRequiredMixin is in View.__mro__
        """
        self.assertIn(LoginRequiredMixin, self.view.__class__.__mro__)

    @patch('intake.views.views.DecisionForm', autospec=True)
    @patch('intake.views.views.NoteForm', autospec=True)
    @patch('intake.views.views.ReferralForm', autospec=True)
    @patch('intake.views.views.ClientForm', autospec=True)
    def test_get_forms(self, mock_client_form,
                       mock_referral_form,
                       mock_note_form, mock_decision_form):
        """
            Tests that all forms are added to context dictionary
            when get_context_data called after view receives GET request.
        """
        request = RequestFactory().get('/fake-path')
        view = setup_viewTest(self.view, request)
        response = view.get(request)

        mock_client_form.assert_called_once()
        mock_referral_form.assert_called_once()
        mock_note_form.assert_called_once()
        mock_decision_form.assert_called_once()
        # self.assertDictContainsSubset({'client_form': mock_client_form}, response.context_data)

    @patch('intake.views.views.messages.success')
    @patch('intake.views.views.TemplateView.render_to_response', autospec=True)
    @patch('intake.views.views._get_form_submit', autospec=True)
    def test_post_valid_form_saved(self, mock_form, mock_response, mock_message):
        """
            Tests that valid bound forms are saved
        """

        mock_form.return_value.is_bound = True
        mock_form.return_value.is_valid.return_value = True
        mock_client = MagicMock()
        mock_client.client_num = 11111
        mock_form.return_value.save.return_value = mock_client

        request = RequestFactory().post('/fake-path')
        view = setup_viewTest(self.view, request)
        view.post(request)

        self.assertEqual(mock_form.call_count, 4)
        mock_form.return_value.is_valid.assert_called_once()
        mock_form.return_value.save.assert_called_once()
        mock_response.assert_called_once()

    @patch('intake.views.views.messages.success')
    @patch('intake.views.views.TemplateView.render_to_response', autospec=True)
    @patch('intake.views.views._get_form_submit', autospec=True)
    def test_post_invalid_form_not_saved(self, mock_form, mock_response, mock_message):
        """
            Test whether form instance is saved depending on form validation.

            _get_form is used after POST request received. Bound Form
        """

        mock_form.return_value.is_bound = False
        mock_form.return_value.is_valid.return_value = False
        mock_client = MagicMock()
        mock_client.client_num = 11111
        mock_form.return_value.save.return_value = mock_client
        request = RequestFactory().post('/fake-path')
        view = setup_viewTest(self.view, request)
        view.post(request)

        mock_form.return_value.save.assert_not_called()

    @patch('intake.views.views.ClientForm', autospec=True, return_value=True)
    def test_get_form_submit(self, mock_form):
        """
            Test that form is bound if prefix in POST QueryDict.
        """

        request = RequestFactory().post('/fake-path', {'pre-text': ['Test']})
        prefix = 'pre-text'

        _get_form_submit(request, mock_form, prefix)

        self.assertNotIn(None, mock_form.call_args)
        self.assertIsInstance(mock_form.call_args[0][0], QueryDict)

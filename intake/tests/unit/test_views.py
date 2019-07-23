from unittest.mock import MagicMock, patch

import pytest
from django.contrib.auth.models import User
from django.http.request import QueryDict
from django.test import RequestFactory, SimpleTestCase, TestCase
from django.urls import resolve
from django_webtest import WebTest

from intake.views import (ClientDetailView, CriminalBackgroundCreateView,
                          DecisionCreateView, IntakeFormView,
                          ReferralCreateView, ReferralDetailView)
from intake.views.intake import _get_form_submit
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
# NoteListView, ClientNoteCreateView,


class ReferralCreateViewTest(SimpleTestCase):
    """ CreateView """

    def setUp(self):
        self.view = ReferralCreateView()

    @patch('django.views.generic.edit.FormMixin.get_form', autospec=True)
    @patch('intake.views.intake.ReferralForm', autospec=True)
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

    @patch('intake.views.intake.CreateView', autospec=True)
    @patch('intake.views.intake.ReferralForm', autospec=True, return_value=True)
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


class ReferralDetailViewTest(SimpleTestCase):
    """ UpdateView """

    def setUp(self):
        self.view = ReferralDetailView()

    @patch('intake.views.intake.ReferralDetailView.get_object', autospec=True)
    @patch('intake.views.intake.Referral', autospec=True)
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

    @patch('intake.views.intake.UpdateView', autospec=True)
    @patch('intake.views.intake.ReferralForm', autospec=True, return_value=True)
    @patch('intake.views.intake.Referral', autospec=True)
    @patch('intake.views.intake.ReferralDetailView.get_object', autospec=True)
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


class ClientListView(SimpleTestCase):
    """ SingleTableView """


class ClientDetailViewTest(SimpleTestCase):
    """
        UpdateView
    """

    def setUp(self):
        self.view = ClientDetailView()

    @patch('intake.views.intake.ClientDetailView.get_object', autospec=True)
    @patch('intake.views.intake.Client', autospec=True)
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

    @patch('intake.views.intake.UpdateView', autospec=True)
    @patch('intake.views.intake.ClientForm', autospec=True, return_value=True)
    @patch('intake.views.intake.Referral', autospec=True)
    @patch('intake.views.intake.ClientDetailView.get_object', autospec=True)
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

    @patch('django.views.generic.edit.FormMixin.get_form', autospec=True)
    @patch('intake.views.intake.DecisionForm', autospec=True, return_value='legal_form')
    def test_get(self, mock_decision_form, mock_get_form):
        mock_get_form.return_value = mock_decision_form

        request = RequestFactory().get('/fake-path')
        view = setup_viewTest(self.view, request)
        response = view.get(request)
        self.assertDictContainsSubset(
            {'form': mock_decision_form}, response.context_data)

    @patch('intake.views.intake.CreateView', autospec=True)
    @patch('intake.views.intake.DecisionForm', autospec=True, return_value=True)
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

    @patch('django.views.generic.edit.FormMixin.get_form', autospec=True)
    @patch('intake.forms.CriminalBackgroundForm', autospec=True, return_value='legal_form')
    def test_get(self, mock_legal_form, mock_get_form):
        mock_get_form.return_value = mock_legal_form

        request = RequestFactory().get('/fake-path')
        view = setup_viewTest(self.view, request)
        response = view.get(request)
        self.assertDictContainsSubset(
            {'form': mock_legal_form}, response.context_data)

    @patch('intake.views.intake.CreateView', autospec=True)
    @patch('intake.views.intake.CriminalBackgroundForm', autospec=True, return_value=True)
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


class IntakeFormViewTest(SimpleTestCase):

    def setUp(self):
        self.view = IntakeFormView()

    @patch('intake.views.intake.DecisionForm', autospec=True)
    @patch('intake.views.intake.NoteForm', autospec=True)
    @patch('intake.views.intake.ReferralForm', autospec=True)
    @patch('intake.views.intake.ClientForm', autospec=True)
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

    @patch('intake.views.intake.messages.success')
    @patch('intake.views.intake.TemplateView.render_to_response', autospec=True)
    @patch('intake.views.intake._get_form_submit', autospec=True)
    def test_post_valid_form_saved(self, mock_form, mock_response, mock_message):
        """
            Tests that valid bound forms are saved
        """

        mock_form.return_value.is_bound = True
        mock_form.return_value.is_valid.return_value = True
        mock_client = MagicMock()
        mock_client.client_id = 11111
        mock_form.return_value.save.return_value = mock_client

        request = RequestFactory().post('/fake-path')
        view = setup_viewTest(self.view, request)
        view.post(request)

        self.assertEqual(mock_form.call_count, 4)
        mock_form.return_value.is_valid.assert_called_once()
        mock_form.return_value.save.assert_called_once()
        mock_response.assert_called_once()

    @patch('intake.views.intake.messages.success')
    @patch('intake.views.intake.TemplateView.render_to_response', autospec=True)
    @patch('intake.views.intake._get_form_submit', autospec=True)
    def test_post_invalid_form_not_saved(self, mock_form, mock_response, mock_message):
        """
            Test whether form instance is saved depending on form validation.

            _get_form is used after POST request received. Bound Form
        """

        mock_form.return_value.is_bound = False
        mock_form.return_value.is_valid.return_value = False
        mock_client = MagicMock()
        mock_client.client_id = 11111
        mock_form.return_value.save.return_value = mock_client
        request = RequestFactory().post('/fake-path')
        view = setup_viewTest(self.view, request)
        view.post(request)

        mock_form.return_value.save.assert_not_called()

    @patch('intake.views.intake.ClientForm', autospec=True, return_value=True)
    def test_get_form_submit(self, mock_form):
        """
            Test that form is bound if prefix in POST QueryDict.
        """

        request = RequestFactory().post('/fake-path', {'pre-text': ['Test']})
        prefix = 'pre-text'

        _get_form_submit(request, mock_form, prefix)

        self.assertNotIn(None, mock_form.call_args)
        self.assertIsInstance(mock_form.call_args[0][0], QueryDict)


class IntakeFormViewUpdateTest(SimpleTestCase):
    """
    """

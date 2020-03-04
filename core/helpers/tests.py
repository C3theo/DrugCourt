from unittest.mock import MagicMock, patch

import pytest
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http.request import QueryDict
from django.test import RequestFactory, SimpleTestCase, TestCase
from django.urls import resolve
from django_webtest import WebTest


def setup_viewTest(view, request, *args, **kwargs):
    """
        Mimic as_view() returned callable, but returns view instance

        args and kwargs are as if you would pass to 'reverse()'
    """

    view.request = request
    view.args = args
    view.kwargs = kwargs
    return view

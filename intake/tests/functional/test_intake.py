import logging
import os
import pdb
import sys
import time
import unittest
from functools import wraps
from importlib import import_module
from pathlib import Path

import pytest
from django.conf import settings
from django.contrib.auth import (BACKEND_SESSION_KEY, HASH_SESSION_KEY,
                                 SESSION_KEY, get_user_model)
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.db.utils import IntegrityError
from django.test import Client, override_settings
from dotenv import load_dotenv

import selenium.webdriver.chrome.service as service
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

from intake.models.factories import ClientFactory
from intake.models import Client
from .base import FunctionalTest


load_dotenv()

User = get_user_model()
logger = logging.getLogger(__name__)
folder_path = settings.BASE_DIR[:-7] + \
    '\\intake\\tests\\functional\\screenshots\\'

@override_settings(DEBUG=True)
class AddClientTest(FunctionalTest):

    def create_fake_user(self):
        self.username = os.environ['TEST_USERNAME']
        self.password = os.environ['TEST_PASSWORD']
        self.user = User.objects.create(
            username=self.username, password=self.password, email='roboto@gmail.com')

    def create_session_cookie(self):
        self.session = SessionStore()
        self.session[SESSION_KEY] = self.user.pk
        self.session[BACKEND_SESSION_KEY] = settings.AUTHENTICATION_BACKENDS[0]
        self.session[HASH_SESSION_KEY] = self.user.get_session_auth_hash()
        self.session.create()

    def add_cookie_to_browser(self):
        self.browser.get(self.live_server_url + '/404_no_such_url/')
        self.browser.add_cookie(dict(
            name=settings.SESSION_COOKIE_NAME,
            value=self.session.session_key,
            path='/',
        ))
        self.browser.refresh()

    def create_pre_authenticated_session(self):
        self.create_fake_user()
        self.create_session_cookie()
        self.add_cookie_to_browser()

    def send_keys_with_tabs(self, inputs=None, form=None):
        keys = list(zip(inputs, [Keys.TAB]*len(inputs)))
        keys = [j for i in keys for j in i]
        form.send_keys(keys)

    def screenshot_submit(self, path=None, button=None):

        self.browser.save_screenshot(path)
        button.click()

    def login_user(self):

        login_screenshot = folder_path + 'login.png'

        self.browser.get(self.live_server_url + '/login/')
        username_elem = self.browser.find_element_by_id('id_username')
        self.send_keys_with_tabs(
            [self.user.username, self.user.password], username_elem)

        login_button = self.wait_for(
            lambda: self.browser.find_element_by_id('login'))
        self.wait_for(lambda: self.screenshot_submit(
            path=login_screenshot, button=login_button))

    def test_intake_client_filter_detail(self):
        client = ClientFactory.create()
        self.create_pre_authenticated_session()
        self.browser.get(self.live_server_url)
        self.wait_to_be_logged_in()

        function_path = folder_path + sys._getframe().f_code.co_name

        home_screenshot = function_path + '_home.png'
        submit = self.wait_for(
            lambda: self.browser.find_element_by_id('id_intake_add'))
        self.wait_for(lambda: self.screenshot_submit(
            path=home_screenshot, button=submit))

        client_filter_screenshot = function_path + '_submit.png'
        field = self.wait_for(
            lambda: self.browser.find_element_by_id('id_client_id'))
        field.send_keys(client.client_id)
        submit = self.wait_for(
            lambda: self.browser.find_element_by_name('filter'))
        self.wait_for(lambda: self.screenshot_submit(
            path=client_filter_screenshot, button=submit))
        table_elem = self.wait_for(
            lambda: self.browser.find_element_by_id('client-id'))
        self.assertEqual(client.client_id, table_elem.text)
        self.wait_for(lambda: table_elem.click())

        client_detail_screenshot = function_path + '_detail.png'
        submit = self.wait_for(
            lambda: self.browser.find_element_by_id('client-update'))
        self.wait_for(lambda: self.screenshot_submit(
            path=client_detail_screenshot, button=submit))

    def test_drug_court_user_intake_client(self):

        self.create_pre_authenticated_session()
        self.browser.get(self.live_server_url + '/intake/new/')
        self.wait_to_be_logged_in()

        this_function_name = sys._getframe().f_code.co_name
        client_screenshot = folder_path + this_function_name + '_submit.png'

        client_form = self.wait_for(
            lambda: self.browser.find_element_by_id('id_client-first_name'))
        inputs = ['Jane', 'H', 'Doe', 'M', '07/07/1970']
        self.send_keys_with_tabs(inputs, client_form)
        submit = self.wait_for(
            lambda: self.browser.find_element_by_name('client'))
        self.wait_for(lambda: self.screenshot_submit(
            path=client_screenshot, button=submit))

    def test_intake_client_referral(self):
        client = ClientFactory.create()
        self.create_pre_authenticated_session()
        self.browser.get(self.live_server_url)
        # self.wait_to_be_logged_in()

        this_function_name = sys._getframe().f_code.co_name
        referral_screenshot = folder_path + this_function_name + '_submit.png'

        self.wait_for(lambda: self.browser.find_element_by_id(
            'referral-add').click())

        form = self.wait_for(
            lambda: self.browser.find_element_by_id('id_client'))

        select = Select(form)
        select.select_by_value('1')

        field = self.browser.find_element_by_name('referrer')
        inputs = ['John Snow', '06/08/2019', '06/08/2019']
        self.send_keys_with_tabs(inputs=inputs, form=field)
        submit = self.browser.find_element_by_id('referral-update')

        self.wait_for(lambda: self.screenshot_submit(
            button=submit, path=referral_screenshot))

        self.wait_for(lambda: self.browser.find_element_by_id('decision').click())
        import pdb; pdb.set_trace()


    def test_drug_court_user_intake_note(self):
        self.create_pre_authenticated_session()
        self.browser.get(self.live_server_url + '/intake/new/')
        self.wait_to_be_logged_in()

        this_function_name = sys._getframe().f_code.co_name
        note_screenshot = folder_path + this_function_name + '_submit.png'

        self.wait_for(
            lambda: self.browser.find_element_by_id('note-tab').click())
        note_form = self.wait_for(
            lambda: self.browser.find_element_by_id('id_note-text'))

        inputs = ['Test Note............']
        self.send_keys_with_tabs(inputs, note_form)
        note_submit = self.wait_for(
            lambda: self.browser.find_element_by_name('note'))
        self.wait_for(lambda: self.screenshot_submit(
            button=note_submit, path=note_screenshot))


# User logs in as Drug Court User

# User checks recent referrals

# User adds new client from referral

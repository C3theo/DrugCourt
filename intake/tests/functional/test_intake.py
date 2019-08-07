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
base = Path(settings.BASE_DIR).parent
folder_path = base / 'intake' / 'tests' / 'functional' / 'screenshots'


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

    def screenshot_submit(self, button=None, path=None):
        self.browser.save_screenshot(path)
        button.click()

    def screenshot_flow(self, function_name=None):
        """
            Save screenshots in folder with labels and sequence number.
        """

        try:
            function_path = folder_path / function_name
        except TypeError:
            function_path = folder_path

        prev_name = None
        count = None
        prev_url_namespace = '_'.join(self.browser.current_url.split('/')[3:])

        def take_screenshot(name='screenshot', window=self.browser):
            nonlocal prev_name
            nonlocal count
            nonlocal prev_url_namespace
            url_namespace = '_'.join(self.browser.current_url.split('/')[3:])
            if prev_name != name or prev_url_namespace != url_namespace:
                count = 0
            screenshot_path = function_path / \
                f'{url_namespace}_{name}_{count}.png'
            screenshot_path = screenshot_path.__str__()
            
            # Check if window is webdriver or element
            try:
                window.save_screenshot(screenshot_path)
            except AttributeError("'WebDriver' object has no attribute 'screenshot'"):
                window.screenshot(screenshot_path)
            count += 1
            prev_name = name
            prev_url_namespace = url_namespace

        # Clear out all screenshots for each test run
        try:
            os.mkdir(function_path)
            return take_screenshot
        except FileExistsError:
            [f.unlink() for f in Path(function_path).glob("*") if f.is_file()]
            return take_screenshot

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

    def test_intake_add_referral(self):
        function_name = sys._getframe().f_code.co_name
        take_screenshot = self.screenshot_flow(function_name)

        self.create_pre_authenticated_session()
        self.browser.get(self.live_server_url)

        # User logs in and redirects to Dashboard

        button = self.wait_for(
            lambda: self.browser.find_element_by_id('id_intake_add'))
        button.location_once_scrolled_into_view
        take_screenshot()
        # User goes to Intake Module
        button.click()

        button = self.wait_for(lambda: self.browser.find_element_by_id('add-referral'))
        # button.location_once_scrolled_into_view
        take_screenshot()
        # User adds new Referral
        button.click()

        inputs = ['Jane', 'H', 'Doe', 'M', '07/07/1970']
        client_form = self.wait_for(lambda: self.browser.find_element_by_id('id_client-first_name'))
        self.send_keys_with_tabs(inputs, client_form)

        ref_form = self.wait_for(lambda: self.browser.find_element_by_id('id_referral-referrer'))
        inputs = ['John Deer', '07/07/2019', '07/10/2019']
        self.send_keys_with_tabs(inputs, ref_form)

        # User fills in client and referral form
        ref_form.location_once_scrolled_into_view
        take_screenshot()

        # TODO: fix scrolling for screenshots
        # client_form.location_once_scrolled_into_view
        # take_screenshot()

        # User submits form
        button = self.wait_for(lambda: self.browser.find_element_by_id('referral-update'))
        button.click()

        button = self.wait_for(lambda: self.browser.find_element_by_link_text('Client: 20190001'))
        take_screenshot()

        # User clicks on newly created Referral
        button.click()

        button = self.wait_for(lambda: self.browser.find_element_by_id('decision'))

        # User clicks on 'Evaluate Referral' button
        button.click()
        take_screenshot()

        pre_trial = self.wait_for(lambda: self.browser.find_element_by_id('id_pre_decision-verdict'))
        select = Select(pre_trial)
        select.select_by_value('Approved')

        dc = self.wait_for(lambda: self.browser.find_element_by_id('id_dc_decision-verdict'))
        select = Select(dc)
        select.select_by_value('Approved')
        
        da = self.wait_for(lambda: self.browser.find_element_by_id('id_da_decision-verdict'))
        select = Select(da)
        select.select_by_value('Approved')

        button = self.wait_for(lambda: self.browser.find_element_by_id('decision-update'))
        button.location_once_scrolled_into_view
        take_screenshot()
        button.click()
        import pdb; pdb.set_trace()


    @pytest.mark.skip()
    def test_intake_client_referral_decision(self):
        function_name = sys._getframe().f_code.co_name
        take_screenshot = self.screenshot_flow(function_name)

        self.create_pre_authenticated_session()
        self.browser.get(self.live_server_url)

        # User logs in and redirects to Dashboard
        self.fail()
        # self.wait_for(
        #     lambda: self.browser.find_element_by_tag_name('table'))

    @pytest.mark.skip()
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

    @pytest.mark.skip()
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

    @pytest.mark.skip()
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

        self.wait_for(
            lambda: self.browser.find_element_by_id('decision').click())
        import pdb
        pdb.set_trace()

    @pytest.mark.skip()
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

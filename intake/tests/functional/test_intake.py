import os
import pdb
import time
import unittest

from pathlib import Path

from django.conf import settings
from django.contrib.auth import (BACKEND_SESSION_KEY, SESSION_KEY, HASH_SESSION_KEY,
                                 get_user_model)
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.db.utils import IntegrityError
from dotenv import load_dotenv

import selenium.webdriver.chrome.service as service
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys

from .base import FunctionalTest
from profiles.models import Profile

load_dotenv()

User = get_user_model()
screenshot_path = os.path.join(
    settings.BASE_DIR, 'intake\\tests\\functional\\screenshots\\')


class AddClientTest(FunctionalTest):

    def create_pre_authenticated_session(self, email):
        username = os.environ['TEST_USERNAME']
        password = os.environ['TEST_PASSWORD']
        user, created = User.objects.get_or_create(
            username=username, password=password, email=email)

        # check if session already exists
        session = SessionStore()
        session[SESSION_KEY] = user.pk
        session[BACKEND_SESSION_KEY] = settings.AUTHENTICATION_BACKENDS[0]
        session[HASH_SESSION_KEY] = user.get_session_auth_hash()
        session.save()

        self.browser.get(self.live_server_url + '/404_no_such_url/')
        self.browser.add_cookie(dict(
            name=settings.SESSION_COOKIE_NAME,
            value=session.session_key,
            path='/'
        ))
        self.browser.refresh()

    def setUp(self):
        super().setUp()
        self.username = os.environ['TEST_USERNAME']
        self.password = os.environ['TEST_PASSWORD']
        self.user, created = User.objects.get_or_create(
            username=self.username, password=self.password, email='roboto@email.com')
     
        if created:
            self.user.save()

        self.login_user()
        # self.create_pre_authenticated_session('roboto@email.com')
        # self.browser.get(self.live_server_url + '/intake/new/')
    
    def tearDown(self):
        super().tearDown()
        User.objects.all().delete()

    def send_keys_with_tabs(self, inputs, form):
        keys = list(zip(inputs, [Keys.TAB]*len(inputs)))
        keys = [j for i in keys for j in i]
        form.send_keys(keys)

    def screenshot_submit(self, path=None, button=None):

        self.browser.save_screenshot(path)
        button.click()

    def login_user(self):

        login_screenshot = screenshot_path + 'login.png'

        self.browser.get(self.live_server_url + '/login/')
        username_elem = self.browser.find_element_by_id('id_username')
        self.send_keys_with_tabs([self.user.username, self.user.password], username_elem)

        login_button = self.wait_for(
            lambda: self.browser.find_element_by_id('login'))
        import pdb
        pdb.set_trace()
        self.wait_for(lambda: self.screenshot_submit(
            path=login_screenshot, button=login_button))

    # def test_drug_court_user_login(self):
    #     # User is redirected to Login Page
    #     self.assertIn('Log In', self.browser.title)

    def test_drug_court_user_intake_client(self):
        client_screenshot = screenshot_path + 'client.png'
        self.browser.get(self.live_server_url + '/intake/new/')

        form_input = self.wait_for(
            lambda: self.browser.find_element_by_id('id_client-first_name'))
        # inputs = ['Jane', 'H', 'Doe', 'M', '07/07/1970']
        # keys = self.send_keys_with_tabs(inputs)
        # form_input.send_keys(keys)
        # self.wait_for(lambda: self.screenshot_submit(path=client_screenshot, button=form_input))

    def test_drug_court_user_intake_referral(self):
        referral_screenshot = screenshot_path + 'referral.png'

        self.wait_for(lambda: self.browser.find_element_by_id(
            'referral-tab').click())
        form_input = self.wait_for(
            lambda: self.browser.find_element_by_id('id_client-first_name'))

        # inputs = ['Jane', 'H', 'Doe', 'M', '07/07/1970']
        # keys = self.send_keys_with_tabs(inputs)
        # form_input.send_keys(keys)
        # self.wait_for(lambda: self.screenshot_submit(form_input, referral_screenshot))

    def test_drug_court_user_intake_note(self):
        note_screenshot = screenshot_path + 'referra.png'

        self.wait_for(
            lambda: self.browser.find_element_by_id('note-tab').click())
        # form_input = self.wait_for(
        #     lambda: self.browser.find_element_by_id('id_note-text'))

        # inputs = ['Test Note............']
        # keys = self.send_keys_with_tabs(inputs)
        # form_input.send_keys(keys)
        self.wait_for(lambda: self.screenshot_submit(
            form_input, note_screenshot))

        # self.browser.find_element_by_id('id_intake_add').click()
        # self.browser.find_element_by_id('notes-tab').click()

        # # TODO: fix this id
        # text_elem = self.browser.find_element_by_id('id_note-text')

        # msg = """Drug Court notes................"""

        # text_elem.send_keys(msg)


# User logs in as Drug Court User

# User checks recent referrals

# User adds new client from referral

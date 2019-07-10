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
from dotenv import load_dotenv

import selenium.webdriver.chrome.service as service
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys

from .base import FunctionalTest

load_dotenv()

User = get_user_model()


class AddClientTest(FunctionalTest):

    def create_pre_authenticated_session(self, email):
        username = os.environ['TEST_USERNAME']
        password = os.environ['TEST_PASSWORD']
        user = User.objects.create(username=username, password=password, email=email)
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


    def tearDown(self):
        self.browser.quit()

    # @wait
    # def test_drug_court_user_login(self):

    #     # User is redirected to Login Page
    #     self.assertIn('Log In', self.browser.title)

    #     # User types in username and password
    #     username_elem = self.browser.find_element_by_id('id_username')
    #     username_elem.send_keys(self.username, Keys.TAB)

    #     pw_elem = self.browser.find_element_by_id('id_password')
    #     pw_elem.send_keys(self.password, Keys.ENTER)

        # TODO: send success message

   
    def test_drug_court_user_intake_note(self):
        # import pdb
        # pdb.set_trace()

        self.create_pre_authenticated_session('roboto@email.com')
        time.sleep(3)

        self.browser.get(self.live_server_url + '/cases/intake')
        form_input = self.wait_for(lambda: self.browser.find_element_by_id('id_client-first_name'))
        inputs = ['Jane', 'H', 'Doe', 'M', '07/07/1970']
        keys = list(zip(inputs, [Keys.TAB]*len(inputs)))
        keys = [j for i in keys for j in i]
        form_input.send_keys(keys)
        time.sleep(3)
        form_input.send_keys(Keys.ENTER)
        # self.browser.get(self.live_server_url + '/cases/intake')
        time.sleep(3)
   

        # self.browser.find_element_by_id('id_intake_add').click()
        # self.browser.find_element_by_id('notes-tab').click()

        # # TODO: fix this id
        # text_elem = self.browser.find_element_by_id('id_note-text')

        # msg = """Drug Court notes................"""

        # text_elem.send_keys(msg)


# User logs in as Drug Court User

# User checks recent referrals

# User adds new client from referral

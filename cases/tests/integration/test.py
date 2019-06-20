import os
import pdb
import time
import unittest
from functools import wraps
from pathlib import Path

from django.conf import settings
from django.contrib.autho import (BACKEND_SESSION_KEY, SESSION_KEY,
                                  get_user_model)
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from dotenv import load_dotenv
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys

load_dotenv()

User = get_user_model()


MAX_WAIT = 10


def wait(f):

    @wraps(f)
    def wrapper(*args, **kwargs):

        start_time = time.time()
        while True:
            try:
                return f(*args, **kwargs)
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)


class NewVisitorTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.username = os.environ['TEST_USERNAME']
        self.password = os.environ['TEST_PASSWORD']

        # User goes to home page
        self.browser.get(self.live_server_url)

    def tearDown(self):
        self.browser.quit()

    def test_drug_court_user_login(self):
        
        pdb.set_trace()
        # User is redirected to Login Page
        self.assertIn('Log In', self.browser.title)

        # User types in username and password
        username_elem = self.browser.find_element_by_id('id_username')
        username_elem.send_keys(self.username, Keys.TAB)

        pw_elem = self.browser.find_element_by_id('id_password')
        pw_elem.send_keys(self.password, Keys.ENTER)

        # TODO: send success message

    def test_drug_court_user_intake_note(self):

        self.login_user()

        self.browser.find_element_by_id('id_intake_add').click()

        self.browser.find_element_by_id('notes-tab').click()

        # TODO: fix this id
        text_elem = self.browser.find_element_by_id('id_note-text')

        msg = """Drug Court notes................"""

        text_elem.send_keys(msg)


    def create_pre_auth_session(self, email):
        user = User.objects.create(email=email)
        session = SessionStore()
        session[SESSION_KEY] = user.pk
        session[BACKEND_SESSION_KEY] = settings.AUTHENTICATION_BACKENDS[0]
        session.save()

        self.browser.get(self.live_server_url + '/404_no_such_url/')
        self.browser.add_cookie(dict(
            name=settings.SESSION_COOKE_NAME,
            value=session.session_key,
            path='/'
        ))


    @wait
    def login_user(self):
        username_elem = self.browser.find_element_by_id('id_username')
        username_elem.send_keys(self.username, Keys.TAB)
        pw_elem = self.browser.find_element_by_id('id_password')
        return pw_elem.send_keys(self.password, Keys.ENTER)


# User logs in as Drug Court User

# User checks recent referrals

# User adds new client from referral

# if __name__ == 'main':
#     unittest.main(warnings='ignore')

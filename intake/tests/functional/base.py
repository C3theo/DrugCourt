import os
import sys
import time
from functools import wraps
from pathlib import Path

from django.conf import settings
from django.contrib.auth import (BACKEND_SESSION_KEY, HASH_SESSION_KEY,
                                 SESSION_KEY, get_user_model)
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.db.utils import IntegrityError
from django.test import Client, override_settings
from dotenv import load_dotenv

from intake.models import ClientFactory
from selenium import webdriver
from selenium.common.exceptions import (NoSuchElementException,
                                        WebDriverException)
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

User = get_user_model()
load_dotenv()
base = Path(settings.BASE_DIR).parent
# folder_path = base / 'intake' / 'tests' / 'functional' / 'screenshots'
MAX_WAIT = 8


def wait(f):

    @wraps(f)
    def wrapper(*args, **kwargs):

        start_time = time.time()
        while True:
            try:
                return f(*args, **kwargs)
            except (AssertionError, WebDriverException, NoSuchElementException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)
    return wrapper


class ScreenShotMixin:
    """
        Mixin to add ScreenShot functionality.
    """
    
    def screenshot_submit(self, button=None, path=None):
        self.browser.save_screenshot(path)
        button.click()

    def screenshot_flow(self, function_name=None):
        """
            Save screenshots in folder with labels and sequence number.
        """
        folder_path = base / '/'.join(self.__module__.split('.')[:-1])
        try:
            function_path = folder_path / 'screenshots' / function_name
        except TypeError:
            function_path = folder_path

        prev_name = None
        page_count = 0
        total_count = 0

        prev_url_namespace = '_'.join(self.browser.current_url.split('/')[3:])

        def take_screenshot(name='screenshot', window=self.browser):
            """
            """

            nonlocal prev_name
            nonlocal page_count
            nonlocal total_count
            nonlocal prev_url_namespace
            url_namespace = '_'.join(self.browser.current_url.split('/')[3:])
            if prev_name != name or prev_url_namespace != url_namespace:
                page_count = 0
            screenshot_path = function_path / \
                f'{total_count}_{url_namespace}_{name}_{page_count}.png'
            screenshot_path = screenshot_path.__str__()

            # Check if window is webdriver or element
            try:
                window.save_screenshot(screenshot_path)
            except AttributeError("'WebDriver' object has no attribute 'screenshot'"):
                window.screenshot(screenshot_path)
            page_count += 1
            total_count += 1
            prev_name = name
            prev_url_namespace = url_namespace
        
        # os.mkdir(function_path)
        # return take_screenshot
        # Clear out all screenshots for each test run
        try:
            os.mkdir(function_path)
            return take_screenshot
        except FileExistsError:
            [f.unlink() for f in Path(function_path).glob("*") if f.is_file()]
            return take_screenshot

class AuthMixin:
    """

    """

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

    
    def login_user(self):

        # login_screenshot = folder_path + 'login.png'

        self.browser.get(self.live_server_url + '/login/')
        username_elem = self.browser.find_element_by_id('id_username')
        self.send_keys_with_tabs(
            [self.user.username, self.user.password], username_elem)

        login_button = self.wait_for(
            lambda: self.browser.find_element_by_id('login'))



class FunctionalTest(StaticLiveServerTestCase, ScreenShotMixin, AuthMixin):
    """
        Class extends StaticLiveServerTestCase to implement set up and helper
        functions for Selenium Web Browser
    """

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        options = webdriver.ChromeOptions()
        options.add_experimental_option('w3c', False)
        cls.browser = webdriver.Chrome(options=options)

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.browser.quit()

    def setUp(self):
        super().setUp()
        self.add_clients()
        self.browser.maximize_window()
        self.create_pre_authenticated_session()
        self.browser.get(self.live_server_url)
      

    def tearDown(self):
        super().tearDown()

    def add_clients(self):
        ClientFactory.create_batch(25)

    @wait
    def wait_for(self, fn):
        return fn()

    @wait
    def wait_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def get_item_input_box(self):
        return self.browser.find_element_by_id('id_text')

    def add_list_item(self, item_text):
        num_rows = len(
            self.browser.find_elements_by_css_selector('#id_list_table tr'))
        self.get_item_input_box().send_keys(item_text)
        self.get_item_input_box().send_keys(Keys.ENTER)
        item_number = num_rows + 1
        self.wait_for_row_in_list_table(
            '{}: {}'.format(item_number, item_text)
        )

    @wait
    def wait_for_login_screen(self):

        username_elem = self.browser.find_element_by_id('id_username')
        pw_elem = self.browser.find_element_by_id('id_password')

        self.assertTrue(username_elem)
        self.assertTrue(pw_elem)

    @wait
    def wait_to_be_logged_in(self):
        log_out_link = self.browser.find_element_by_id('user-logout')
        self.assertIsNotNone(log_out_link)

    @wait
    def wait_to_be_logged_out(self):
        log_in_link = self.browser.find_element_by_id('user-login')
        self.assertIsNotNone(log_in_link)

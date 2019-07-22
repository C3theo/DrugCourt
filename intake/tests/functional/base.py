from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
import sys
import time
from functools import wraps

MAX_WAIT = 5

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
    return wrapper

class FunctionalTest(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        for arg in sys.argv:
            if 'liveserver' in arg:
                cls.server_host = arg.split('=')[1]
                cls.server_url = 'http://' + cls.server_host
                cls.against_staging = True
                return
        super().setUpClass()
     
        cls.server_url = cls.live_server_url

    def setUp(self):
  
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()


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
        num_rows = len(self.browser.find_elements_by_css_selector('#id_list_table tr'))
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
        self.browser.find_element_by_name('username')
        navbar = self.browser.find_element_by_css_selector('.navbar')
        self.assertIn('Log Out', navbar.text)


    @wait
    def wait_to_be_logged_out(self, email):
        self.browser.find_element_by_name('email')
        navbar = self.browser.find_element_by_css_selector('.navbar')
        self.assertNotIn(email, navbar.text)
import logging
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

import selenium.webdriver.chrome.service as service
from intake.models import Client
from intake.models.factories import ClientFactory, ReferralFactory
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.expected_conditions import \
    element_to_be_clickable
from selenium.webdriver.support.ui import Select, WebDriverWait

from .base import FunctionalTest

User = get_user_model()
logger = logging.getLogger(__name__)
base = Path(settings.BASE_DIR).parent
folder_path = base / 'intake' / 'tests' / 'functional' / 'screenshots'


@override_settings(DEBUG=True)
class ClientDashboard(FunctionalTest):
    """
    """

    def test_add_court_date(self):
        function_name = sys._getframe().f_code.co_name
        take_screenshot = self.screenshot_flow(function_name)
        client_link = self.wait_for(
            lambda: self.browser.find_element_by_xpath('//*[@id="model-table"]/tbody/tr[1]/td[1]/a'))
        href = client_link.get_attribute('href')
        if href.split('/')[-1] == 'dashboard':
            take_screenshot()
            client_link.click()

        # User taken to client Dashboard
        add_court_date_button = self.wait_for(
            lambda: self.browser.find_element_by_xpath('//*[@id="nav-home"]/p/button'))
        take_screenshot()
        add_court_date_button.click()

        # Modal form appears for User to fill in.
        modal = self.wait_for(
            lambda: self.browser.find_element_by_xpath(
                '//*[@id="modal-model"]/div[1]/div/form/div[1]'))
        take_screenshot()
        event_option = self.wait_for(
            lambda: self.browser.find_element_by_id('id_event')
        )
        select = Select(event_option)
        select.select_by_value('Entry')

        court_date_type_option = self.wait_for(
            lambda: self.browser.find_element_by_id('id_court_date_type')
        )
        select = Select(court_date_type_option)
        select.select_by_value('New')
        inputs = ['07/07/1970']
        date = self.wait_for(
            lambda: self.browser.find_element_by_id('id_court_date')
        )
        self.send_keys_with_tabs(inputs, date)
        submit = self.wait_for(
            lambda: self.browser.find_element_by_xpath(
                '//*[@id="modal-model"]/div[1]/div/form/div[3]/button[2]')
        )

        # User submits form
        take_screenshot()
        submit.click()
        import pdb; pdb.set_trace()



    @pytest.mark.skip()
    def test_intake_add_referral(self):
        """
            Test adding and approving a Client's Referral
        """

        function_name = sys._getframe().f_code.co_name
        take_screenshot = self.screenshot_flow(function_name)

        # self.create_pre_authenticated_session()
        # self.browser.get(self.live_server_url)

        # User logs in and redirects to Dashboard
        button = self.wait_for(
            lambda: self.browser.find_element_by_id('id_intake_add'))
        button.location_once_scrolled_into_view
        take_screenshot()
        # User goes to Intake Module
        button.click()

        button = self.wait_for(
            lambda: self.browser.find_element_by_id('add-referral'))
        # button.location_once_scrolled_into_view
        take_screenshot()
        # User adds new Referral
        button.click()

        inputs = ['Jane', 'H', 'Doe', 'M', '07/07/1970']
        client_form = self.wait_for(
            lambda: self.browser.find_element_by_id('id_client-first_name'))
        self.send_keys_with_tabs(inputs, client_form)

        ref_form = self.wait_for(
            lambda: self.browser.find_element_by_id('id_referral-referrer'))
        inputs = ['John Deer', '07/07/2019', '07/10/2019']
        self.send_keys_with_tabs(inputs, ref_form)

        # User fills in client and referral form
        ref_form.location_once_scrolled_into_view
        take_screenshot()

        # User submits form
        button = self.wait_for(
            lambda: self.browser.find_element_by_id('referral-update'))
        button.click()

        button = self.wait_for(
            lambda: self.browser.find_element_by_link_text('20190001'))
        take_screenshot()

        # User clicks on newly created Referral
        button.click()

        button = self.wait_for(
            lambda: self.browser.find_element_by_id('decision'))

        # User clicks on 'Evaluate Referral' button
        button.click()
        take_screenshot()

        # User Approves all Decsisions
        pre_trial = self.wait_for(
            lambda: self.browser.find_element_by_id('id_pre_decision-verdict'))
        select = Select(pre_trial)
        select.select_by_value('Approved')

        dc = self.wait_for(lambda: self.browser.find_element_by_id(
            'id_dc_decision-verdict'))
        select = Select(dc)
        select.select_by_value('Approved')

        da = self.wait_for(lambda: self.browser.find_element_by_id(
            'id_da_decision-verdict'))
        select = Select(da)
        select.select_by_value('Approved')

        button = self.wait_for(
            lambda: self.browser.find_element_by_id('decision-update'))
        button.location_once_scrolled_into_view
        take_screenshot()
        button.click()

        # User is redirected to Intake Landing page with created Client/Referral that is approved for program
        elem = self.browser.find_element_by_xpath(
            "/html/body/main[@class='container mx-auto']/div[@class='jumbotron']/div[@class='card']/div[@class='card-body rounded']/table[@class='table']/tbody/tr[1]/td[4]")
        assert elem.text == 'Approved'
        take_screenshot()
# //*[@id="model-table"]/tbody/tr[1]/td[1]/a
    @pytest.mark.skip()
    def test_drug_court_user_intake_note(self):
        """
            Test Client Note Creation
        """

        function_name = sys._getframe().f_code.co_name
        take_screenshot = self.screenshot_flow(function_name)

        # self.create_pre_authenticated_session()
        self.wait_to_be_logged_in()

        referral = ReferralFactory.create()

        # User goes to Referral
        self.browser.get(self.live_server_url + '/intake')

        # User Selects Client
        button = self.wait_for(lambda:
                               self.browser.find_element_by_xpath(
                                   "/html/body/main[@class='container mx-auto']/div[@class='jumbotron']/div[@class='card']/div[@class='card-body rounded']/table[@class='table']/tbody/tr[1]/td[1]/a[@class='btn btn-secondary']")
                               )
        button.click()

        # User clicks on "Add Note Button"
        button = self.wait_for(lambda:
                               self.browser.find_element_by_xpath(
                                   "/html/body/main[@class='container mx-auto']/div[@class='jumbotron']/div[@class='card']/div[@class='card-body rounded']/div[@class='btn-group pb-5']/button[@class='btn btn-primary']")
                               )
        take_screenshot()
        button.click()

        # Client Field is Auto-populated for Client
        # TODO: make read only

        # User Selects Note type from drop down
        drop_down = WebDriverWait(self.browser, 10).until(
            element_to_be_clickable((By.ID, 'id_note-note_type')))

        select = Select(drop_down)
        select.select_by_value('Court')

        # User types in notes for client
        field = self.wait_for(lambda:
                              self.browser.find_element_by_xpath(
                                  "/html/body[@class='modal-open']/main[@class='container mx-auto']/div[@class='jumbotron']/div[@class='card']/div[@class='card-body rounded']/div[@id='noteModal']/div[@class='modal-dialog']/div[@class='modal-content']/div[@class='modal-body']/form[@id='note-form']/div[@class='form-row'][2]/div[@class='form-group col-12']/div[@id='div_id_note-text']/div/textarea[@id='id_note-text']")
                              )
        inputs = ['Client is doing great in program.']
        self.send_keys_with_tabs(inputs, field)
        take_screenshot()
        # User clicks "Add Notes" button in modal form
        button = self.wait_for(lambda:
                               self.browser.find_element_by_xpath(
                                   "/html/body[@class='modal-open']/main[@class='container mx-auto']/div[@class='jumbotron']/div[@class='card']/div[@class='card-body rounded']/div[@id='noteModal']/div[@class='modal-dialog']/div[@class='modal-content']/div[@class='modal-footer']/input[@id='add-note']")
                               )
        button.click()

        # User clicks "View All Notes Button"
        button = self.wait_for(lambda:
                               self.browser.find_element_by_xpath(
                                   "/html/body/main[@class='container mx-auto']/div[@class='jumbotron']/div[@class='card']/div[@class='card-body rounded']/div[@class='btn-group pb-5']/a[@class='btn btn-secondary']")
                               )
        button.click()
        take_screenshot()

        # User is redirected to Notes page filtered by Client ID, from which note was created
        # assert url == 'http://127.0.0.1:8000/notes/'

        # User sees newly created note for client in Notes Module
        table_field = self.wait_for(lambda:
                                    self.browser.find_element_by_xpath(
                                        "/html/body/main[@class='container mx-auto']/div[@class='jumbotron']/div[@class='card']/div[@class='card-body rounded']/div[@class='table-container']/table[@class='table table-striped table-light']/tbody/tr[@class='even'][1]/td[4]")
                                    )

        assert table_field.text == referral.client.client_id

# -*- coding: utf-8 -*-

"""
    ytelapiv3

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

import jsonpickle
import dateutil.parser
from .controller_test_base import ControllerTestBase
from ..test_helper import TestHelper
from ytelapiv3.api_helper import APIHelper


class ConferenceControllerTests(ControllerTestBase):

    @classmethod
    def setUpClass(cls):
        super(ConferenceControllerTests, cls).setUpClass()
        cls.controller = cls.api_client.conference

    # Retrieve a list of conference objects.
    def test_test_list_conferences(self):
        # Parameters for the API call
        page = None
        pagesize = None
        friendly_name = None
        date_created = None

        # Perform the API call through the SDK function
        result = self.controller.create_list_conferences(page, pagesize, friendly_name, date_created)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)


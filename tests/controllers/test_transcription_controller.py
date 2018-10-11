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


class TranscriptionControllerTests(ControllerTestBase):

    @classmethod
    def setUpClass(cls):
        super(TranscriptionControllerTests, cls).setUpClass()
        cls.controller = cls.api_client.transcription

    # Retrieve a list of transcription objects for your Ytel account.
    def test_test_list_transcriptions(self):
        # Parameters for the API call
        page = None
        pagesize = None
        status = None
        date_transcribed = None

        # Perform the API call through the SDK function
        result = self.controller.create_list_transcriptions(page, pagesize, status, date_transcribed)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)

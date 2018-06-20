# -*- coding: utf-8 -*-

"""
    ytelapi.controllers.recording_controller

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

from .base_controller import BaseController
from ..api_helper import APIHelper
from ..configuration import Configuration
from ..http.auth.basic_auth import BasicAuth

class RecordingController(BaseController):

    """A Controller to access Endpoints in the ytelapi API."""


    def create_recording_deleterecording(self,
                                         recordingsid):
        """Does a POST request to /recording/deleterecording.json.

        Remove a recording from your Ytel account.

        Args:
            recordingsid (string): The unique identifier for a recording.

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/recording/deleterecording.json'
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'recordingsid': recordingsid
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def create_recording_viewrecording(self,
                                       recordingsid):
        """Does a POST request to /recording/viewrecording.json.

        Retrieve the recording of a call by its RecordingSid. This resource
        will return information regarding the call such as start time, end
        time, duration, and so forth.

        Args:
            recordingsid (string): The unique identifier for the recording.

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/recording/viewrecording.json'
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'recordingsid': recordingsid
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def create_recording_listrecording(self,
                                       options=dict()):
        """Does a POST request to /recording/listrecording.json.

        Retrieve a list of recording objects.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    page -- int -- The page count to retrieve from the total
                        results in the collection. Page indexing starts at 1.
                    pagesize -- int -- The count of objects to return per
                        page.
                    datecreated -- string -- Filter results by creation date
                    callsid -- string -- The unique identifier for a call.

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/recording/listrecording.json'
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'page': options.get('page', None),
            'pagesize': options.get('pagesize', None),
            'Datecreated': options.get('datecreated', None),
            'callsid': options.get('callsid', None)
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body
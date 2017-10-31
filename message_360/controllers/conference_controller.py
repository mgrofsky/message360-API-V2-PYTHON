# -*- coding: utf-8 -*-

"""
    message_360.controllers.conference_controller

    This file was automatically generated for message360 by APIMATIC v2.0 ( https://apimatic.io ).
"""

from .base_controller import BaseController
from ..api_helper import APIHelper
from ..configuration import Configuration
from ..http.auth.basic_auth import BasicAuth

class ConferenceController(BaseController):

    """A Controller to access Endpoints in the message_360 API."""


    def deaf_mute_participant(self,
                              options=dict()):
        """Does a POST request to /conferences/deafMuteParticipant.{ResponseType}.

        Deaf Mute Participant

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    conference_sid -- string -- ID of the active conference
                    participant_sid -- string -- ID of an active participant
                    response_type -- string -- Response Type either json or
                        xml
                    muted -- bool -- Mute a participant
                    deaf -- bool -- Make it so a participant cant hear

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(conference_sid=options.get("conference_sid"),
                                 participant_sid=options.get("participant_sid"),
                                 response_type=options.get("response_type"))

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/conferences/deafMuteParticipant.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'conferenceSid': options.get('conference_sid', None),
            'ParticipantSid': options.get('participant_sid', None),
            'Muted': options.get('muted', None),
            'Deaf': options.get('deaf', None)
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def view_participant(self,
                         options=dict()):
        """Does a POST request to /conferences/viewparticipant.{ResponseType}.

        View Participant

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    conference_sid -- string -- unique conference sid
                    participant_sid -- string -- TODO: type description here.
                        Example: 
                    response_type -- string -- Response type format xml or
                        json

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(conference_sid=options.get("conference_sid"),
                                 participant_sid=options.get("participant_sid"),
                                 response_type=options.get("response_type"))

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/conferences/viewparticipant.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'ConferenceSid': options.get('conference_sid', None),
            'ParticipantSid': options.get('participant_sid', None)
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def add_participant(self,
                        options=dict()):
        """Does a POST request to /conferences/addParticipant.{ResponseType}.

        Add Participant in conference 

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    conferencesid -- string -- Unique Conference Sid
                    participantnumber -- string -- Particiant Number
                    response_type -- string -- Response type format xml or
                        json
                    muted -- bool -- add muted
                    deaf -- bool -- add without volume

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(conferencesid=options.get("conferencesid"),
                                 participantnumber=options.get("participantnumber"),
                                 response_type=options.get("response_type"))

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/conferences/addParticipant.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'conferencesid': options.get('conferencesid', None),
            'participantnumber': options.get('participantnumber', None),
            'muted': options.get('muted', None),
            'deaf': options.get('deaf', None)
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def view_conference(self,
                        options=dict()):
        """Does a POST request to /conferences/viewconference.{ResponseType}.

        View Conference

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    conferencesid -- string -- The unique identifier of each
                        conference resource
                    response_type -- string -- Response type format xml or
                        json

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(conferencesid=options.get("conferencesid"),
                                 response_type=options.get("response_type"))

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/conferences/viewconference.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'conferencesid': options.get('conferencesid', None)
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def create_conference(self,
                          options=dict()):
        """Does a POST request to /conferences/createConference.{ResponseType}.

        Here you can experiment with initiating a conference call through
        message360 and view the request response generated when doing so.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    mfrom -- string -- This number to display on Caller ID as
                        calling
                    to -- string -- To number
                    url -- string -- URL requested once the call connects
                    method -- HttpActionEnum -- Specifies the HTTP method used
                        to request the required URL once call connects.
                    record_callback_url -- string -- Recording parameters will
                        be sent here upon completion.
                    response_type -- string -- Response type format xml or
                        json
                    status_call_back_url -- string -- URL that can be
                        requested to receive notification when call has ended.
                        A set of default parameters will be sent here once the
                        conference is finished.
                    status_call_back_method -- HttpActionEnum -- Specifies the
                        HTTP methodlinkclass used to request
                        StatusCallbackUrl.
                    fall_back_url -- string -- URL requested if the initial
                        Url parameter fails or encounters an error
                    fall_back_method -- HttpActionEnum -- Specifies the HTTP
                        method used to request the required FallbackUrl once
                        call connects.
                    record -- bool -- Specifies if the conference should be
                        recorded.
                    record_callback_method -- HttpActionEnum -- Specifies the
                        HTTP method used to request the required URL once
                        conference connects.
                    schdeule_time -- string -- Schedule conference in future.
                        Schedule time must be greater than current time
                    timeout -- int -- The number of seconds the call stays on
                        the line while waiting for an answer. The max time
                        limit is 999 and the default limit is 60 seconds but
                        lower times can be set.

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(mfrom=options.get("mfrom"),
                                 to=options.get("to"),
                                 url=options.get("url"),
                                 method=options.get("method"),
                                 record_callback_url=options.get("record_callback_url"),
                                 response_type=options.get("response_type"))

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/conferences/createConference.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_parameters = {
            'Url': options.get('url', None)
        }
        _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
            _query_parameters, Configuration.array_serialization)
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'From': options.get('mfrom', None),
            'To': options.get('to', None),
            'Method': options.get('method', None),
            'RecordCallbackUrl': options.get('record_callback_url', None),
            'StatusCallBackUrl': options.get('status_call_back_url', None),
            'StatusCallBackMethod': options.get('status_call_back_method', None),
            'FallBackUrl': options.get('fall_back_url', None),
            'FallBackMethod': options.get('fall_back_method', None),
            'Record': options.get('record', None),
            'RecordCallbackMethod': options.get('record_callback_method', None),
            'SchdeuleTime': options.get('schdeule_time', None),
            'Timeout': options.get('timeout', None)
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def hangup_participant(self,
                           options=dict()):
        """Does a POST request to /conferences/hangupparticipant.{ResponseType}.

        Remove a participant from a conference.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    conference_sid -- string -- The unique identifier for a
                        conference object.
                    participant_sid -- string -- The unique identifier for a
                        participant object.
                    response_type -- string -- Response type format xml or
                        json

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(conference_sid=options.get("conference_sid"),
                                 participant_sid=options.get("participant_sid"),
                                 response_type=options.get("response_type"))

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/conferences/hangupparticipant.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_parameters = {
            'ParticipantSid': options.get('participant_sid', None)
        }
        _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
            _query_parameters, Configuration.array_serialization)
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'ConferenceSid': options.get('conference_sid', None)
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def play_conference_audio(self,
                              options=dict()):
        """Does a POST request to /conferences/playaudio.{ResponseType}.

        Play an audio file during a conference.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    conference_sid -- string -- The unique identifier for a
                        conference object.
                    participant_sid -- string -- The unique identifier for a
                        participant object.
                    audio_url -- AudioFormatEnum -- The URL for the audio file
                        that is to be played during the conference. Multiple
                        audio files can be chained by using a semicolon.
                    response_type -- string -- Response type format xml or
                        json

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(conference_sid=options.get("conference_sid"),
                                 participant_sid=options.get("participant_sid"),
                                 audio_url=options.get("audio_url"),
                                 response_type=options.get("response_type"))

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/conferences/playaudio.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'ConferenceSid': options.get('conference_sid', None),
            'ParticipantSid': options.get('participant_sid', None),
            'AudioUrl': options.get('audio_url', None)
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def list_participant(self,
                         options=dict()):
        """Does a POST request to /conferences/listparticipant.{ResponseType}.

        List Participant

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    conference_sid -- string -- unique conference sid
                    response_type -- string -- Response format, xml or json
                    page -- int -- page number
                    pagesize -- int -- Amount of records to return per page
                    muted -- bool -- Participants that are muted
                    deaf -- bool -- Participants cant hear

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(conference_sid=options.get("conference_sid"),
                                 response_type=options.get("response_type"))

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/conferences/listparticipant.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'ConferenceSid': options.get('conference_sid', None),
            'Page': options.get('page', None),
            'Pagesize': options.get('pagesize', None),
            'Muted': options.get('muted', None),
            'Deaf': options.get('deaf', None)
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def list_conference(self,
                        options=dict()):
        """Does a POST request to /conferences/listconference.{ResponseType}.

        List Conference

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    response_type -- string -- Response type format xml or
                        json
                    page -- int -- Which page of the overall response will be
                        returned. Zero indexed
                    page_size -- int -- Number of individual resources listed
                        in the response per page
                    friendly_name -- string -- Only return conferences with
                        the specified FriendlyName
                    date_created -- string -- Conference created date

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(response_type=options.get("response_type"))

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/conferences/listconference.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'Page': options.get('page', None),
            'PageSize': options.get('page_size', None),
            'FriendlyName': options.get('friendly_name', None),
            'DateCreated': options.get('date_created', None)
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

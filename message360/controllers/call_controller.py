# -*- coding: utf-8 -*-

"""
    message360.controllers.call_controller

    This file was automatically generated for message360 by APIMATIC BETA v2.0 on 11/11/2016
"""

from .base_controller import *

class CallController(BaseController):

    """A Controller to access Endpoints in the message360 API."""

    def create_view_call(self,
                         options=dict()):
        """Does a POST request to /calls/viewcalls.{ResponseType}.

        View Call Response

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    callsid -- string -- Call Sid id for particular Call
                    response_type -- string -- Response format, xml or json

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(callsid = options.get("callsid"))

        # The base uri for api requests
        _query_builder = Configuration.base_uri
 
        # Prepare query string for API call
        _query_builder += '/calls/viewcalls.{ResponseType}'

        # Process optional template parameters
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })

        # Validate and preprocess url
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'callsid': options.get('callsid', None)
        }
        
        # Form encode parameters.
        _form_parameters = APIHelper.form_encode_parameters(_form_parameters)

        # Prepare the API call.
        _request = self.http_client.post(_query_url, parameters=_form_parameters)

        # Apply authentication.
        BasicAuth.apply(_request)

        # Execute the request.
        _context = self.execute_request(_request)        

        # Global error handling using HTTP status codes.
        self.validate_response(_context)    

        # Return appropriate type
        return _context.response.raw_body



    def create_make_call(self,
                         options=dict()):
        """Does a POST request to /calls/makecall.{ResponseType}.

        You can experiment with initiating a call through Message360 and view
        the request response generated when doing so and get the response in
        json

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    from_country_code -- string -- from country code
                    mfrom -- string -- This number to display on Caller ID as
                        calling
                    to_country_code -- string -- To cuntry code number
                    to -- string -- To number
                    url -- string -- URL requested once the call connects
                    method -- HttpAction -- Specifies the HTTP method used to
                        request the required URL once call connects.
                    status_call_back_url -- string -- specifies the HTTP
                        methodlinkclass used to request StatusCallbackUrl.
                    status_call_back_method -- HttpAction -- Specifies the
                        HTTP methodlinkclass used to request
                        StatusCallbackUrl.
                    fall_back_url -- string -- URL requested if the initial
                        Url parameter fails or encounters an error
                    fall_back_method -- HttpAction -- Specifies the HTTP
                        method used to request the required FallbackUrl once
                        call connects.
                    heart_beat_url -- string -- URL that can be requested
                        every 60 seconds during the call to notify of elapsed
                        tim
                    heart_beat_method -- bool -- Specifies the HTTP method
                        used to request HeartbeatUrl.
                    timeout -- int -- Time (in seconds) Message360 should wait
                        while the call is ringing before canceling the call
                    play_dtmf -- string -- DTMF Digits to play to the call
                        once it connects. 0-9, #, or *
                    hide_caller_id -- bool -- Specifies if the caller id will
                        be hidden
                    record -- bool -- Specifies if the call should be
                        recorded
                    record_call_back_url -- string -- Recording parameters
                        will be sent here upon completion
                    record_call_back_method -- HttpAction -- Method used to
                        request the RecordCallback URL.
                    transcribe -- bool -- Specifies if the call recording
                        should be transcribed
                    transcribe_call_back_url -- string -- Transcription
                        parameters will be sent here upon completion
                    if_machine -- IfMachine -- How Message360 should handle
                        the receiving numbers voicemail machine
                    response_type -- string -- Response format, xml or json

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(from_country_code = options.get("from_country_code"),
                            mfrom = options.get("mfrom"),
                            to_country_code = options.get("to_country_code"),
                            to = options.get("to"),
                            url = options.get("url"))

        # The base uri for api requests
        _query_builder = Configuration.base_uri
 
        # Prepare query string for API call
        _query_builder += '/calls/makecall.{ResponseType}'

        # Process optional template parameters
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })

        # Validate and preprocess url
        _query_url = APIHelper.clean_url(_query_builder)

        # Process optional query parameters
        _query_parameters = {
            'Method': options.get('method', None)
        }

        # Prepare form parameters
        _form_parameters = {
            'FromCountryCode': options.get('from_country_code', None),
            'From': options.get('mfrom', None),
            'ToCountryCode': options.get('to_country_code', None),
            'To': options.get('to', None),
            'Url': options.get('url', None),
            'StatusCallBackUrl': options.get('status_call_back_url', None),
            'StatusCallBackMethod': options.get('status_call_back_method', None),
            'FallBackUrl': options.get('fall_back_url', None),
            'FallBackMethod': options.get('fall_back_method', None),
            'HeartBeatUrl': options.get('heart_beat_url', None),
            'HeartBeatMethod': options.get('heart_beat_method', None),
            'Timeout': options.get('timeout', None),
            'PlayDtmf': options.get('play_dtmf', None),
            'HideCallerId': options.get('hide_caller_id', None),
            'Record': options.get('record', None),
            'RecordCallBackUrl': options.get('record_call_back_url', None),
            'RecordCallBackMethod': options.get('record_call_back_method', None),
            'Transcribe': options.get('transcribe', None),
            'TranscribeCallBackUrl': options.get('transcribe_call_back_url', None),
            'IfMachine': options.get('if_machine', None)
        }
        
        # Form encode parameters.
        _form_parameters = APIHelper.form_encode_parameters(_form_parameters)

        # Prepare the API call.
        _request = self.http_client.post(_query_url, query_parameters=_query_parameters, parameters=_form_parameters)

        # Apply authentication.
        BasicAuth.apply(_request)

        # Execute the request.
        _context = self.execute_request(_request)        

        # Global error handling using HTTP status codes.
        self.validate_response(_context)    

        # Return appropriate type
        return _context.response.raw_body



    def create_play_audio(self,
                          options=dict()):
        """Does a POST request to /calls/playaudios.{ResponseType}.

        Play Dtmf and send the Digit

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    length -- int -- Time limit in seconds for audio play
                        back
                    direction -- Direction -- The leg of the call audio will
                        be played to
                    loop -- bool -- Repeat audio playback indefinitely
                    mix -- bool -- If false, all other audio will be muted
                    call_sid -- string -- The unique identifier of each call
                        resource
                    audio_url -- string -- URL to sound that should be played.
                        You also can add more than one audio file using
                        semicolons e.g.
                        http://example.com/audio1.mp3;http://example.com/audio2
                        .wav
                    response_type -- string -- Response format, xml or json

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(length = options.get("length"),
                            direction = options.get("direction"),
                            loop = options.get("loop"),
                            mix = options.get("mix"))

        # The base uri for api requests
        _query_builder = Configuration.base_uri
 
        # Prepare query string for API call
        _query_builder += '/calls/playaudios.{ResponseType}'

        # Process optional template parameters
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })

        # Validate and preprocess url
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'Length': options.get('length', None),
            'Direction': options.get('direction', None),
            'Loop': options.get('loop', None),
            'Mix': options.get('mix', None),
            'CallSid': options.get('call_sid', None),
            'AudioUrl': options.get('audio_url', None)
        }
        
        # Form encode parameters.
        _form_parameters = APIHelper.form_encode_parameters(_form_parameters)

        # Prepare the API call.
        _request = self.http_client.post(_query_url, parameters=_form_parameters)

        # Apply authentication.
        BasicAuth.apply(_request)

        # Execute the request.
        _context = self.execute_request(_request)        

        # Global error handling using HTTP status codes.
        self.validate_response(_context)    

        # Return appropriate type
        return _context.response.raw_body



    def create_record_call(self,
                           options=dict()):
        """Does a POST request to /calls/recordcalls.{ResponseType}.

        Record a Call

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    call_sid -- string -- The unique identifier of each call
                        resource
                    record -- bool -- Set true to initiate recording or false
                        to terminate recording
                    direction -- Direction -- The leg of the call to record
                    time_limit -- int -- Time in seconds the recording
                        duration should not exceed
                    call_back_url -- string -- URL consulted after the
                        recording completes
                    fileformat -- AudioFormat -- Format of the recording file.
                        Can be .mp3 or .wav
                    response_type -- string -- Response format, xml or json

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(call_sid = options.get("call_sid"),
                            record = options.get("record"))

        # The base uri for api requests
        _query_builder = Configuration.base_uri
 
        # Prepare query string for API call
        _query_builder += '/calls/recordcalls.{ResponseType}'

        # Process optional template parameters
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })

        # Validate and preprocess url
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'CallSid': options.get('call_sid', None),
            'Record': options.get('record', None),
            'Direction': options.get('direction', None),
            'TimeLimit': options.get('time_limit', None),
            'CallBackUrl': options.get('call_back_url', None),
            'Fileformat': options.get('fileformat', None)
        }
        
        # Form encode parameters.
        _form_parameters = APIHelper.form_encode_parameters(_form_parameters)

        # Prepare the API call.
        _request = self.http_client.post(_query_url, parameters=_form_parameters)

        # Apply authentication.
        BasicAuth.apply(_request)

        # Execute the request.
        _context = self.execute_request(_request)        

        # Global error handling using HTTP status codes.
        self.validate_response(_context)    

        # Return appropriate type
        return _context.response.raw_body



    def create_voice_effect(self,
                            options=dict()):
        """Does a POST request to /calls/voiceeffect.{ResponseType}.

        Voice Effect

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    call_sid -- string -- TODO: type description here.
                        Example: 
                    audio_direction -- AudioDirection -- TODO: type
                        description here. Example: 
                    pitch_semi_tones -- float -- value between -14 and 14
                    pitch_octaves -- float -- value between -1 and 1
                    pitch -- float -- value greater than 0
                    rate -- float -- value greater than 0
                    tempo -- float -- value greater than 0
                    response_type -- string -- Response format, xml or json

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(call_sid = options.get("call_sid"))

        # The base uri for api requests
        _query_builder = Configuration.base_uri
 
        # Prepare query string for API call
        _query_builder += '/calls/voiceeffect.{ResponseType}'

        # Process optional template parameters
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })

        # Validate and preprocess url
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'CallSid': options.get('call_sid', None),
            'AudioDirection': options.get('audio_direction', None),
            'PitchSemiTones': options.get('pitch_semi_tones', None),
            'PitchOctaves': options.get('pitch_octaves', None),
            'Pitch': options.get('pitch', None),
            'Rate': options.get('rate', None),
            'Tempo': options.get('tempo', None)
        }
        
        # Form encode parameters.
        _form_parameters = APIHelper.form_encode_parameters(_form_parameters)

        # Prepare the API call.
        _request = self.http_client.post(_query_url, parameters=_form_parameters)

        # Apply authentication.
        BasicAuth.apply(_request)

        # Execute the request.
        _context = self.execute_request(_request)        

        # Global error handling using HTTP status codes.
        self.validate_response(_context)    

        # Return appropriate type
        return _context.response.raw_body



    def create_send_digit(self,
                          options=dict()):
        """Does a POST request to /calls/senddigits.{ResponseType}.

        Play Dtmf and send the Digit

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    call_sid -- string -- The unique identifier of each call
                        resource
                    play_dtmf -- string -- DTMF digits to play to the call.
                        0-9, #, *, W, or w
                    play_dtmf_direction -- Direction -- The leg of the call
                        DTMF digits should be sent to
                    response_type -- string -- Response format, xml or json

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(call_sid = options.get("call_sid"),
                            play_dtmf = options.get("play_dtmf"))

        # The base uri for api requests
        _query_builder = Configuration.base_uri
 
        # Prepare query string for API call
        _query_builder += '/calls/senddigits.{ResponseType}'

        # Process optional template parameters
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })

        # Validate and preprocess url
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'CallSid': options.get('call_sid', None),
            'PlayDtmf': options.get('play_dtmf', None),
            'PlayDtmfDirection': options.get('play_dtmf_direction', None)
        }
        
        # Form encode parameters.
        _form_parameters = APIHelper.form_encode_parameters(_form_parameters)

        # Prepare the API call.
        _request = self.http_client.post(_query_url, parameters=_form_parameters)

        # Apply authentication.
        BasicAuth.apply(_request)

        # Execute the request.
        _context = self.execute_request(_request)        

        # Global error handling using HTTP status codes.
        self.validate_response(_context)    

        # Return appropriate type
        return _context.response.raw_body



    def create_interrupted_call(self,
                                options=dict()):
        """Does a POST request to /calls/interruptcalls.{ResponseType}.

        Interrupt the Call by Call Sid

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    call_sid -- string -- Call SId
                    url -- string -- URL the in-progress call will be
                        redirected to
                    method -- HttpAction -- The method used to request the
                        above Url parameter
                    status -- InterruptedCallStatus -- Status to set the
                        in-progress call to
                    response_type -- string -- Response format, xml or json

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(call_sid = options.get("call_sid"))

        # The base uri for api requests
        _query_builder = Configuration.base_uri
 
        # Prepare query string for API call
        _query_builder += '/calls/interruptcalls.{ResponseType}'

        # Process optional template parameters
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })

        # Validate and preprocess url
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'CallSid': options.get('call_sid', None),
            'Url': options.get('url', None),
            'Method': options.get('method', None),
            'Status': options.get('status', None)
        }
        
        # Form encode parameters.
        _form_parameters = APIHelper.form_encode_parameters(_form_parameters)

        # Prepare the API call.
        _request = self.http_client.post(_query_url, parameters=_form_parameters)

        # Apply authentication.
        BasicAuth.apply(_request)

        # Execute the request.
        _context = self.execute_request(_request)        

        # Global error handling using HTTP status codes.
        self.validate_response(_context)    

        # Return appropriate type
        return _context.response.raw_body



    def create_list_calls(self,
                          options=dict()):
        """Does a POST request to /calls/listcalls.{ResponseType}.

        A list of calls associated with your Message360 account

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    page -- string -- Which page of the overall response will
                        be returned. Zero indexed
                    page_size -- string -- Number of individual resources
                        listed in the response per page
                    to -- string -- Only list calls to this number
                    mfrom -- string -- Only list calls from this number
                    date_created -- string -- Only list calls starting within
                        the specified date range
                    response_type -- string -- Response format, xml or json

        Returns:
            void: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # The base uri for api requests
        _query_builder = Configuration.base_uri
 
        # Prepare query string for API call
        _query_builder += '/calls/listcalls.{ResponseType}'

        # Process optional template parameters
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })

        # Validate and preprocess url
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'Page': options.get('page', None),
            'PageSize': options.get('page_size', None),
            'To': options.get('to', None),
            'From': options.get('mfrom', None),
            'DateCreated': options.get('date_created', None)
        }
        
        # Form encode parameters.
        _form_parameters = APIHelper.form_encode_parameters(_form_parameters)

        # Prepare the API call.
        _request = self.http_client.post(_query_url, parameters=_form_parameters)

        # Apply authentication.
        BasicAuth.apply(_request)

        # Execute the request.
        _context = self.execute_request(_request)        

        # Global error handling using HTTP status codes.
        self.validate_response(_context)    
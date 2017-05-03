# -*- coding: utf-8 -*-

"""
    message_360.models.data_17_model

    This file was automatically generated for message360 by APIMATIC v2.0 ( https://apimatic.io )
"""


class Data17Model(object):

    """Implementation of the 'data17' model.

    TODO: type model description here.

    Attributes:
        companyname (string): TODO: type description here.
        otpcode (int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "companyname" : "companyname",
        "otpcode" : "otpcode"
    }

    def __init__(self,
                 companyname=None,
                 otpcode=None):
        """Constructor for the Data17Model class"""

        # Initialize members of the class
        self.companyname = companyname
        self.otpcode = otpcode


    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        companyname = dictionary.get("companyname")
        otpcode = dictionary.get("otpcode")

        # Return an object of this model
        return cls(companyname,
                   otpcode)


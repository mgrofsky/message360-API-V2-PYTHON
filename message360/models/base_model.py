# -*- coding: utf-8 -*-

""" 
    message360.models.base_model

    This file was automatically generated for message360 by APIMATIC v2.0 ( https://apimatic.io ) on 12/08/2016
"""

class BaseModel(object):    

    """All classes of structures inherit this base class.
    
    We are using this inheritance relationship to seperate the common
    logic all structure classes use. We also use it to detect if a
    class is a structure class.
    
    """

    def to_dictionary(self):
        """Creates a dictionary representation of a structure class. The 
        keys are taken from the API description and may differ from language
        specific variable names of properties.
            
        Returns:
            dictionary: A dictionary form of the model with properties in 
            their API formats.
            
        """

        dictionary = dict()

        # Loop through all properties in this model
        for name in self.names:
            value = getattr(self, name)                
            if isinstance(value, list):
                # Loop through each item
                dictionary[self.names[name]] = list()
                for item in value:
                    dictionary[self.names[name]].append(item.to_dictionary() if isinstance(item, BaseModel) else item)
            elif isinstance(value, dict):
                # Loop through each item
                dictionary[self.names[name]] = dict()
                for key in value:
                    dictionary[self.names[name]][key] = value[key].to_dictionary() if isinstance(value[key], BaseModel) else value[key]
            else:
                dictionary[self.names[name]] = value.to_dictionary() if isinstance(value, BaseModel) else value

        # Return the result
        return dictionary


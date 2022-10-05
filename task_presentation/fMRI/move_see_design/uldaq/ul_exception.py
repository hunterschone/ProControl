"""
Created on Mar 7 2018

@author: MCC
"""
from ctypes import create_string_buffer, c_uint
from .ul_c_interface import lib
from .ul_enums import ULError


class ULException(Exception):
    """
    Exception for an error in the UL.

    Args:
        error_code (ULError): A ULError error code value.
    """
    def __init__(self, error_code):
        self.error_code = ULError(error_code)
        """The :class:`ULError` error code value."""
        self.error_message = ''
        """The error message"""
        if error_code > 100000:
            self.error_message = python_error_messages[error_code]
        else:
            error_message = create_string_buffer(1000)
            lib.ulGetErrMsg(c_uint(error_code), error_message)
            self.error_message = error_message.value.decode('utf-8')

    def __str__(self):
        return str(self.error_code) + ': ' + self.error_message


python_error_messages = {ULError.BAD_DESCRIPTOR: 'Invalid descriptor'}

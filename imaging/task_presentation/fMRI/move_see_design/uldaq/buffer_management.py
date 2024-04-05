"""
Created on Feb 12 2018

@author: MCC
"""
from ctypes import c_ulonglong, c_double, Array


def create_float_buffer(number_of_channels, samples_per_channel):
    # type: (int, int) -> Array[float]
    """
    Create a buffer for double precision floating point sample values.

    Args:
        number_of_channels (int): Number of channels in the scan.
        samples_per_channel (int): Number samples per channel to be stored in
            the buffer.

    Returns:
        Array[float]:

        An array of size number_of_channels * samples_per_channel
    """
    dbl_array = c_double * (number_of_channels * samples_per_channel)  # type: type
    return dbl_array()


def create_int_buffer(number_of_channels, samples_per_channel):
    # type: (int, int) -> Array[int]
    """
    Create a buffer for 64-bit unsigned integer sample values.

    Args:
        number_of_channels (int): Number of channels in the scan.
        samples_per_channel (int): Number samples per channel to be stored in
            the buffer.

    Returns:
        Array[int]:

        An array of size number_of_channels * samples_per_channel.
    """
    ull_array = c_ulonglong * (number_of_channels * samples_per_channel)  # type: type
    return ull_array()

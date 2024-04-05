"""
Created on Mar 29 2018

@author: MCC
"""
from ctypes import Structure, c_char, c_uint, c_int, c_longlong
from collections import namedtuple
from .utils import enum_mask_to_list
from .ul_enums import (MemAccessType, MemRegion, InterfaceType, DaqOutChanType,
                       DaqInChanType, Range, AiInputMode)

"""A named tuple used to pass parameters to the user defined event callback
function. Used with DaqDevice.enable_event()."""
EventCallbackArgs = namedtuple('EventCallbackArgs',
                               'event_type event_data user_data')


def c_char_array(size):
    return c_char * size


class DaqDeviceDescriptor(Structure):
    """A class containing properties that define a particular DAQ device."""
    _fields_ = [("_product_name", c_char_array(64)),
                ("_product_id", c_uint),
                ("_dev_interface", c_uint),
                ("_dev_string", c_char_array(64)),
                ("_unique_id", c_char_array(64)),
                ("_reserved", c_char_array(512)), ]

    @property
    def product_name(self):
        """The generic (unqualified) product name of the device referenced by
         the DaqDeviceDescriptor."""
        return self._product_name.decode('utf8')

    @product_name.setter
    def product_name(self, value):
        self._product_name = value.encode('utf8')

    @property
    def product_id(self):
        """The numeric string indicating the product type referenced by the
        DaqDeviceDescriptor."""
        return self._product_id

    @product_id.setter
    def product_id(self, value):
        self._product_id = value

    @property
    def dev_interface(self):
        """The :class:`InterfaceType` indicating the type of
        interface in use by the device referenced by the
        DaqDeviceDescriptor."""
        return InterfaceType(self._dev_interface)

    @dev_interface.setter
    def dev_interface(self, value):
        self._dev_interface = value

    @property
    def dev_string(self):
        """Similar to product_name, but may contain additional information."""
        return self._dev_string.decode('utf8')

    @dev_string.setter
    def dev_string(self, value):
        self._dev_string = value.encode('utf8')

    @property
    def unique_id(self):
        """A string that uniquely identifies a specific device, usually with
         a serial number or MAC address."""
        return self._unique_id.decode('utf8')

    @unique_id.setter
    def unique_id(self, value):
        self._unique_id = value.encode('utf8')

    def __str__(self):
        if self.dev_string is not None and self.dev_string != "":
            return self.dev_string
        else:
            return self.product_name


class MemDescriptor(Structure):
    """A class containing properties that define the location and access types
    for a specified region of physical memory on the device."""
    _fields_ = [("_region", c_uint),
                ("_address", c_uint),
                ("_size", c_uint),
                ("_access_types", c_uint),
                ("_reserved", c_char_array(64)), ]

    @property
    def region(self):
        """A :class:`MemRegion` value indicating the region of memory."""
        return MemRegion(self._region)

    @property
    def address(self):
        """A numeric value that specifies the address of the memory."""
        return self._address

    @property
    def size(self):
        """The size in bytes that specifies the size of the memory area at the
        specified address."""
        return self._size

    @property
    def access_types(self):
        """A list of :class:`MemAccessType` values indicating the access
        rights to the memory at the specified address"""
        return enum_mask_to_list(MemAccessType, self._access_types)


class AiQueueElement(Structure):
    """A class containing properties that define an analog input queue element."""
    _fields_ = [("_channel", c_uint),
                ("_input_mode", c_uint),
                ("_range", c_uint),
                ("_reserved", c_char_array(64)), ]

    @property
    def channel(self):
        """The analog input channel number for the queue element."""
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value

    @property
    def input_mode(self):
        """The :class:`AiInputMode` value to use for the specified channel for the queue element."""
        return AiInputMode(self._input_mode)

    @input_mode.setter
    def input_mode(self, value):
        self._input_mode = value

    @property
    def range(self):
        """The :class:`Range` value to use for the specified channel for the queue element."""
        return Range(self._range)

    @range.setter
    def range(self, value):
        self._range = value


class DaqInChanDescriptor(Structure):
    """A class containing properties that define a DAQ input channel."""
    _fields_ = [("_channel", c_uint),
                ("_type", c_int),
                ("_range", c_int),
                ("_reserved", c_char_array(64)), ]

    @property
    def channel(self):
        """The channel number."""
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value

    @property
    def type(self):
        """The :class:`DaqInChanType` for the specified channel."""
        return DaqInChanType(self._type)

    @type.setter
    def type(self, value):
        self._type = value

    @property
    def range(self):
        """The :class:`Range` to be used for the specified channel; ignored if
        not analog."""
        return Range(self._range)

    @range.setter
    def range(self, value):
        self._range = value


class DaqOutChanDescriptor(Structure):
    """A class containing properties that define a DAQ output channel."""
    _fields_ = [("_channel", c_uint),
                ("_type", c_int),
                ("_range", c_int),
                ("_reserved", c_char_array(64)), ]

    @property
    def channel(self):
        """The channel number."""
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value

    @property
    def type(self):
        """The :class:`DaqOutChanType` for the specified channel."""
        return DaqOutChanType(self._type)

    @type.setter
    def type(self, value):
        self._type = value

    @property
    def range(self):
        """The :class:`Range` to be used for the specified channel; ignored if
        not analog."""
        return Range(self._range)

    @range.setter
    def range(self, value):
        self._range = value


class TransferStatus(Structure):
    """A class containing properties that define the progress of a scan operation."""
    _fields_ = [("_current_scan_count", c_longlong),
                ("_current_total_count", c_longlong),
                ("_current_index", c_longlong),
                ("_reserved", c_char_array(64)), ]

    @property
    def current_scan_count(self):
        """The number of samples per channel transferred since the scan
        started."""
        return self._current_scan_count

    @property
    def current_total_count(self):
        """The total number of samples transferred since the scan
        started."""
        return self._current_total_count

    @property
    def current_index(self):
        """The index into the data buffer immediately following the last sample transferred."""
        return self._current_index

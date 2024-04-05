"""
Created on Feb 17 2018

@author: MCC
"""

from ctypes import create_string_buffer, c_uint, byref, c_longlong, c_bool
from .ul_exception import ULException
from .ul_c_interface import lib, UlInfoItem, DevConfigItem
from .ul_enums import DevVersionType


class DaqDeviceConfig:
    """
    An instance of the DaqDeviceConfig class is obtained by calling
    :func:`DaqDevice.get_config`.
    """

    def __init__(self, handle):
        self.__handle = handle

    def get_version(self, version_type):
        # type: (DevVersionType) -> str
        """
        Gets the version of the firmware specified on the device
        referenced by the :class:`DaqDevice` object, specified
        by :class:`DevVersionType`, and returns it as a string.

        Args:
            version_type (DevVersionType): The type of firmware.

        Returns:
            str: The version of the specified type of firmware.

        Raises:
            :class:`ULException`
        """
        string_len = c_uint(100)
        info_str = create_string_buffer(string_len.value)
        err = lib.ulDevGetConfigStr(self.__handle, UlInfoItem.VER_STR,
                                    version_type, info_str, byref(string_len))
        if err != 0:
            raise ULException(err)
        return info_str.value.decode('utf-8')

    def has_exp(self):
        # type: () -> bool
        """
        Determines whether the device referenced by the :class:`DaqDevice`
        object has an expansion board attached.

        Returns:
            bool: True if an expansion board is attached.
            False if no expansion board is attached.

        Raises:
            :class:`ULException`
        """
        has_exp = c_longlong()
        err = lib.ulDevGetConfig(self.__handle, DevConfigItem.HAS_EXP, 0,
                                 byref(has_exp))
        if err != 0:
            raise ULException(err)
        return c_bool(has_exp).value

    def set_connection_code(self, connection_code, mem_unlock_code):
        # type: (int, int) -> None
        """
        Configures the connection code for the Ethernet device referenced by the
        :class:`DaqDevice` object.  The connection code becomes active after
        cycling power to the device or calling :func:`DaqDevice.reset`.  This
        function only applies to Ethernet devices.

        Args:
            connection_code (int): The connection code.
            mem_unlock_code (int): The memory unlock code required to write to
                the EEPROM, which is where the connection code is stored. See
                hardware documentation for more details.

        Raises:
            :class:`ULException`
        """
        # Unlock the memory for writes
        err = lib.ulDevSetConfig(self.__handle, DevConfigItem.MEM_UNLOCK_CODE,
                                 0, mem_unlock_code)
        if err != 0:
            raise ULException(err)
        # Write the new connection code to memory
        err = lib.ulDevSetConfig(self.__handle, DevConfigItem.CONNECTION_CODE,
                                 0, connection_code)
        if err != 0:
            raise ULException(err)
        # Lock the memory
        err = lib.ulDevSetConfig(self.__handle, DevConfigItem.MEM_UNLOCK_CODE,
                                 0, 0)
        if err != 0:
            raise ULException(err)

    def get_connection_code(self):
        # type: () -> int
        """
        Gets the connection code for the device referenced by the
        :class:`DaqDevice` object.

        Returns:
            int: The connection code.

        Raises:
            :class:`ULException`
        """
        code = c_longlong()
        err = lib.ulDevGetConfig(self.__handle, DevConfigItem.CONNECTION_CODE,
                                 0, byref(code))

        if err != 0:
            raise ULException(err)
        return code.value

    def get_ip_address(self):
        # type: () -> str
        """
        Gets the IP address of the device referenced by the
        :class:`DaqDevice` object and returns it as a string.

        Returns:
            str: The IP address.

        Raises:
            :class:`ULException`
        """
        string_len = c_uint(100)
        ip_address_str = create_string_buffer(string_len.value)
        err = lib.ulDevGetConfigStr(self.__handle, UlInfoItem.IP_ADDR_STR,
                                    0, ip_address_str, byref(string_len))
        if err != 0:
            raise ULException(err)
        return ip_address_str.value.decode('utf-8')

    def get_network_interface_name(self):
        # type: () -> str
        """
        Gets the network interface name for the device referenced by the
        :class:`DaqDevice` object and returns it as a string.

        Returns:
            str: The network interface name.

        Raises:
            :class:`ULException`
        """
        string_len = c_uint(100)
        network_name_str = create_string_buffer(string_len.value)
        err = lib.ulDevGetConfigStr(self.__handle, UlInfoItem.NET_IFC_STR,
                                    0, network_name_str, byref(string_len))
        if err != 0:
            raise ULException(err)
        return network_name_str.value.decode('utf-8')

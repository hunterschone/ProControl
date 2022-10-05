"""
Created on Feb 17 2018

@author: MCC
"""

from ctypes import c_longlong, byref
from .ul_exception import ULException
from .ul_c_interface import lib, DioInfoItem, DioConfigItem
from .ul_enums import DigitalDirection, ULError, DigitalPortType


class DioConfig:
    """
    An instance of the DioConfig class is obtained by calling
    :func:`DioDevice.get_config`.
    """

    def __init__(self, handle):
        self.__handle = handle

    def get_port_direction(self, port_type):
        # type: (DigitalPortType) -> list[DigitalDirection]
        """
        Gets the configured direction for each bit in the specified port
        for the device referenced by the :class:`DioInfo` object object.

        Args:
            port_type (DigitalPortType): The digital port type whose
                direction is being determined.

        Returns:
            list[DigitalDirection]:

            A list of values that specify
            the direction of each bit in the specified port.

        Raises:
            :class:`ULException`
        """
        bit_direction_mask = c_longlong()
        num_bits = c_longlong()
        port_types_list = []
        number_of_ports = c_longlong()
        bit_mask = 1
        bit_direction_list = []

        err = lib.ulDIOGetInfo(self.__handle, DioInfoItem.NUM_PORTS, 0,
                               byref(number_of_ports))
        if err != 0:
            raise ULException(err)

        # get the supported port types
        type_of_port = c_longlong()
        for i in range(number_of_ports.value):
            err = lib.ulDIOGetInfo(self.__handle, DioInfoItem.PORT_TYPE, i,
                                   byref(type_of_port))
            if err != 0:
                raise ULException(err)

            port_types_list.append(type_of_port.value)

        # get the index for the port type
        if port_type in port_types_list:
            port_index = port_types_list.index(port_type)

            err = lib.ulDIOGetInfo(self.__handle, DioInfoItem.NUM_BITS,
                                   port_index, byref(num_bits))
            if err != 0:
                raise ULException(err)

            err = lib.ulDIOGetConfig(self.__handle,
                                     DioConfigItem.PORT_DIRECTION_MASK,
                                     port_index, byref(bit_direction_mask))
            if err != 0:
                raise ULException(err)

            for bit_num in range(num_bits.value):
                if (bit_direction_mask.value >> bit_num) & bit_mask:
                    bit_direction_list.append(DigitalDirection.OUTPUT)
                else:
                    bit_direction_list.append(DigitalDirection.INPUT)
        else:
            raise ULException(ULError.BAD_PORT_TYPE)

        return bit_direction_list

    def set_port_initial_output_val(self, port_type, initial_output_val):
        # type: (DigitalPortType, int) -> None
        """
        Sets the initial output value of the specified digital port type.  This
        allows for a known state when switching the port direction from input
        to output.

        Args:
            port_type (DigitalPortType): The digital port type whose initial
                value is being set.
            initial_output_val (int): The initial output value for the
                specified digital port type.

        Raises:
            :class:`ULException`
        """
        err = lib.ulAISetConfig(self.__handle,
                                DioConfigItem.PORT_INITIAL_OUTPUT_VAL,
                                port_type, initial_output_val)
        if err != 0:
            raise ULException(err)

    def get_port_iso_filter_mask(self, port_type):
        # type: (DigitalPortType) -> int
        """
        Gets the ISO filter mask for the specified port type.

        Args:
            port_type (DigitalPortType): The digital port type whose filter
                mask is being retrieved.

        Returns:
            int:

            The filter mask for the specified port type.
            A zero indicates the corresponding bit is disabled.

        Raises:
            :class:`ULException`
        """
        filter_mask = c_longlong()
        err = lib.ulDIOGetConfig(self.__handle,
                                 DioConfigItem.PORT_ISO_FILTER_MASK,
                                 port_type, byref(filter_mask))
        if err != 0:
            raise ULException(err)
        return filter_mask.value

    def set_port_iso_filter_mask(self, port_type, filter_mask):
        # type: (DigitalPortType, int) -> None
        """
        Sets the ISO filter mask for the specified port type.

        Args:
            port_type (DigitalPortType): The digital port type whose filter
                mask is being set.
            filter_mask (int): The filter mask for the specified port type.
                A zero indicates the corresponding bit is disabled.

        Raises:
            :class:`ULException`
        """
        err = lib.ulAISetConfig(self.__handle,
                                DioConfigItem.PORT_ISO_FILTER_MASK,
                                port_type, filter_mask)
        if err != 0:
            raise ULException(err)

    def get_port_logic(self, port_type):
        # type: (DigitalPortType) -> int
        """
        Gets the logic for the specified port type.

        Args:
            port_type (DigitalPortType): The digital port type whose logic is
                being retrieved.

        Returns:
            int:

            The logic for the specified port type.
            A zero indicates non-invert mode for the corresponding bit.
            A non-zero indicates inverted mode for the corresponding bit.

        Raises:
            :class:`ULException`
        """
        logic = c_longlong()
        err = lib.ulDIOGetConfig(self.__handle,
                                 DioConfigItem.PORT_LOGIC,
                                 port_type, byref(logic))
        if err != 0:
            raise ULException(err)
        return logic.value

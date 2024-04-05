"""
Created on Feb 17 2018

@author: MCC
"""
from ctypes import c_longlong, c_bool, c_double, byref
from .ul_enums import (DigitalPortType, DigitalPortIoType, ScanOption,
                       TriggerType, ULError, DigitalDirection)
from .ul_exception import ULException
from .ul_c_interface import lib, DioInfoItem, DioInfoItemDbl
from .utils import enum_mask_to_list


class DioPortInfo:
    """Digital input/output port information."""

    def __init__(self):
        self._port_type = DigitalPortType.AUXPORT
        self._port_io_type = DigitalPortIoType.IN
        self._number_of_bits = 0
        self._reserved = '\0' * 64

    @property
    def port_type(self):
        """The :class:`DigitalPortType` value."""
        return DigitalPortType(self._port_type)

    @port_type.setter
    def port_type(self, value):
        self._port_type = value

    @property
    def port_io_type(self):
        """The :class:`DigitalPortIoType` value."""
        return DigitalPortIoType(self._port_io_type)

    @port_io_type.setter
    def port_io_type(self, value):
        self._port_io_type = value

    @property
    def number_of_bits(self):
        """The number of bits in the port."""
        return self._number_of_bits

    @number_of_bits.setter
    def number_of_bits(self, value):
        self._number_of_bits = value


class DioInfo:
    """
    An instance of the DioInfo class is obtained by calling
    :func:`DioDevice.get_info`.
    """

    def __init__(self, handle):
        self.__handle = handle

    def get_num_ports(self):
        # type: () -> int
        """
        Gets the total number of digital I/O ports
        on the device referenced by the :class:`DioInfo` object.

        Returns:
            int:

            The number of digital I/O ports.

        Raises:
            :class:`ULException`
        """
        number_of_ports = c_longlong()

        err = lib.ulDIOGetInfo(self.__handle, DioInfoItem.NUM_PORTS, 0,
                               byref(number_of_ports))
        if err != 0:
            raise ULException(err)

        return number_of_ports.value

    def get_port_types(self):
        # type: () -> list[DigitalPortType]
        """
        Gets a list of supported port types on
        the device referenced by the :class:`DioInfo` object.

        Returns:
           list[DigitalPortType]:

           A list of supported digital port types.

        Raises:
            :class:`ULException`
        """
        port_type = c_longlong()
        port_types_list = []

        number_of_ports = self.get_num_ports()

        for i in range(number_of_ports):
            err = lib.ulDIOGetInfo(self.__handle, DioInfoItem.PORT_TYPE, i,
                                   byref(port_type))
            if err != 0:
                raise ULException(err)

            for d_port_type in DigitalPortType:
                if port_type.value == d_port_type:
                    port_types_list.append(d_port_type)

        return port_types_list

    def get_port_info(self, port_type):
        # type: (DigitalPortType) -> DioPortInfo
        """
        Gets the port information object for the specified port
        on the device referenced by the :class:`DioInfo` object.

        Args:
            port_type (DigitalPortType): The digital port type.

        Returns:
            DioPortInfo:

            The port type and number of bits in the port.

        Raises:
            :class:`ULException`
        """
        number_of_bits = c_longlong()
        port_io_type = c_longlong()

        port_types_list = self.get_port_types()

        if port_type in port_types_list:
            port_index = port_types_list.index(port_type)
            err = lib.ulDIOGetInfo(self.__handle, DioInfoItem.NUM_BITS,
                                   port_index, byref(number_of_bits))
            if err != 0:
                raise ULException(err)

            err = lib.ulDIOGetInfo(self.__handle, DioInfoItem.PORT_IO_TYPE,
                                   port_index, byref(port_io_type))
            if err != 0:
                raise ULException(err)
        else:
            raise ULException(ULError.BAD_PORT_TYPE)

        pio_type = DigitalPortIoType.IN

        for d_port_io_type in DigitalPortIoType:
            if port_io_type.value == d_port_io_type:
                pio_type = d_port_io_type
                break

        port_info = DioPortInfo()
        port_info.port_type = port_type
        port_info.number_of_bits = number_of_bits.value
        port_info.port_io_type = pio_type

        return port_info

    def has_pacer(self, direction):
        # type: (DigitalDirection) -> bool
        """
        Determines whether the device referenced by the :class:`DioInfo` object
        supports paced digital operations (scanning)
        for the specified digital direction.

        Args:
            direction (DigitalDirection): The direction of the digital port
            (input or output).

        Returns:
            bool:

            True if the device supports paced digital operations in the
            specified direction.

            False if the device does not support paced digital operations
            in the specified direction.

        Raises:
            :class:`ULException`
        """
        has_pacer = c_longlong()

        err = lib.ulDIOGetInfo(self.__handle, DioInfoItem.HAS_PACER, direction,
                               byref(has_pacer))
        if err != 0:
            raise ULException(err)

        return c_bool(has_pacer).value

    def get_min_scan_rate(self, direction):
        # type: (DigitalDirection) -> float
        """
        Gets the minimum scan rate for the device referenced by the
        :class:`DioInfo` object in samples per second for the specified digital
        direction.

        Args:
            direction (DigitalDirection): The direction of the digital port
                (INPUT or OUTPUT). or output).

        Returns:
            float:

            The minimum scan rate in samples per second.

        Raises:
            :class:`ULException`
        """
        min_scan_rate = c_double()

        err = lib.ulDIOGetInfoDbl(self.__handle, DioInfoItemDbl.MIN_SCAN_RATE,
                                  direction, byref(min_scan_rate))
        if err != 0:
            raise ULException(err)

        return min_scan_rate.value

    def get_max_scan_rate(self, direction):
        # type: (DigitalDirection) -> float
        """
        Gets the maximum scan rate for the device referenced by the
        :class:`DioInfo` object in samples per second for the specified
        digital direction.

        Args:
            direction (DigitalDirection): The direction of the digital port
                (INPUT or OUTPUT).

        Returns:
            float:

            The maximum scan rate in samples per second.

        Raises:
            :class:`ULException`
        """
        max_scan_rate = c_double()

        err = lib.ulDIOGetInfoDbl(self.__handle, DioInfoItemDbl.MAX_SCAN_RATE,
                                  direction, byref(max_scan_rate))
        if err != 0:
            raise ULException(err)

        return max_scan_rate.value

    def get_max_throughput(self, direction):
        # type: (DigitalDirection) -> float
        """
        Gets the maximum throughput for the device referenced by
        the :class:`DioInfo` object in samples per second for the
        specified digital direction.

        Args:
            direction (DigitalDirection): The direction of the digital port
                (INPUT or OUTPUT).

        Returns:
            float:

            The maximum throughput in samples per second.

        Raises:
            :class:`ULException`
        """
        max_throughput = c_double()

        err = lib.ulDIOGetInfoDbl(self.__handle, DioInfoItemDbl.MAX_THROUGHPUT,
                                  direction, byref(max_throughput))
        if err != 0:
            raise ULException(err)

        return max_throughput.value

    def get_fifo_size(self, direction):
        # type: (DigitalDirection) -> int
        """
        Gets the FIFO size in bytes for the device referenced by the
        :class:`DioInfo` object for the specified digital direction.

        Args:
            direction (DigitalDirection): The direction of the digital port
                (INPUT or OUTPUT).

        Returns:
            int:

            The FIFO size in bytes.

        Raises:
            :class:`ULException`
        """
        fifo_size = c_longlong()

        err = lib.ulDIOGetInfo(self.__handle, DioInfoItem.FIFO_SIZE, direction,
                               byref(fifo_size))
        if err != 0:
            raise ULException(err)

        return fifo_size.value

    def get_scan_options(self, direction):
        # type: (DigitalDirection) -> list[ScanOption]
        """
        Gets a list of :class:`ScanOption` attributes (suitable for bit-wise
        operations) specifying scan options supported by the device referenced
        by the :class:`DioInfo` object for the specified digital direction.

        Args:
            direction (DigitalDirection): The direction of the digital port
                (INPUT or OUTPUT).

        Returns:
            list[ScanOption]:

            A list of supported scan options.

        Raises:
            :class:`ULException`
        """
        scan_options_mask = c_longlong()

        err = lib.ulDIOGetInfo(self.__handle, DioInfoItem.SCAN_OPTIONS,
                               direction, byref(scan_options_mask))
        if err != 0:
            raise ULException(err)

        return enum_mask_to_list(ScanOption, scan_options_mask.value)

    def get_trigger_types(self, direction):
        # type: (DigitalDirection) -> list[TriggerType]
        """
        Gets a list of supported trigger types for the device referenced
        by the :class:`DioInfo` object for the specified digital direction.

        Args:
            direction (DigitalDirection): The direction of the digital port
                (INPUT or OUTPUT).

        Returns:
            list[TriggerType]:

            A list of the supported trigger types.

        Raises:
            :class:`ULException`
        """
        trigger_types_mask = c_longlong()

        err = lib.ulDIOGetInfo(self.__handle, DioInfoItem.TRIG_TYPES, direction,
                               byref(trigger_types_mask))
        if err != 0:
            raise ULException(err)

        return enum_mask_to_list(TriggerType, trigger_types_mask.value)

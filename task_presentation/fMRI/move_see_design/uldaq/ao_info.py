"""
Created on Mar 5, 2018

@author: MCC
"""
from ctypes import c_longlong, byref, c_double, c_bool
from .ul_c_interface import lib, AoInfoItem, AoInfoItemDbl
from .ul_exception import ULException
from .ul_enums import ScanOption, Range, TriggerType
from .utils import enum_mask_to_list


class AoInfo:
    """
    The instance of the AoInfo class is obtained by calling
    :func:`AoDevice.get_info`.

    """

    def __init__(self, handle):
        self.__handle = handle

    def get_num_chans(self):
        # type: () -> int
        """
        Gets the total number of D/A channels for the device
        referenced by the :class:`AoInfo` object.

        Returns:
            int:

            The number of analog output channels.

        Raises:
            :class:`ULException`
        """
        number_of_channels = c_longlong()
        err = lib.ulAOGetInfo(self.__handle, AoInfoItem.NUM_CHANS, 0,
                              byref(number_of_channels))
        if err != 0:
            raise ULException(err)
        return number_of_channels.value

    def get_resolution(self):
        # type: () -> int
        """
        Gets the D/A resolution in number of bits for the device
        referenced by the :class:`AoInfo` object.

        Returns:
            int:

            The number of bits of resolution (integer) for the
            A/D converter on the device.

        Raises:
            :class:`ULException`
        """
        resolution = c_longlong()
        err = lib.ulAOGetInfo(self.__handle, AoInfoItem.RESOLUTION, 0,
                              byref(resolution))
        if err != 0:
            raise ULException(err)
        return resolution.value

    def get_min_scan_rate(self):
        # type: () -> float
        """
        Gets the minimum scan rate for the device
        referenced by the :class:`AoInfo` object in samples per second.

        Returns:
            float:

            The minimum scan rate in samples per second.

        Raises:
            :class:`ULException`
        """
        min_scan_rate = c_double()
        err = lib.ulAOGetInfoDbl(self.__handle, AoInfoItemDbl.MIN_SCAN_RATE, 0,
                                 byref(min_scan_rate))
        if err != 0:
            raise ULException(err)
        return min_scan_rate.value

    def get_max_scan_rate(self):
        # type: () -> float
        """
        Gets the maximum scan rate for the device
        referenced by the :class:`AoInfo` object in samples per second.

        Returns:
            float:

            The maximum scan rate in samples per second.

        Raises:
            :class:`ULException`
        """
        max_scan_rate = c_double()
        err = lib.ulAOGetInfoDbl(self.__handle, AoInfoItemDbl.MAX_SCAN_RATE, 0,
                                 byref(max_scan_rate))
        if err != 0:
            raise ULException(err)
        return max_scan_rate.value

    def get_max_throughput(self):
        # type: () -> float
        """
        Gets the maximum throughput for the device
        referenced by the :class:`AoInfo` object in samples per second.

        Returns:
            float:

            The maximum throughput in samples per second.

        Raises:
            :class:`ULException`
        """
        max_throughput = c_double()
        err = lib.ulAOGetInfoDbl(self.__handle, AoInfoItemDbl.MAX_THROUGHPUT, 0,
                                 byref(max_throughput))
        if err != 0:
            raise ULException(err)
        return max_throughput.value

    def get_fifo_size(self):
        # type: () -> int
        """
        Gets the FIFO size in bytes for the device
        referenced by the :class:`AoInfo` object.

        Returns:
            int:

            The FIFO size in bytes.

        Raises:
            :class:`ULException`
        """
        fifo_size = c_longlong()
        err = lib.ulAOGetInfo(self.__handle, AoInfoItem.FIFO_SIZE, 0,
                              byref(fifo_size))
        if err != 0:
            raise ULException(err)
        return fifo_size.value

    def get_scan_options(self):
        # type: () -> list[ScanOption]
        """
        Gets a list of :class:`ScanOption` attributes (suitable
        for bit-wise operations) specifying scan options supported
        by the device referenced by the :class:`AoInfo` object.

        Returns:
            list[ScanOption]:

            A list of supported :class:`ScanOption` values.

        Raises:
            :class:`ULException`
        """
        scan_options_mask = c_longlong()
        err = lib.ulAOGetInfo(self.__handle, AoInfoItem.SCAN_OPTIONS, 0,
                              byref(scan_options_mask))
        if err != 0:
            raise ULException(err)
        return enum_mask_to_list(ScanOption, scan_options_mask.value)

    def has_pacer(self):
        # type: () -> bool
        """
        Determines whether the device referenced by the :class:`AoInfo` object
        supports paced analog output operations.

        Returns:
            bool:

            True if the device has an analog output hardware pacer.
            False if the device does not have an analog output hardware pacer.

        Raises:
            :class:`ULException`
        """
        has_pacer = c_longlong()
        err = lib.ulAOGetInfo(self.__handle, AoInfoItem.HAS_PACER, 0,
                              byref(has_pacer))
        if err != 0:
            raise ULException(err)
        return c_bool(has_pacer).value

    def get_ranges(self):
        # type: () -> list[Range]
        """
        Gets a list of supported ranges for the device referenced by the
        :class:`AoInfo` object.

        Returns:
            list[Range]:

            The list of supported analog ranges.

        Raises:
            :class:`ULException`
        """
        num_ranges = c_longlong()
        ao_range = c_longlong()
        ao_range_list = []

        err = lib.ulAOGetInfo(self.__handle, AoInfoItem.NUM_RANGES, 0,
                              byref(num_ranges))
        if err != 0:
            raise ULException(err)

        for i in range(num_ranges.value):
            err = lib.ulAOGetInfo(self.__handle, AoInfoItem.RANGE, i,
                                  byref(ao_range))
            if err != 0:
                raise ULException(err)
            ao_range_list.append(Range(ao_range.value))

        return ao_range_list

    def get_trigger_types(self):
        # type: () -> list[TriggerType]
        """
        Gets a list of supported trigger types for the device referenced by the
        :class:`AoInfo` object.

        Returns:
            list[TriggerType]:

            The list of supported trigger types.

        Raises:
            :class:`ULException`
        """
        trigger_types_mask = c_longlong()
        err = lib.ulAOGetInfo(self.__handle, AoInfoItem.TRIG_TYPES, 0,
                              byref(trigger_types_mask))
        if err != 0:
            raise ULException(err)
        return enum_mask_to_list(TriggerType, trigger_types_mask.value)

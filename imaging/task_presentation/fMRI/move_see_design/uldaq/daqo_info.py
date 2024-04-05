"""
Created on Mar 19, 2018

@author: MCC
"""
from ctypes import c_longlong, c_double, byref
from .ul_c_interface import lib, DaqoInfoItem, DaqoInfoItemDbl
from .ul_enums import DaqOutChanType, ScanOption, TriggerType
from .ul_exception import ULException
from .utils import enum_mask_to_list


class DaqoInfo:
    """
    An instance of the DaqoInfo class is obtained by calling
    :func:`DaqoDevice.get_info`.
    """

    def __init__(self, handle):
        self.__handle = handle

    def get_channel_types(self):
        # type: () -> list[DaqOutChanType]
        """
        Gets a list of supported :class:`DaqOutChanType` channel types
        for the device referenced by the :class:`DaqoInfo` object.

        Returns:
            list[DaqOutChanType]:

            A list of supported :class:`DaqOutChanType` attributes (suitable for
            bitwise operations) specifying compatible channel types for the
            for the device referenced by the :class:`DaqoInfo` object.

        Raises:
            :class:`ULException`
        """
        chan_types_mask = c_longlong()
        err = lib.ulDaqOGetInfo(self.__handle, DaqoInfoItem.CHAN_TYPES, 0,
                                byref(chan_types_mask))
        if err != 0:
            raise ULException(err)
        return enum_mask_to_list(DaqOutChanType, chan_types_mask.value)

    def get_min_scan_rate(self):
        # type: () -> float
        """
        Gets the minimum scan rate for the device referenced by the
        :class:`DaqoInfo` object in samples per second.

        Returns:
            float:

            The minimum scan rate in samples per second.

        Raises:
            :class:`ULException`
        """
        min_scan_rate = c_double()
        err = lib.ulDaqOGetInfoDbl(self.__handle, DaqoInfoItemDbl.MIN_SCAN_RATE,
                                   0, byref(min_scan_rate))
        if err != 0:
            raise ULException(err)
        return min_scan_rate.value

    def get_max_scan_rate(self):
        # type: () -> float
        """
        Gets the maximum scan rate for the device referenced by the
        :class:`DaqoInfo` object in samples per second.

        Returns:
            float:

            The maximum scan rate in samples per second.

        Raises:
            :class:`ULException`
        """
        max_scan_rate = c_double()
        err = lib.ulDaqOGetInfoDbl(self.__handle, DaqoInfoItemDbl.MAX_SCAN_RATE,
                                   0, byref(max_scan_rate))
        if err != 0:
            raise ULException(err)
        return max_scan_rate.value

    def get_max_throughput(self):
        # type: () -> float
        """
        Gets the maximum throughput for the device referenced by the
        :class:`DaqoInfo` object in samples per second.

        Returns:
            float:

            The maximum throughput.

        Raises:
            :class:`ULException`
        """
        max_throughput = c_double()
        err = lib.ulDaqOGetInfoDbl(self.__handle,
                                   DaqoInfoItemDbl.MAX_THROUGHPUT, 0,
                                   byref(max_throughput))
        if err != 0:
            raise ULException(err)
        return max_throughput.value

    def get_fifo_size(self):
        # type: () -> int
        """
        Gets the FIFO size in bytes for the device referenced
        by the :class:`DaqoInfo` object.

        Returns:
            int:

            The FIFO size in bytes.

        Raises:
            :class:`ULException`
        """
        fifo_size = c_longlong()
        err = lib.ulDaqOGetInfo(self.__handle, DaqoInfoItem.FIFO_SIZE, 0,
                                byref(fifo_size))
        if err != 0:
            raise ULException(err)
        return fifo_size.value

    def get_scan_options(self):
        # type: () -> list[ScanOption]
        """
        Gets a list of supported scan options
        for the device referenced by the :class:`DaqoInfo` object.

        Returns:
            list[ScanOption]:

            A list of supported :class:`ScanOption` attributes (suitable for
            bit-wise operations) specifying supported scan option values.

        Raises:
            :class:`ULException`
        """
        scan_options_mask = c_longlong()
        err = lib.ulDaqOGetInfo(self.__handle, DaqoInfoItem.SCAN_OPTIONS, 0,
                                byref(scan_options_mask))
        if err != 0:
            raise ULException(err)
        return enum_mask_to_list(ScanOption, scan_options_mask.value)

    def get_trigger_types(self):
        # type: () -> list[TriggerType]
        """
        Gets a list of supported trigger types
        for the device referenced by the :class:`DaqoInfo` object.

        Returns:
            list[TriggerType]:

            A list of :class:`TriggerType` attributes (suitable for
            bit-wise operations) specifying
            supported trigger type values.

        Raises:
            :class:`ULException`
        """
        trigger_types_mask = c_longlong()
        err = lib.ulDaqOGetInfo(self.__handle, DaqoInfoItem.TRIG_TYPES, 0,
                                byref(trigger_types_mask))
        if err != 0:
            raise ULException(err)
        return enum_mask_to_list(TriggerType, trigger_types_mask.value)

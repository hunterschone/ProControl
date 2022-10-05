"""
Created on Feb 17 2018

@author: MCC
"""
from ctypes import c_longlong, byref, c_double, c_bool
from .ul_enums import (CounterMeasurementType, CounterMeasurementMode,
                       CounterRegisterType, ScanOption, TriggerType)
from .ul_exception import ULException
from .ul_c_interface import lib, CtrInfoItem, CtrInfoItemDbl
from .utils import enum_mask_to_list


class CtrInfo:
    """
    An instance of the CtrInfo class is obtained by calling
    :func:`CtrDevice.get_info`.

    """

    def __init__(self, handle):
        self.__handle = handle

    def get_num_ctrs(self):
        # type: () -> int
        """
        Gets the total number of counters on the device
        referenced by the :class:`CtrInfo` object.

        Returns:
            int:

            The number of counters.

        Raises:
            :class:`ULException`
        """
        number_of_ctrs = c_longlong()
        err = lib.ulCtrGetInfo(self.__handle, CtrInfoItem.NUM_CTRS, 0,
                               byref(number_of_ctrs))
        if err != 0:
            raise ULException(err)
        return number_of_ctrs.value

    def get_measurement_types(self, counter_number):
        # type: (int) -> list[CounterMeasurementType]
        """
        Gets a list of supported measurement types
        for a specified counter on the device referenced by the
        :class:`CtrInfo` object.

        Args:
            counter_number (int): The counter number.

        Returns:
            list[CounterMeasurementType]:

            A list of :class:`CounterMeasurementType` attributes (suitable for
            bit-wise operations) specifying the compatible measurement types.

        Raises:
            :class:`ULException`
        """
        measurement_types_mask = c_longlong()
        err = lib.ulCtrGetInfo(self.__handle, CtrInfoItem.MEASUREMENT_TYPES,
                               counter_number, byref(measurement_types_mask))
        if err != 0:
            raise ULException(err)
        return enum_mask_to_list(CounterMeasurementType,
                                 measurement_types_mask.value)

    def get_measurement_modes(self, counter_measurement_type):
        # type: (CounterMeasurementType) -> list[CounterMeasurementMode]
        """
        Gets a list of supported measurement modes compatible with the
        specified measurement type on the device referenced by the
        :class:`CtrInfo` object.

        Args:
            counter_measurement_type (CounterMeasurementType): The
                measurement type.

        Returns:
            list[CounterMeasurementMode]:

            A list of :class:`CounterMeasurementMode` attributes (suitable for
            bit-wise operations) specifying the compatible measurement types.

        Raises:
            :class:`ULException`
        """
        measurement_modes_mask = c_longlong()
        err = lib.ulCtrGetInfo(self.__handle, CtrInfoItem.MEASUREMENT_MODES,
                               counter_measurement_type,
                               byref(measurement_modes_mask))
        if err != 0:
            raise ULException(err)
        return enum_mask_to_list(CounterMeasurementMode,
                                 measurement_modes_mask.value)

    def get_register_types(self):
        # type: () -> list[CounterRegisterType]
        """
        Gets a list of supported register types for the device referenced
        by the :class:`CtrInfo` object.

        Returns:
            list[CounterRegisterType]:

            A list of :class:`CtrRegisterType` attributes (suitable for bit-wise
            operations) specifying supported register types.

        Raises:
            :class:`ULException`
        """
        register_types_mask = c_longlong()
        err = lib.ulCtrGetInfo(self.__handle, CtrInfoItem.REGISTER_TYPES, 0,
                               byref(register_types_mask))
        if err != 0:
            raise ULException(err)
        return enum_mask_to_list(CounterRegisterType, register_types_mask.value)

    def get_resolution(self):
        # type: () -> int
        """
        Gets the counter resolution in number of bits for
        the device referenced by the :class:`CtrInfo` object.

        Returns:
            int:

            The number of bits of resolution.

        Raises:
            :class:`ULException`
        """
        resolution = c_longlong()
        err = lib.ulCtrGetInfo(self.__handle, CtrInfoItem.RESOLUTION, 0,
                               byref(resolution))
        if err != 0:
            raise ULException(err)
        return resolution.value

    def get_min_scan_rate(self):
        # type: () -> float
        """
        Gets the minimum scan rate for the device referenced
        by the :class:`CtrInfo` object in samples per second.

        Returns:
            float:

            The minimum scan rate in samples per second.

        Raises:
            :class:`ULException`
        """
        min_scan_rate = c_double()
        err = lib.ulCtrGetInfoDbl(self.__handle, CtrInfoItemDbl.MIN_SCAN_RATE,
                                  0, byref(min_scan_rate))
        if err != 0:
            raise ULException(err)
        return min_scan_rate.value

    def get_max_scan_rate(self):
        # type: () -> float
        """
        Gets the maximum scan rate for the device referenced by the
        :class:`CtrInfo` object in samples per second.

        Returns:
            float:

            The maximum scan rate in samples per second.

        Raises:
            :class:`ULException`
        """
        max_scan_rate = c_double()
        err = lib.ulCtrGetInfoDbl(self.__handle, CtrInfoItemDbl.MAX_SCAN_RATE,
                                  0, byref(max_scan_rate))
        if err != 0:
            raise ULException(err)
        return max_scan_rate.value

    def get_max_throughput(self):
        # type: () -> float
        """
        Gets the maximum throughput for the device referenced by the
        :class:`CtrInfo` object in samples per second.

        Returns:
            float:

            The maximum throughput in samples per second.

        Raises:
            :class:`ULException`
        """
        max_throughput = c_double()
        err = lib.ulCtrGetInfoDbl(self.__handle, CtrInfoItemDbl.MAX_THROUGHPUT,
                                  0, byref(max_throughput))
        if err != 0:
            raise ULException(err)
        return max_throughput.value

    def get_fifo_size(self):
        # type: () -> int
        """
        Gets the FIFO size in bytes for the device referenced by the
        :class:`CtrInfo` object.

        Returns:
            int:

            The FIFO size in bytes.

        Raises:
            :class:`ULException`
        """
        fifo_size = c_longlong()
        err = lib.ulCtrGetInfo(self.__handle, CtrInfoItem.FIFO_SIZE, 0,
                               byref(fifo_size))
        if err != 0:
            raise ULException(err)
        return fifo_size.value

    def get_scan_options(self):
        # type: () -> list[ScanOption]
        """
        Gets a list of scan options supported by the
        device referenced by the :class:`CtrInfo` object.

        Returns:
            list[ScanOption]:

            A list of attributes (suitable for bit-wise operations)
            specifying supported :class:`ScanOption` values.

        Raises:
            :class:`ULException`
        """
        scan_options_mask = c_longlong()
        err = lib.ulCtrGetInfo(self.__handle, CtrInfoItem.SCAN_OPTIONS, 0,
                               byref(scan_options_mask))
        if err != 0:
            raise ULException(err)
        return enum_mask_to_list(ScanOption, scan_options_mask.value)

    def has_pacer(self):
        # type: () -> bool
        """
        Determines whether the device referenced by the :class:`CtrInfo` object
        supports paced counter input operations.

        Returns:
            bool:

            Returns *True* if the device has a counter hardware pacer, or
            *False* if the device does not have a counter hardware pacer.

        Raises:
            :class:`ULException`
        """
        has_pacer = c_longlong()
        err = lib.ulCtrGetInfo(self.__handle, CtrInfoItem.HAS_PACER, 0,
                               byref(has_pacer))
        if err != 0:
            raise ULException(err)
        return c_bool(has_pacer).value

    def get_trigger_types(self):
        # type: () -> list[TriggerType]
        """
        Gets a list of supported trigger types for the
        device referenced by the :class:`CtrInfo` object.

        Returns:
            TriggerType:

            A list of :class:`TriggerType` attributes (suitable for bit-wise
            operations) specifying supported trigger type values.

        Raises:
            :class:`ULException`
        """
        trigger_types_mask = c_longlong()
        err = lib.ulCtrGetInfo(self.__handle, CtrInfoItem.TRIG_TYPES, 0,
                               byref(trigger_types_mask))
        if err != 0:
            raise ULException(err)
        return enum_mask_to_list(TriggerType, trigger_types_mask.value)

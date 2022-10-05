"""
Created on Feb 16 2018

@author: MCC
"""
from ctypes import byref, c_double, c_uint, c_ulonglong, Array, c_longlong
from .ctr_info import CtrInfo
from .ctr_config import CtrConfig
from .ul_c_interface import lib
from .ul_exception import ULException
from .ul_enums import (CounterRegisterType, CounterDebounceMode,
                       CounterDebounceTime, CounterEdgeDetection,
                       CounterMeasurementMode, CounterMeasurementType,
                       CounterTickSize, CConfigScanFlag, TriggerType,
                       ScanStatus, WaitType, ScanOption, CInScanFlag)
from .ul_structs import TransferStatus


class CtrDevice:
    """
    An instance of the CtrDevice class is obtained by calling
    :func:`DaqDevice.get_ctr_device`.
    """

    def __init__(self, handle):
        self.__handle = handle
        self.__ctr_info = CtrInfo(handle)
        self.__ctr_config = CtrConfig(handle)

    def get_info(self):
        # type: () -> CtrInfo
        """
        Gets the counter information object for the device
        referenced by the :class:`CtrDevice` object.

        Returns:
            CtrInfo:

            The :class:`CtrInfo` object used for retrieving information
            about the counter subsystem of the UL DAQ Device.

        """
        return self.__ctr_info

    def get_config(self):
        # type: () -> CtrConfig
        """
        Gets the counter configuration object for the device
        referenced by the :class:`CtrDevice` object.

        Returns:
            CtrConfig:

            The object used for retrieving configuration
            information about the counter subsystem of the UL DAQ Device.
        """
        return self.__ctr_config

    def c_in(self, counter_number):
        # type: (int) -> int
        """
        Reads the value of a count register
        for the device referenced by the :class:`CtrDevice` object.

        Args:
            counter_number (int): The counter number.

        Returns:
            int:

            The data value.

        Raises:
            :class:`ULException`
        """
        data = c_ulonglong()
        err = lib.ulCIn(self.__handle, counter_number, byref(data))
        if err != 0:
            raise ULException(err)
        return data.value

    def c_load(self, counter_number, register_type, load_value):
        # type: (int, CounterRegisterType, int) -> None
        """
        Loads a value into the specified counter register
        for the device referenced by the :class:`CtrDevice` object.

        Args:
            counter_number (int): The counter number.
            register_type (CounterRegisterType): The type of counter register.
            load_value (int): The load value.

        Raises:
            :class:`ULException`
        """
        load = c_ulonglong(load_value)
        err = lib.ulCLoad(self.__handle, counter_number, register_type, load)
        if err != 0:
            raise ULException(err)

    def c_clear(self, counter_number):
        # type: (int) -> None
        """
        Clears the value of a count register for the device referenced
        by the :class:`CtrDevice` object (sets it to 0).

        Args:
            counter_number (int): The counter number to clear.

        Raises:
            :class:`ULException`
        """
        err = lib.ulCClear(self.__handle, counter_number)
        if err != 0:
            raise ULException(err)

    def c_read(self, counter_number, register_type):
        # type: (int, CounterRegisterType) -> int
        """
        Reads the value of the specified counter register
        for the device referenced by the :class:`CtrDevice` object.

        Args:
            counter_number (int): The counter number.
            register_type (CounterRegisterType): The type of counter register.

        Returns:
            int:

            The value of the counter register.

        Raises:
            :class:`ULException`
        """
        data = c_ulonglong()
        err = lib.ulCRead(self.__handle, counter_number, register_type,
                          byref(data))
        if err != 0:
            raise ULException(err)
        return data.value

    def c_in_scan(self, low_counter_num, high_counter_num, samples_per_counter,
                  rate, options, flags, data):
        # type: (int, int, int, float, ScanOption, CInScanFlag, Array[int]) -> float
        """
        Scans a range counters at the specified rate on the
        device referenced by the :class:`CtrDevice` object and stores the
        samples.

        Args:
            low_counter_num (int): The first counter in the scan.
            high_counter_num (int): The last counter in the scan.
            samples_per_counter (int): The number of samples per counter to
                read.
            rate (float): The rate in samples per second per counter.
            options (ScanOption): One or more scan options
                (suitable for bit-wise operations) specifying the
                optional conditions that will be applied to the scan, such as
                continuous or external clock.
            flags (CInScanFlag): One or more flag values (suitable for
                bit-wise operations) specifying the conditioning
                applied to the data before it is returned.
            data (Array[int]): The buffer to receive the data being read. Use
                :class:`create_int_buffer` to create the buffer.

        Returns:
            float:

            The actual input scan rate.

        Raises:
            :class:`ULException`
        """
        rate = c_double(rate)
        err = lib.ulCInScan(self.__handle, low_counter_num, high_counter_num,
                            samples_per_counter, byref(rate),
                            options, flags, data)
        if err != 0:
            raise ULException(err)
        return rate.value

    def c_config_scan(self,
                      counter_number,  # type: int
                      measurement_type,  # type: CounterMeasurementType
                      measurement_mode,  # type: CounterMeasurementMode
                      edge_detection,  # type: CounterEdgeDetection
                      tick_size,  # type: CounterTickSize
                      debounce_mode,  # type: CounterDebounceMode
                      debounce_time,  # type: CounterDebounceTime
                      flags=CConfigScanFlag.DEFAULT  # type: CConfigScanFlag
                     ):  # type: ()-> None
        """
        Configures the specified counter on the device
        referenced by the :class:`CtrDevice` object; for counters with
        programmable types.

        Args:
            counter_number (int): The counter number.
            measurement_type (CounterMeasurementType): The measurement type.
            measurement_mode (CounterMeasurementMode):The measurement mode.
            edge_detection (CounterEdgeDetection): Sets whether to increment
                the counter on a positive edge or negative edge of the
                input signal.
            tick_size (CounterTickSize): An attribute that specifies the
                resolution for measurement modes such as period, pulse width,
                and timing.
            debounce_mode (CounterDebounceMode): The debounce mode.
            debounce_time (CounterDebounceTime): The debounce time.
            flags (Optional[CConfigScanFlag]): One or more flag values
                (suitable for bit-wise operations) specifying the
                conditioning applied to the data before it is returned.

        Raises:
            :class:`ULException`
        """
        err = lib.ulCConfigScan(self.__handle, counter_number, measurement_type,
                                measurement_mode, edge_detection, tick_size,
                                debounce_mode, debounce_time, flags)
        if err != 0:
            raise ULException(err)

    def set_trigger(self, trig_type, trig_chan, level, variance,
                    retrigger_count):
        # type: (TriggerType, int, float, float, int) -> None
        """
        Configures the trigger parameters for the device referenced by
        the :class:`CtrDevice` object that will be used when
        :func:`c_in_scan` is called with the :class:`~ScanOption.RETRIGGER` or
        :class:`~ScanOption.EXTTRIGGER` ScanOption.

        Args:
            trig_type (TriggerType): One of the :class:`TriggerType`
                attributes that determines the type of the external trigger.
            trig_chan (int): The trigger channel; ignored if trig_type is set to
                :class:`~TriggerType.POS_EDGE` :class:`~TriggerType.NEG_EDGE`,
                :class:`~TriggerType.HIGH`, :class:`~TriggerType.LOW`,
                :class:`~TriggerType.GATE_HIGH`, :class:`~TriggerType.GATE_LOW`,
                :class:`~TriggerType.RISING`, or :class:`~TriggerType.FALLING`.
            level (float): The level at or around which the trigger event should
                be detected; ignored if trig_type is set to
                :class:`~TriggerType.POS_EDGE`, :class:`~TriggerType.NEG_EDGE`,
                :class:`~TriggerType.HIGH`, :class:`~TriggerType.LOW`,
                :class:`~TriggerType.GATE_HIGH`, :class:`~TriggerType.GATE_LOW`,
                :class:`~TriggerType.RISING`, or :class:`~TriggerType.FALLING`.
            variance (float): The degree to which the input signal can vary
                relative to the level parameter; ignored for all
                types where level is ignored.
            retrigger_count (int): The number of samples per trigger
                to acquire with each trigger event; ignored unless
                :class:`~ScanOption.RETRIGGER` is set for the scan.

        Raises:
            :class:`ULException`
        """
        trig_level = c_double(level)
        trig_variance = c_double(variance)

        err = lib.ulCInSetTrigger(self.__handle, trig_type, trig_chan,
                                  trig_level, trig_variance, retrigger_count)
        if err != 0:
            raise ULException(err)

    def get_scan_status(self):
        # type: () -> tuple[ScanStatus, TransferStatus]
        """
        Gets the status, count, and index of the counter input scan operation
        on the device referenced by the :class:`CtrDevice` object.

        Returns:
            ScanStatus, TransferStatus:

            A tuple containing the scan status and transfer status
            of the analog output background operation.

        Raises:
            :class:`ULException`
        """
        scan_status = c_uint()
        transfer_status = TransferStatus()

        err = lib.ulCInScanStatus(self.__handle, byref(scan_status),
                                  byref(transfer_status))
        if err != 0:
            raise ULException(err)

        return ScanStatus(scan_status.value), transfer_status

    def scan_stop(self):
        # type: () -> None
        """
        Stops the counter input scan operation currently running
        on the device referenced by the :class:`CtrDevice` object.

        Raises:
            :class:`ULException`
        """
        err = lib.ulCInScanStop(self.__handle)
        if err != 0:
            raise ULException(err)

    def scan_wait(self, wait_type, timeout):
        # type: (WaitType, float) -> None
        """
        Waits until the scan operation completes on the device
        referenced by the :class:`CtrDevice` object, or the specified timeout
        elapses.

        Args:
            wait_type (WaitType): The wait type`.
            timeout (float): The timeout value in seconds (s); set to -1 to
                wait indefinitely for the scan function to end.

        Raises:
            :class:`ULException`
        """
        wait_param = c_longlong(0)
        err = lib.ulCInScanWait(self.__handle, wait_type, wait_param, timeout)
        if err != 0:
            raise ULException(err)

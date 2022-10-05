"""
Created on Feb 16 2018

@author: MCC
"""
from ctypes import (c_double, byref, c_bool, c_uint, c_ulonglong, Array,
                    c_longlong)
from .ul_exception import ULException
from .ul_c_interface import lib
from .ul_enums import (DigitalPortType, DigitalDirection, DInScanFlag,
                       DOutScanFlag, ScanOption, ScanStatus, TriggerType,
                       ULError)
from .ul_enums import WaitType
from .ul_structs import TransferStatus
from .dio_info import DioInfo
from .dio_config import DioConfig


class DioDevice:
    """
    An instance of the DioDevice class is obtained by calling
    :func:`DaqDevice.get_dio_device`.
    """

    def __init__(self, handle):
        self.__handle = handle
        self.__dio_info = DioInfo(handle)
        self.__dio_config = DioConfig(handle)

    def get_info(self):
        # type: () -> DioInfo
        """
        Gets the Digital I/O information object for the device
        referenced by the :class:`DioDevice` object.

        Returns:
            DioInfo:

            The object used for retrieving information about the
            digital I/O subsystem of the UL DAQ Device.
        """
        return self.__dio_info

    def get_config(self):
        # type: () -> DioConfig
        """
        Gets the Digital I/O configuration object for the device
        referenced by the :class:`DioDevice` object.

        Returns:
            DioConfig:

            The object used for retrieving configuration
            information about the digital I/O subsystem of the UL DAQ Device.
        """
        return self.__dio_config

    def d_config_port(self, port_type, direction):
        # type: (DigitalPortType, DigitalDirection) -> None
        """
        Configures a digital port as input or output
        for the device referenced by the :class:`DioDevice` object.

        Args:
            port_type (DigitalPortType): The digital port type;
                the port must be configurable.
            direction (DigitalDirection): The direction of the digital port
                (input or output).

        Raises:
            :class:`ULException`
        """
        err = lib.ulDConfigPort(self.__handle, port_type, direction)
        if err != 0:
            raise ULException(err)

    def d_config_bit(self, port_type, bit_number, direction):
        # type: (DigitalPortType, int, DigitalDirection) -> None
        """
        Configures a digital bit as input or output for the
        device referenced by the :class:`DioDevice` object. The port must be
        configurable (DigitalPortIoType = BITIO).

        Args:
            port_type (DigitalPortType): The digital port containing the bit to
                configure; the bit must be configurable.
            bit_number (int): The bit number within the specified port.
            direction (DigitalDirection): The bit direction (input or output).

        Raises:
            :class:`ULException`
        """
        err = lib.ulDConfigBit(self.__handle, port_type, bit_number, direction)
        if err != 0:
            raise ULException(err)

    def d_in(self, port_type):
        # type: (DigitalPortType) -> int
        """
        Returns the value read from a digital port
        for the device referenced by the :class:`DioDevice` object.

        Args:
            port_type (DigitalPortType): Digital port to read.

        Returns:
            int:

            The value of the digital port.

        Raises:
            :class:`ULException`
        """
        data = c_ulonglong()

        err = lib.ulDIn(self.__handle, port_type, byref(data))
        if err != 0:
            raise ULException(err)

        return data.value

    def d_out(self, port_type, data):
        # type: (DigitalPortType, int) -> None
        """
        Writes the specified value to a digital output port
        for the device referenced by the :class:`DioDevice` object.

        Args:
            port_type (DigitalPortType): The digital port.
            data (int): The value to write to the digital port.

        Raises:
            :class:`ULException`
        """
        err = lib.ulDOut(self.__handle, port_type, data)
        if err != 0:
            raise ULException(err)

    def d_bit_in(self, port_type, bit_number):
        # type: (DigitalPortType, int) -> int
        """
        Returns the value read from a digital bit
        for the device referenced by the :class:`DioDevice` object.

        Args:
            port_type (DigitalPortType): Digital port
                containing the bit to read.
            bit_number (int): The bit position within the port to read.

        Returns:
            int:

            The value of the digital bit.

        Raises:
            :class:`ULException`
        """
        data = c_uint()

        err = lib.ulDBitIn(self.__handle, port_type, bit_number, byref(data))
        if err != 0:
            raise ULException(err)

        return c_bool(data).value

    def d_bit_out(self, port_type, bit_number, data):
        # type: (DigitalPortType, int, int) -> None
        """
        Writes the specified value to a digital output bit
        for the device referenced by the :class:`DioDevice` object.

        Args:
            port_type (DigitalPortType): The digital port
                containing the bit to be written to.
            bit_number (int): The number of the bit to be written to.
            data (int): The bit value to write.

        Raises:
            :class:`ULException`
        """
        err = lib.ulDBitOut(self.__handle, port_type, bit_number, data)
        if err != 0:
            raise ULException(err)

    def d_in_scan(self, low_port_type, high_port_type, samples_per_port, rate,
                  options, flags, data):
        # type: (DigitalPortType, DigitalPortType, int, float, ScanOption, DInScanFlag, Array[int]) -> float
        """
        Scans a range of digital ports at the specified rate on the device
        referenced by the :class:`DioDevice` object.

        Args:
            low_port_type (DigitalPortType): First digital port in the scan.
            high_port_type (DigitalPortType): Last digital port in the scan.
            samples_per_port (int): The number of samples to read.
            rate (float): The sample input rate, in samples per second.
            options (ScanOption): One or more attributes
                (suitable for bit-wise operations) specifying the
                optional conditions that will be applied to the scan, such as
                continuous or external clock.
            flags (DInScanFlag): One or more :class:`DInScanFlag` attributes
                (suitable for bit-wise operations) specifying the conditioning
                applied to the data before it is returned.
            data (Array[int]): The buffer in which the digital data is returned.
                Use :class:`create_int_buffer` to create the buffer.

        Returns:
            float:

            The actual sample input rate of the scan.

        Raises:
            :class:`ULException`
        """
        rate = c_double(rate)

        err = lib.ulDInScan(self.__handle, low_port_type, high_port_type,
                            samples_per_port, byref(rate), options, flags, data)
        if err != 0:
            raise ULException(err)

        return rate.value

    def d_out_scan(self, low_port_type, high_port_type, samples_per_port, rate,
                   options, flags, data):
        # type: (DigitalPortType, DigitalPortType, int, float, ScanOption, DOutScanFlag, Array[int]) -> float
        """
        Scans data to a range of digital output ports at the specified rate
        on the device referenced by the :class:`DioDevice` object.

        Args:
            low_port_type (DigitalPortType): First digital port in the scan.
            high_port_type (DigitalPortType): Last digital port in the scan.
            samples_per_port (int): The number of samples per port to write.
            rate (float): The sample output rate, in samples per second.
            options (ScanOption): One or more :class:`ScanOption` attributes
                (suitable for bit-wise operations) specifying the
                optional conditions that will be applied to the scan, such as
                continuous or external clock.
            flags (DOutScanFlag): One or more :class:`DOutScanFlag` attributes
                (suitable for bit-wise operations) specifying the conditioning
                applied to the data before it is output.
            data (Array[int]): The data buffer to write to the digital port.
                Use :class:`create_int_buffer` to create the buffer.

        Returns:
            float:

            The actual sample output rate of the scan.

        Raises:
            :class:`ULException`
        """
        rate = c_double(rate)

        err = lib.ulDOutScan(self.__handle, low_port_type, high_port_type,
                             samples_per_port, byref(rate), options, flags,
                             data)
        if err != 0:
            raise ULException(err)

        return rate.value

    def d_in_set_trigger(self, trig_type, trig_chan, level, variance,
                         retrigger_sample_count):
        # type: (TriggerType, int, float, float, int) -> None
        """
        Configures the trigger parameters for the device referenced by the
        :class:`DioDevice` object that will be used when :class:`d_in_scan` is
        called with :class:`~ScanOption.RETRIGGER` or
        :class:`~ScanOption.EXTTRIGGER`.

        Args:
            trig_type (TriggerType): One of the class:`TriggerType` attributes
                that determines the type of the external trigger.
            trig_chan (int): The trigger channel; ignored if trig_type is set to
                :class:`~TriggerType.POS_EDGE` :class:`~TriggerType.NEG_EDGE`,
                :class:`~TriggerType.HIGH`, :class:`~TriggerType.LOW`,
                :class:`~TriggerType.GATE_HIGH`, :class:`~TriggerType.GATE_LOW`,
                :class:`~TriggerType.RISING`, or :class:`~TriggerType.FALLING`.
            level (float): The level at or around which the trigger event should
                be detected; ignored if trig_type is set to
                :class:`~TriggerType.POS_EDGE` :class:`~TriggerType.NEG_EDGE`,
                :class:`~TriggerType.HIGH`, :class:`~TriggerType.LOW`,
                :class:`~TriggerType.GATE_HIGH`, :class:`~TriggerType.GATE_LOW`,
                :class:`~TriggerType.RISING`, or :class:`~TriggerType.FALLING`.
            variance (float): The degree to which the input signal can vary
                relative to the level parameter; ignored for all types where
                level is ignored. For pattern triggering, this argument serves
                as the mask value.
            retrigger_sample_count (int): The number of samples per trigger to
                acquire with each trigger event; ignored unless
                :class:`~ScanOption.RETRIGGER` is set for the scan.

        Raises:
            :class:`ULException`
        """
        err = lib.ulDInSetTrigger(self.__handle, trig_type, trig_chan, level,
                                  variance, retrigger_sample_count)

        if err != 0:
            raise ULException(err)

    def d_out_set_trigger(self, trig_type, trig_chan, level, variance,
                          retrigger_sample_count):
        # type: (TriggerType, int, float, float, int) -> None
        """
        Configures the trigger parameters for the device referenced by the
        :class:`DioDevice` object that will be used when :class:`d_out_scan` is
        called with :class:`~ScanOption.RETRIGGER` or
        :class:`~ScanOption.EXTTRIGGER`.

        Args:
            trig_type (TriggerType): One of the :class:`TriggerType` attributes
                that determines the type of the external trigger.
            trig_chan (int): The trigger channel; ignored if trig_type is set to
                :class:`~TriggerType.POS_EDGE` :class:`~TriggerType.NEG_EDGE`,
                :class:`~TriggerType.HIGH`, :class:`~TriggerType.LOW`,
                :class:`~TriggerType.GATE_HIGH`, :class:`~TriggerType.GATE_LOW`,
                :class:`~TriggerType.RISING`, or :class:`~TriggerType.FALLING`.
            level (float): The level at or around which the trigger event should
                be detected; ignored if trig_type is set to
                :class:`~TriggerType.POS_EDGE` :class:`~TriggerType.NEG_EDGE`,
                :class:`~TriggerType.HIGH`, :class:`~TriggerType.LOW`,
                :class:`~TriggerType.GATE_HIGH`, :class:`~TriggerType.GATE_LOW`,
                :class:`~TriggerType.RISING`, or :class:`~TriggerType.FALLING`.
            variance (float): The degree to which the input signal can vary
                relative to the level parameter; ignored for all types where
                level is ignored. For pattern triggering, this argument serves
                as the mask value.
            retrigger_sample_count (int): The number of samples per trigger to
                acquire with each trigger event; ignored unless
                :class:`~ScanOption.RETRIGGER` is set for the scan.

        Raises:
            :class:`ULException`
        """
        err = lib.ulDOutSetTrigger(self.__handle, trig_type, trig_chan, level,
                                   variance, retrigger_sample_count)
        if err != 0:
            raise ULException(err)

    def d_in_get_scan_status(self):
        # type: () -> tuple[ScanStatus, TransferStatus]
        """
        Gets the status, count, and index of the digital input scan operation
        on the device referenced by the :class:`DioDevice` object.

        Returns:
            ScanStatus, TransferStatus:

            A tuple containing the scan status and transfer status of the
            digital input background operation.

        Raises:
            :class:`ULException`
        """
        status = c_uint()
        transfer_status = TransferStatus()

        err = lib.ulDInScanStatus(self.__handle, byref(status), transfer_status)
        if err != 0:
            raise ULException(err)

        return ScanStatus(status.value), transfer_status

    def d_out_get_scan_status(self):
        # type: () -> tuple[ScanStatus, TransferStatus]
        """
        Gets the status, count, and index of the digital output scan operation
        on the device referenced by the :class:`DioDevice` object.

        Returns:
            ScanStatus, TransferStatus:

            A tuple containing the scan status and transfer status of the
            digital output background operation.

        Raises:
            :class:`ULException`
        """
        status = c_uint()
        transfer_status = TransferStatus()

        err = lib.ulDOutScanStatus(self.__handle, byref(status),
                                   transfer_status)
        if err != 0:
            raise ULException(err)

        return ScanStatus(status.value), transfer_status

    def d_in_scan_stop(self):
        # type: () -> None
        """
        Stops the digital input scan operation currently running
        on the device referenced by the :class:`DioDevice` object.

        Raises:
            :class:`ULException`
        """
        err = lib.ulDInScanStop(self.__handle)
        if err != 0:
            raise ULException(err)

    def d_out_scan_stop(self):
        # type: () -> None
        """
        Stops the digital output scan operation currently running
        on the device referenced by the :class:`DioDevice` object.

        Raises:
            :class:`ULException`
        """
        err = lib.ulDOutScanStop(self.__handle)
        if err != 0:
            raise ULException(err)

    def d_in_scan_wait(self, wait_type, timeout):
        # type: (WaitType, float) -> None
        """
        Waits until the scan operation completes
        on the device referenced by the :class:`DioDevice` object,
        or the specified timeout elapses.

        Args:
            wait_type (WaitType): One or more of the :class:`WaitType`
                attributes (suitable for bit-wise operations) specifying the
                event types to wait for.
            timeout (float): The timeout value in seconds (s); set to -1 to
                wait indefinitely for the scan function to end.

        Raises:
            :class:`ULException`
        """
        wait_param = c_longlong(0)
        err = lib.ulDInScanWait(self.__handle, wait_type, wait_param, timeout)
        if err != 0:
            raise ULException(err)

    def d_out_scan_wait(self, wait_type, timeout):
        # type: (WaitType, float) -> None
        """
        Waits until the scan operation completes on the device referenced by
        the :class:`DioDevice` object, or the specified timeout elapses.

        Args:
            wait_type (WaitType): One or more of the :class:`WaitType`
                attributes (suitable for bit-wise operations) specifying the
                event types to wait for.
            timeout (float): The timeout value in seconds (s); set to -1 to
                wait indefinitely for the scan function to end.

        Raises:
            :class:`ULException`
        """
        wait_param = c_longlong(0)
        err = lib.ulDOutScanWait(self.__handle, wait_type, wait_param, timeout)
        if err != 0:
            raise ULException(err)

    def d_in_list(self, low_port_type, high_port_type):
        # type: (DigitalPortType, DigitalPortType) -> list[int]
        """
        Returns a list of values read from the specified range of digital ports
        for the device referenced by the :class:`DioDevice` object.

        Args:
            low_port_type (DigitalPortType): First digital port to read.
            high_port_type (DigitalPortType): Last digital port to read.

        Returns:
            list[int]:

            A list of values from the specified range of digital ports.

        Raises:
            :class:`ULException`
        """
        num_ports = high_port_type - low_port_type + 1
        ull_array_type = c_ulonglong * num_ports  # type: type
        ull_array = ull_array_type()

        err = lib.ulDInArray(self.__handle, low_port_type, high_port_type,
                             ull_array)
        if err != 0:
            raise ULException(err)

        return list(ull_array)

    def d_out_list(self, low_port_type, high_port_type, data):
        # type: (DigitalPortType, DigitalPortType, list[int]) -> None
        """
        Writes a list of values to the specified range of digital output
        ports for the device referenced by the :class:`DioDevice` object.

        Args:
            low_port_type (DigitalPortType): First digital port to write.
            high_port_type (DigitalPortType): Last digital port to write.
            data (list[int]): The list of values to write to the digital ports.

        Raises:
            :class:`ULException`
        """
        num_ports = high_port_type - low_port_type + 1
        if len(data) != num_ports:
            raise ULException(ULError.BAD_ARG)

        ull_array_type = c_ulonglong * num_ports  # type: type
        ull_array = ull_array_type(*data)

        err = lib.ulDOutArray(self.__handle, low_port_type, high_port_type,
                              ull_array)
        if err != 0:
            raise ULException(err)

    def d_clear_alarm(self, port_type, bit_mask):
        # type: (DigitalPortType, int) -> None
        """
        Clears the alarms for the bits specified by the bit mask within the
        specified :class:`DigitalPortType` of the device referenced by the
        :class:`DioDevice` object.

        Args:
            port_type (DigitalPortType): The digital port containing the bit(s)
                to configure.
            bit_mask (int): A mask of bits within the specified port whose
                alarms will be cleared.

        Raises:
            :class:`ULException`
        """
        err = lib.ulDClearAlarm(self.__handle, port_type, bit_mask)
        if err != 0:
            raise ULException(err)

"""
Created on Feb 16 2018

@author: MCC
"""
from ctypes import c_uint, c_double, c_longlong, byref, Array
from .ul_enums import (AiInputMode, AInFlag, AInScanFlag, Range, ScanOption,
                       ScanStatus, TriggerType, WaitType, TInFlag, TempScale,
                       TInListFlag, ULError)
from .ul_structs import AiQueueElement, TransferStatus
from .ul_exception import ULException
from .ul_c_interface import lib
from .ai_info import AiInfo
from .ai_config import AiConfig


def ai_queue_array(size, queue_list):
    queue_array = AiQueueElement * size  # type: type
    return queue_array(*queue_list)


class AiDevice:
    """
    An instance of the AiDevice class is obtained by calling
    :func:`DaqDevice.get_ai_device`.
    """

    def __init__(self, handle):
        self.__handle = handle
        self.__ai_info = AiInfo(handle)
        self.__ai_config = AiConfig(handle)

    def get_info(self):
        # type: () -> AiInfo
        """
        Gets the analog input information object for the device
        referenced by the :class:`AiDevice` object.

        Returns:
            AiInfo:

            An object used for retrieving information about the analog
            input subsystem of the UL DAQ Device.
        """
        return self.__ai_info

    def get_config(self):
        # type: () -> AiConfig
        """
        Gets the analog input configuration object for the device
        referenced by the :class:`AiDevice` object.

        Returns:
            AiConfig:

            The object used for retrieving configuration
            information about the analog input subsystem of the UL DAQ Device.
        """
        return self.__ai_config

    def a_in(self, channel, input_mode, analog_range, flags):
        # type: (int, AiInputMode, Range, AInFlag) -> float
        """
        Returns the value read from an A/D channel on the device
        referenced by the :class:`AiDevice` object.

        Args:
            channel (int): A/D channel number.
            input_mode (AiInputMode): The input mode of the specified channel.
            analog_range (Range): The range of the data to be read.
            flags (AInFlag): One or more of the :class:`AInFlag` attributes
                (suitable for bit-wise operations) specifying the conditioning
                applied to the data before it is returned.

        Returns:
            float:

            The value of the A/D channel.

        Raises:
            :class:`ULException`
        """
        data = c_double()
        err = lib.ulAIn(self.__handle, channel, input_mode, analog_range, flags,
                        byref(data))
        if err != 0:
            raise ULException(err)
        return data.value

    def a_in_scan(self, low_channel, high_channel, input_mode, analog_range,
                  samples_per_channel, rate, options, flags,
                  data):
        # type: (int, int, AiInputMode, Range, int, float, ScanOption, AInScanFlag, Array[float]) -> float
        """
        Scans a range of A/D channels on the device
        referenced by the :class:`AiDevice` object, and stores the samples.

        Args:
            low_channel (int): First A/D channel in the scan.
            high_channel (int): Last A/D channel in the scan.
            input_mode (AiInputMode): The input mode of the specified channels.
            analog_range (Range): The range of the data being read.
            samples_per_channel (int): the number of A/D samples to collect from
                each channel in the scan.
            rate (float): A/D sample rate in samples per channel per second.
            options (ScanOption): One or more of the attributes
                (suitable for bit-wise operations) specifying the
                optional conditions that will be applied to the scan, such as
                continuous or external clock.
            flags (AInScanFlag): One or more of the attributes
                (suitable for bit-wise operations) specifying the conditioning
                applied to the data before it is returned.
            data (Array[float]): The buffer to receive the data.
                Use :class:`create_float_buffer` to create the buffer.

        Returns:
            float:

            The actual input scan rate of the scan.

        Raises:
            :class:`ULException`
        """
        rate = c_double(rate)
        err = lib.ulAInScan(self.__handle, low_channel, high_channel,
                            input_mode, analog_range, samples_per_channel,
                            byref(rate), options, flags, data)
        if err != 0:
            raise ULException(err)
        return rate.value

    def a_in_load_queue(self, queue):
        # type: (list[AiQueueElement]) -> None
        """
        Loads the A/D queue of the device referenced by the :class:`AiDevice`
        object.

        Args:
            queue (list[AiQueueElement]): A list of AiQueueElement structs,
                each of which contains fields specifying the channel, range,
                and mode.

        Raises:
            :class:`ULException`
        """
        num_elements = len(queue)
        queue_array = ai_queue_array(num_elements, queue)
        err = lib.ulAInLoadQueue(self.__handle, queue_array, num_elements)
        if err != 0:
            raise ULException(err)

    def set_trigger(self, trig_type, trig_chan, level, variance,
                    retrigger_sample_count):
        # type: (TriggerType, int, float, float, int) -> None
        """
        Configures the trigger parameters for the device referenced by the
        :class:`AiDevice` object that will be used when :func:`a_in_scan`
        is called with :class:`~ScanOption.RETRIGGER` or
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
                relative to the level parameter; ignored for all
                types where level is ignored. For pattern triggering,
                this argument serves as the mask value.
            retrigger_sample_count (int): The number of samples per trigger
                to acquire with each trigger event; ignored unless the
                RETRIGGER ScanOption is set for the scan.

        Raises:
            :class:`ULException`
        """
        err = lib.ulAInSetTrigger(self.__handle, trig_type, trig_chan, level,
                                  variance, retrigger_sample_count)
        if err != 0:
            raise ULException(err)

    def get_scan_status(self):
        # type: () -> tuple[ScanStatus, TransferStatus]
        """
        Gets the status, count, and index of an A/D scan operation
        on the device referenced by the :class:`AiDevice` object.

        Returns:
            ScanStatus, TransferStatus:

            A tuple containing the scan status and transfer status for the
            analog input background operation.

        Raises:
            :class:`ULException`
        """
        status = c_uint()
        transfer_status = TransferStatus()
        err = lib.ulAInScanStatus(self.__handle, byref(status), transfer_status)
        if err != 0:
            raise ULException(err)
        return ScanStatus(status.value), transfer_status

    def scan_stop(self):
        # type: () -> None
        """
        Stops the analog input scan operation currently running
        on the device referenced by the :class:`AiDevice` object.

        Raises:
            :class:`ULException`
        """
        err = lib.ulAInScanStop(self.__handle)
        if err != 0:
            raise ULException(err)

    def scan_wait(self, wait_type, timeout):
        # type: (WaitType, float) -> None
        """
        Waits until the scan operation completes on the device
        referenced by the :class:`AiDevice` object, or
        the specified timeout elapses.

        Args:
            wait_type (WaitType): One or more of the attributes
                (suitable for bit-wise operations) specifying the
                event types to wait for.
            timeout (float): The timeout value in seconds (s); set to -1 to
                wait indefinitely for the scan function to end.

        Raises:
            :class:`ULException`
        """
        wait_param = c_longlong(0)
        err = lib.ulAInScanWait(self.__handle, wait_type, wait_param, timeout)
        if err != 0:
            raise ULException(err)

    def t_in(self, channel, scale, flags=TInFlag.DEFAULT):
        # type: (int, TempScale, TInFlag) -> float
        """
        Returns a temperature value read from an A/D channel on the device
        referenced by the :class:`AiDevice` object.

        Args:
            channel (int): A/D channel number.
            scale (TempScale): The temperature scaling option for the
                temperature value to be read.
            flags (Optional[TInFlag]): One or more flag values
                (suitable for bit-wise operations) specifying the
                conditioning applied to the data before it is returned.

        Returns:
            float:

            The temperature value of the A/D channel.

        Raises:
            :class:`ULException`
        """
        data = c_double()
        err = lib.ulTIn(self.__handle, channel, scale, flags, byref(data))
        if err != 0:
            raise ULException(err)
        return data.value

    def t_in_list(self, low_chan, high_chan, scale, flags=TInListFlag.DEFAULT,
                  ignore_open_connection=False):
        # type: (int, int, TempScale, TInListFlag, bool) -> list[float]
        """
        Returns a list a temperature values read from the specified range of
        A/D channels on the device referenced by the :class:`AiDevice` object.

        Args:
            low_chan (int): The low A/D channel number in the range of channels.
            high_chan (int): The high A/D channel number in the range of
                channels.
            scale (TempScale): The temperature scaling option for the
                temperature values to be read.
            flags (Optional[TInListFlag]): One or more flag values
                (suitable for bit-wise operations) specifying the
                conditioning applied to the data before it is returned.
            ignore_open_connection (Optional[bool]): If true, exceptions due to
                open thermocouple detection are suppressed and a data value of
                -9999 indicates an open connection error.

        Returns:
            list[float]:

            A list of temperature values for the specified range of A/D
            channels.

        Raises:
            :class:`ULException`
        """
        dbl_array_type = c_double * (high_chan - low_chan + 1)  # type: type
        dbl_array = dbl_array_type()

        err = lib.ulTInArray(self.__handle, low_chan, high_chan, scale,
                             flags, dbl_array)
        if err != 0 and not (ignore_open_connection and
                             err == ULError.OPEN_CONNECTION):
            raise ULException(err)

        return list(dbl_array)

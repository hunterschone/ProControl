"""
Created on Feb 16 2018

@author: MCC
"""
from ctypes import c_uint, byref, c_double, Array, c_longlong
from .ao_info import AoInfo
from .ao_config import AoConfig
from .ul_exception import ULException
from .ul_c_interface import lib
from .ul_enums import (AOutFlag, AOutScanFlag, Range, ScanOption, ScanStatus,
                       WaitType, TriggerType, AOutListFlag, ULError)
from .ul_structs import TransferStatus


class AoDevice:
    """
     An instance of the AoDevice class is obtained by calling
     :func:`DaqDevice.get_ao_device`.

    """

    def __init__(self, handle):
        self.__handle = handle
        self.__ao_info = AoInfo(handle)
        self.__ao_config = AoConfig(handle)

    def get_info(self):
        # type: () -> AoInfo
        """
        Get the analog output information object for the device
        referenced by the :class:`AoDevice` object.

        Returns:
            AoInfo:

            An object used for getting the capabilities of the analog output
            subsystem.
        """
        return self.__ao_info

    def get_config(self):
        # type: () -> AoConfig
        """
        Gets the analog output configuration object for the device
        referenced by the :class:`AoDevice` object.

        Returns:
            AoConfig:

            The object used for retrieving configuration
            information about the analog output subsystem of the UL DAQ Device.
        """
        return self.__ao_config

    def a_out(self, channel, analog_range, flags, data):
        # type: (int, Range, AOutFlag, float) -> None
        """
         Writes the data value to a D/A output channel on the
         device referenced by the :class:`AoDevice` object.

        Args:
            channel (int): D/A channel number.
            analog_range (Range): The range to use when writing data.
            flags (AOutFlag): One or more of the :class:`AOutFlag` attributes
                (suitable for bit-wise operations) tht specifies whether to
                scale and/or calibrate the data.
            data (float): The value to write.

        Returns:
            float:

            The actual output scan rate.

        Raises:
            :class:`ULException`
        """
        err = lib.ulAOut(self.__handle, channel, analog_range,
                         flags, data)
        if err != 0:
            raise ULException(err)

    def a_out_scan(self, low_chan, high_chan, analog_range, samples_per_channel,
                   rate, options, flags, data):
        # type: (int, int, Range, int, float, ScanOption, AOutScanFlag, Array[float]) -> float
        """
        Outputs values to a range of D/A channels on the
        device referenced by the :class:`AoDevice` object.

        Args:
            low_chan (int): First D/A channel in the scan.
            high_chan (int): Last D/A channel in the scan.
            analog_range (Range): The range of the data to be written.
            samples_per_channel (int): Number of D/A samples to output.
            rate (float): Sample output rate in scans per second.
            options (ScanOption): One or more of the attributes
                (suitable for bit-wise operations) specifying the
                optional conditions that will be applied to the scan.
            flags (AOutScanFlag): One or more of the attributes (suitable for
                bit-wise operations) specifying the conditioning applied to
                the data.
            data (Array[float]): The data buffer to write. Use
                :class:`create_float_buffer` to create the buffer.

        Returns:
            float:

            The actual output scan rate.

        Raises:
            :class:`ULException`
        """
        sample_rate = c_double(rate)
        err = lib.ulAOutScan(self.__handle, low_chan, high_chan, analog_range,
                             samples_per_channel, byref(sample_rate), options,
                             flags, data)
        if err != 0:
            raise ULException(err)

        return sample_rate.value

    def get_scan_status(self):
        # type: () -> tuple[ScanStatus, TransferStatus]
        """
        Gets the current status, count, and index of the D/A operation
        for the device referenced by the :class:`AoDevice` object.

        Returns:
            ScanStatus, TransferStatus:

            A tuple containing the scan status and transfer status of the
            analog output background operation.

        Raises:
            :class:`ULException`
        """
        scan_status = c_uint()
        transfer_status = TransferStatus()
        err = lib.ulAOutScanStatus(self.__handle, byref(scan_status),
                                   byref(transfer_status))
        if err != 0:
            raise ULException(err)

        return ScanStatus(scan_status.value), transfer_status

    def scan_stop(self):
        # type: () -> None
        """
        Stops the D/A scan operation currently running on
        the device referenced by the :class:`AoDevice` object.

        Raises:
            :class:`ULException`
        """
        err = lib.ulAOutScanStop(self.__handle)
        if err != 0:
            raise ULException(err)

    def scan_wait(self, wait_type, timeout):
        # type: (WaitType, float) -> None
        """
        Waits until the scan operation completes on
        the device referenced by the :class:`AoDevice` object,
        or the specified timeout elapses.

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
        err = lib.ulAOutScanWait(self.__handle, wait_type, wait_param, timeout)
        if err != 0:
            raise ULException(err)

    def set_trigger(self, trigger_type, channel, level, variance,
                    retrigger_count):
        # type: (TriggerType, int, float, float, int) -> None
        """
        Configures the trigger parameters for the device referenced
        by the :class:`AoDevice` object that will be used
        when :func:`a_out_scan` is called with :class:`~ScanOption.RETRIGGER` or
        :class:`~ScanOption.EXTTRIGGER`.

        Args:
            trigger_type (TriggerType): One of the TriggerType attributes
                that determines the type of the external trigger.
            channel (int): Analog output channel number; ignored if trigger_type
                is set to
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
            retrigger_count (int): The number of samples to generate with each
                trigger event; ignored unless :func:`ScanOption.RETRIGGER`
                is set for the scan.

        Raises:
            :class:`ULException`
        """
        trig_level = c_double(level)
        trig_variance = c_double(variance)

        err = lib.ulAOutSetTrigger(self.__handle, trigger_type, channel,
                                   trig_level, trig_variance, retrigger_count)
        if err != 0:
            raise ULException(err)

    def a_out_list(self, low_chan, high_chan, ranges, flags, data):
        # type: (int, int, list[Range], AOutListFlag, list[float]) -> None
        """
        Writes a list of values to the specified range of D/A channels for the
        device referenced by the :class:`AoDevice` object.

        Args:
            low_chan (int): The low D/A channel number in the range of channels.
            high_chan (int): The high D/A channel number in the range of
                channels.
            ranges (list[Range]): The range to use for each of the channels in
                the specified range of channels.
            flags (AOutListFlag): One or more of the attributes
                (suitable for bit-wise operations) specifying the conditioning
                applied to the data.
            data (list[float]): The values to write to the specified range of
                D/A channels.

        Raises:
            :class:`ULException`
        """
        num_channels = high_chan - low_chan + 1
        if len(ranges) != num_channels or len(data) != num_channels:
            raise ULException(ULError.BAD_ARG)

        range_array_type = c_uint * num_channels  # type: type
        range_array = range_array_type(*ranges)

        data_array_type = c_double * num_channels  # type: type
        data_array = data_array_type(*data)

        err = lib.ulAOutArray(self.__handle, low_chan, high_chan, range_array,
                              flags, data_array)
        if err != 0:
            raise ULException(err)

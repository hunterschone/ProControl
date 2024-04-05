"""
Created on Feb 16 2018

@author: MCC
"""
from ctypes import c_double, c_uint, byref, Array, c_longlong
from .daqo_info import DaqoInfo
from .ul_c_interface import lib
from .ul_exception import ULException
from .ul_enums import ScanStatus, WaitType, TriggerType, ScanOption, DaqOutScanFlag
from .ul_structs import DaqOutChanDescriptor, TransferStatus


def _daqo_chan_descriptor_array(size, descriptor_list):
    chan_descriptor_array = DaqOutChanDescriptor * size  # type: type
    return chan_descriptor_array(*descriptor_list)


class DaqoDevice:
    """
    An instance of the DaqoDevice class is obtained by calling
    :func:`DaqDevice.get_daqo_device`.
    """

    def __init__(self, handle):
        self.__handle = handle
        self.__daqo_info = DaqoInfo(handle)

    def get_info(self):
        # type: () -> DaqoInfo
        """
        Gets the DAQ output information object for the device
        referenced by the :class:`DaqoDevice` object.

        Returns:
            DaqoInfo:

            A DaqoInfo object used for retrieving information about the
            DAQ output subsystem of the UL DAQ Device.
        """
        return self.__daqo_info

    def daq_out_scan(self, channel_descriptors, samples_per_channel, rate,
                     options, flags, data):
        # type: (list[DaqOutChanDescriptor], int, float, ScanOption, DaqOutScanFlag, Array[float]) -> float
        """
        Outputs values synchronously to multiple output subsystems, such as
        analog and digital subsystems, on the device referenced by the
        :class:`DaqoDevice` object. This method only works with devices that
        support synchronous output.

        Args:
            channel_descriptors (list[DaqOutChanDescriptor]): A list of
                DaqOutChanDescriptor objects.
            samples_per_channel (int): The number of samples per channel to
                output.
            rate (float): The sample rate in scans per second.
            options (ScanOption): One or more attributes (suitable for bit-wise
                operations) specifying the optional conditions that will be
                applied to the scan, such as continuous or external clock.
            flags (DaqOutScanFlag): One or more attributes (suitable for
                bit-wise operations) specifying the conditioning applied to the
                data.
            data (Array[float]): The data buffer to be written. Use
                :class:`create_float_buffer` to create the buffer.

        Returns:
            float:

            The actual output scan rate.

        Raises:
            :class:`ULException`
        """
        sample_rate = c_double(rate)
        number_of_channels = len(channel_descriptors)
        chan_descriptor_array = _daqo_chan_descriptor_array(number_of_channels,
                                                            channel_descriptors)
        err = lib.ulDaqOutScan(self.__handle, chan_descriptor_array,
                               number_of_channels, samples_per_channel,
                               byref(sample_rate), options, flags, data)
        if err != 0:
            raise ULException(err)

        return sample_rate.value

    def get_scan_status(self):
        # type: () -> tuple[ScanStatus, TransferStatus]
        """
        Gets the current status, count, and index of the synchronous output scan
        operation on the device referenced by the :class:`DaqoDevice` object.

        Returns:
            ScanStatus, TransferStatus:

            A tuple containing the scan status and transfer status for the
            daq input background operation.

        Raises:
            :class:`ULException`
        """
        scan_status = c_uint()
        transfer_status = TransferStatus()
        err = lib.ulDaqOutScanStatus(self.__handle, byref(scan_status),
                                     byref(transfer_status))
        if err != 0:
            raise ULException(err)

        return ScanStatus(scan_status.value), transfer_status

    def scan_stop(self):
        # type: () -> None
        """
        Stops the synchronous output scan operation currently running
        on the device referenced by the :class:`DaqoDevice` object.

        Raises:
            :class:`ULException`
        """
        err = lib.ulDaqOutScanStop(self.__handle)
        if err != 0:
            raise ULException(err)

    def scan_wait(self, wait_type, timeout):
        # type: (WaitType, float) -> None
        """
        Waits until the scan operation completes on the device referenced by
        the :class:`DaqoDevice` object, or the specified timeout elapses.

        Args:
            wait_type (WaitType): The wait type.
            timeout (float): The timeout value in seconds (s); set to -1 to
                wait indefinitely for the scan function to end.

        Raises:
            :class:`ULException`
        """
        wait_param = c_longlong(0)
        err = lib.ulDaqOutScanWait(self.__handle, wait_type, wait_param,
                                   timeout)
        if err != 0:
            raise ULException(err)

    def set_trigger(self, trigger_type, trigger_channel, level, variance,
                    retrigger_sample_count):
        # type: (TriggerType, DaqOutChanDescriptor, float, float, int) -> None
        """
        Configures the trigger parameters for the device referenced by the
        :class:`DaqoDevice` object that will be used when :func:`daq_out_scan`
        is called with the :class:`~ScanOption.RETRIGGER` or
        :class:`~ScanOption.EXTTRIGGER` ScanOption.

        Args:
            trigger_type (TriggerType): One of the :class:`TriggerType`
                attributes that determines the type of the external trigger.
            trigger_channel (DaqOutChanDescriptor): The trigger channel.
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
                :class:`ScanOption.RETRIGGER` is set for the scan.

        Raises:
            :class:`ULException`
        """
        trig_level = c_double(level)
        trig_variance = c_double(variance)

        err = lib.ulDaqOutSetTrigger(self.__handle, trigger_type,
                                     trigger_channel, trig_level, trig_variance,
                                     retrigger_sample_count)
        if err != 0:
            raise ULException(err)

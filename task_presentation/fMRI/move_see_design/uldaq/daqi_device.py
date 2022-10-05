"""
Created on Feb 16 2018

@author: MCC
"""

from ctypes import c_uint, c_double, byref, Array, c_longlong
from .ul_enums import (TriggerType, ScanStatus, WaitType, ScanOption,
                       DaqInScanFlag)
from .ul_structs import DaqInChanDescriptor, TransferStatus
from .ul_exception import ULException
from .ul_c_interface import lib
from .daqi_info import DaqiInfo


def _daqi_chan_descriptor_array(size, descriptor_list):
    chan_descriptor_array = DaqInChanDescriptor * size  # type: type
    return chan_descriptor_array(*descriptor_list)


class DaqiDevice:
    """
    An instance of the DaqiDevice class is obtained by calling
    :func:`DaqDevice.get_daqi_device`.
    """

    def __init__(self, handle):
        self.__handle = handle
        self.__daqi_info = DaqiInfo(handle)

    def get_info(self):
        # type: () -> DaqiInfo
        """
        Gets the DAQ input information object for the device
        referenced by the :class:`DaqiDevice` object.

        Returns:
            DaqiInfo:

            A DaqiInfo object used for retrieving
            information about the DAQ input subsystem of the UL DAQ Device.
        """
        return self.__daqi_info

    def set_trigger(self, trigger_type, trigger_channel, level, variance,
                    retrigger_sample_count):
        # type: (TriggerType, DaqInChanDescriptor, float, float, int) -> None
        """
        Configures the trigger parameters for the device referenced by the
        :class:`DaqiDevice` object that will be used when
        :func:`daq_in_scan` is called with the :class:`~ScanOption.RETRIGGER`
        or :class:`~ScanOption.EXTTRIGGER` ScanOption.

        Args:
            trigger_type (TriggerType): One of the :class:`TriggerType`
                attributes that determines the type of the external trigger.
            trigger_channel (DaqInChanDescriptor): The trigger channel.
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
        err = lib.ulDaqInSetTrigger(self.__handle, trigger_type, trigger_channel,
                                    level, variance, retrigger_sample_count)
        if err != 0:
            raise ULException(err)

    def daq_in_scan(self, channel_descriptors, samples_per_channel, rate,
                    options, flags, data):
        # type: (list[DaqInChanDescriptor], int, float, ScanOption, DaqInScanFlag, Array[float]) -> float
        """
        Allows scanning of multiple input subsystems, such as analog, digital,
        or counter, on the device referenced by the :class:`DaqiDevice` object
        and stores the samples in an array. This method works only
        with devices that support synchronous input.

        Args:
            channel_descriptors (list[DaqInChanDescriptor]): A list of DAQ input
                channel descriptors.
            samples_per_channel (int): the number of samples to collect from
                each channel in the scan.
            rate (float): Sample input rate in samples per second.
            options (ScanOption): One or more attributes (suitable for bit-wise
                operations) specifying the optional conditions that will be
                applied to the scan, such as continuous or external clock.
            flags (DaqInScanFlag): One or more attributes (suitable for bit-wise
                operations) specifying the conditioning applied to the data
                before it is returned.
            data (Array[float]): The data buffer to receive the data being read.
                Use :class:`create_float_buffer` to create the buffer.

        Returns:
            float:

            The actual input scan rate of the scan.

        Raises:
            :class:`ULException`
        """
        num_channels = len(channel_descriptors)
        rate = c_double(rate)
        chan_descriptor_array = _daqi_chan_descriptor_array(num_channels,
                                                            channel_descriptors)
        err = lib.ulDaqInScan(self.__handle, chan_descriptor_array,
                              num_channels, samples_per_channel, byref(rate),
                              options, flags, data)
        if err != 0:
            raise ULException(err)
        return rate.value

    def get_scan_status(self):
        # type: () -> tuple[ScanStatus, TransferStatus]
        """
        Gets the current status, count, and index of the synchronous input scan
        operation on the device referenced by the :class:`DaqiDevice` object.

        Returns:
            ScanStatus, TransferStatus:

            A tuple containing the scan status and transfer status for the
            daq input background operation.

        Raises:
            :class:`ULException`
        """
        status = c_uint()
        transfer_status = TransferStatus()
        err = lib.ulDaqInScanStatus(self.__handle, byref(status),
                                    transfer_status)
        if err != 0:
            raise ULException(err)
        return ScanStatus(status.value), transfer_status

    def scan_stop(self):
        # type: () -> None
        """
        Stops the synchronous input scan operation currently running
        on the device referenced by the :class:`DaqiDevice` object.

        Raises:
            :class:`ULException`
        """
        err = lib.ulDaqInScanStop(self.__handle)
        if err != 0:
            raise ULException(err)

    def scan_wait(self, wait_type, timeout):
        # type: (WaitType, float) -> None
        """
        Waits until the scan operation completes on the device
        referenced by the :class:`DaqiDevice` object, or the specified timeout
        elapses.

        Args:
            wait_type (WaitType): The wait type.
            timeout (float): The timeout value in seconds (s); set to -1 to
                wait indefinitely for the scan function to end.

        Raises:
            :class:`ULException`
        """
        wait_param = c_longlong(0)
        err = lib.ulDaqInScanWait(self.__handle, wait_type, wait_param, timeout)
        if err != 0:
            raise ULException(err)

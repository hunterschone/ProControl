"""
Created on Feb 17 2018

@author: MCC
"""
from ctypes import c_longlong, c_bool, c_double, byref
from .ul_enums import (AiChanType, AiInputMode, AiQueueType,
                       AiChanQueueLimitation, Range, ScanOption, TriggerType)
from .ul_exception import ULException
from .ul_c_interface import lib, AiInfoItem, AiInfoItemDbl
from .utils import enum_mask_to_list


class AiInfo:
    """
    An instance of the AiInfo class is obtained by calling
    :func:`AiDevice.get_info`.
    """

    def __init__(self, handle):
        self.__handle = handle

    def get_num_chans(self):
        # type: () -> int
        """
        Gets the total number of A/D channels on the device referenced by the
        :class:`AiInfo` object.

        Returns:
            int:

            The number of analog input channels.

        Raises:
            :class:`ULException`
        """
        number_of_channels = c_longlong()
        err = lib.ulAIGetInfo(self.__handle, AiInfoItem.NUM_CHANS, 0,
                              byref(number_of_channels))
        if err != 0:
            raise ULException(err)
        return number_of_channels.value

    def get_num_chans_by_mode(self, input_mode):
        # type: (AiInputMode) -> int
        """
        Gets the number of A/D channels on the device referenced
        by the :class:`AiInfo` object for the specified input mode.

        Args:
            input_mode (AiInputMode): The analog input mode for which the number
                of channels is to be determined

        Returns:
            int:

            The number of analog input channels.

        Raises:
            :class:`ULException`
        """
        number_of_channels = c_longlong()
        err = lib.ulAIGetInfo(self.__handle, AiInfoItem.NUM_CHANS_BY_MODE,
                              input_mode,
                              byref(number_of_channels))
        if err != 0:
            raise ULException(err)

        return number_of_channels.value

    def get_num_chans_by_type(self, channel_type):
        # type: (AiChanType) -> int
        """
        Gets the number of A/D channels on the device referenced
        by the :class:`AiInfo` object for the specified
        :class:`AiChanType`.

        Args:
            channel_type (AiChanType): The analog channel type for which the
                number of channels is to be determined.

        Returns:
            int:

            The number of analog input channels.

        Raises:
            :class:`ULException`
        """
        number_of_channels = c_longlong()
        err = lib.ulAIGetInfo(self.__handle, AiInfoItem.NUM_CHANS_BY_TYPE,
                              channel_type, byref(number_of_channels))
        if err != 0:
            raise ULException(err)
        return number_of_channels.value

    def get_resolution(self):
        # type: () -> int
        """
        Gets the A/D resolution for the device referenced
        by the :class:`AiInfo` object in number of bits.

        Returns:
            int:

            The number of bits of resolution (integer) for the
            A/D converter on the device.

        Raises:
            :class:`ULException`
        """
        resolution = c_longlong()
        err = lib.ulAIGetInfo(self.__handle, AiInfoItem.RESOLUTION, 0,
                              byref(resolution))
        if err != 0:
            raise ULException(err)
        return resolution.value

    def get_min_scan_rate(self):
        # type: () -> float
        """
        Gets the minimum scan rate for the device referenced
        by the :class:`AiInfo` object in samples per second.

        Returns:
            float:

            The minimum scan rate in samples per second.

        Raises:
            :class:`ULException`
        """
        min_scan_rate = c_double()
        err = lib.ulAIGetInfoDbl(self.__handle, AiInfoItemDbl.MIN_SCAN_RATE, 0,
                                 byref(min_scan_rate))
        if err != 0:
            raise ULException(err)
        return min_scan_rate.value

    def get_max_scan_rate(self):
        # type: () -> float
        """
        Gets the maximum scan rate for the device referenced
        by the :class:`AiInfo` object in samples per second.

        Returns:
            float:

            The maximum scan rate in samples per second.

        Raises:
            :class:`ULException`
        """
        max_scan_rate = c_double()
        err = lib.ulAIGetInfoDbl(self.__handle, AiInfoItemDbl.MAX_SCAN_RATE, 0,
                                 byref(max_scan_rate))
        if err != 0:
            raise ULException(err)
        return max_scan_rate.value

    def get_max_throughput(self):
        # type: () -> float
        """
        Gets the maximum throughput for the device referenced
        by the :class:`AiInfo` object in samples per second.

        Returns:
            float:

            The maximum throughput in samples per second.

        Raises:
            :class:`ULException`
        """
        max_throughput = c_double()
        err = lib.ulAIGetInfoDbl(self.__handle, AiInfoItemDbl.MAX_THROUGHPUT, 0,
                                 byref(max_throughput))
        if err != 0:
            raise ULException(err)
        return max_throughput.value

    def get_max_burst_rate(self):
        # type: () -> float
        """
        Gets the maximum burst rate for the device referenced by the
        :class:`AiInfo` object in samples per second when using
        :class:`ScanOption.BURSTIO`.

        Returns:
            float:

            The maximum burst rate in samples per second.

        Raises:
            :class:`ULException`
        """
        max_burst_rate = c_double()
        err = lib.ulAIGetInfoDbl(self.__handle,
                                 AiInfoItemDbl.MAX_BURST_THROUGHPUT, 0,
                                 byref(max_burst_rate))
        if err != 0:
            raise ULException(err)
        return max_burst_rate.value

    def get_max_burst_throughput(self):
        # type: () -> float
        """
        Gets the maximum burst throughput for the device referenced
        by the :class:`AiInfo` object in samples per second.

        Returns:
            float:

            The maximum burst throughput in samples per second.

        Raises:
            :class:`ULException`
        """
        max_burst_throughput = c_double()
        err = lib.ulAIGetInfoDbl(self.__handle,
                                 AiInfoItemDbl.MAX_BURST_THROUGHPUT, 0,
                                 byref(max_burst_throughput))
        if err != 0:
            raise ULException(err)
        return max_burst_throughput.value

    def get_fifo_size(self):
        # type: () -> int
        """
        Gets the FIFO size in bytes for the device referenced
        by the :class:`AiInfo` object.

        Returns:
            int:

            The FIFO size in bytes.

        Raises:
            :class:`ULException`
        """
        fifo_size = c_longlong()
        err = lib.ulAIGetInfo(self.__handle, AiInfoItem.FIFO_SIZE, 0,
                              byref(fifo_size))
        if err != 0:
            raise ULException(err)
        return fifo_size.value

    def get_scan_options(self):
        # type: () -> list[ScanOption]
        """
        Gets a list of :class:`ScanOption` attributes (suitable
        for bit-wise operations) specifying scan options supported
        by the device referenced by the :class:`AiInfo` object.

        Returns:
            list[ScanOption]:

            A list of supported ScanOption values.

        Raises:
            :class:`ULException`
        """
        scan_options_mask = c_longlong()
        err = lib.ulAIGetInfo(self.__handle, AiInfoItem.SCAN_OPTIONS, 0,
                              byref(scan_options_mask))
        if err != 0:
            raise ULException(err)
        return enum_mask_to_list(ScanOption, scan_options_mask.value)

    def has_pacer(self):
        # type: () -> bool
        """
        Determines whether the device referenced by the :class:`AiInfo` object
        supports paced analog input operations.

        Returns:
            bool:

            True if the device has an analog input hardware pacer.
            False if the device does not have an analog input hardware pacer.

        Raises:
            :class:`ULException`
        """
        has_pacer = c_longlong()
        err = lib.ulAIGetInfo(self.__handle, AiInfoItem.HAS_PACER, 0,
                              byref(has_pacer))
        if err != 0:
            raise ULException(err)
        return c_bool(has_pacer).value

    def get_chan_types(self):
        # type: () -> list[AiChanType]
        """
        Gets a list of :class:`AiChanType` attributes
        (suitable for bit-wise operations) indicating supported
        channel types for the device referenced by the
        :class:`AiInfo` object.

        Returns:
            list[AiChanType]:

            A list of the supported analog channel types.

        Raises:
            :class:`ULException`
        """
        chan_types_mask = c_longlong()
        err = lib.ulAIGetInfo(self.__handle, AiInfoItem.CHAN_TYPES, 0,
                              byref(chan_types_mask))
        if err != 0:
            raise ULException(err)
        return enum_mask_to_list(AiChanType, chan_types_mask.value)

    def get_ranges(self, input_mode):
        # type: (AiInputMode) -> list[Range]
        """
        Gets a list of supported ranges for the specified input mode
        for the device referenced by the :class:`AiInfo` object.

        Args:
            input_mode (AiInputMode): The analog input mode for which the
                supported ranges are to be determined.

        Returns:
            list[Range]:

            The list of supported analog ranges.

        Raises:
            :class:`ULException`
        """
        ai_range = c_longlong()
        ai_range_list = []

        # Get the number of ranges based on the AiInputMode.
        number_of_ranges = c_longlong()
        if input_mode == AiInputMode.DIFFERENTIAL:
            info_item = AiInfoItem.NUM_DIFF_RANGES
        else:
            info_item = AiInfoItem.NUM_SE_RANGES
        err = lib.ulAIGetInfo(self.__handle, info_item, 0,
                              byref(number_of_ranges))
        if err != 0:
            raise ULException(err)

        # Get the supported ranges based on the AiInputMode.
        if input_mode == AiInputMode.DIFFERENTIAL:
            info_item = AiInfoItem.DIFF_RANGE
        else:
            info_item = AiInfoItem.SE_RANGE

        # Loop through the number of ranges and to get the numeric value for
        # the range. Use the numeric value to get the Range enumeration item
        # and store the item in the list being returned
        for i in range(number_of_ranges.value):
            err = lib.ulAIGetInfo(self.__handle, info_item, i, byref(ai_range))
            if err != 0:
                raise ULException(err)
            ai_range_list.append(Range(ai_range.value))

        return ai_range_list

    def get_trigger_types(self):
        # type: () -> list[TriggerType]
        """
        Gets a list of supported trigger types for the device referenced
        by the :class:`AiInfo` object.

        Returns:
            list[TriggerType]:

            The list of supported trigger types.

        Raises:
            :class:`ULException`
        """
        trigger_types_mask = c_longlong()
        err = lib.ulAIGetInfo(self.__handle, AiInfoItem.TRIG_TYPES, 0,
                              byref(trigger_types_mask))
        if err != 0:
            raise ULException(err)
        return enum_mask_to_list(TriggerType, trigger_types_mask.value)

    def get_max_queue_length(self, input_mode):
        # type: (AiInputMode) -> int
        """
        Gets the maximum length of the queue list for the specified channel
        mode for the device referenced by the :class:`AiInfo` object.

        Args:
            input_mode (AiInputMode): The analog input channel mode for
                which the queue length is to be determined.

        Returns:
            int:

            The maximum number of elements in the queue list.

        Raises:
            :class:`ULException`
        """
        max_queue_length = c_longlong()
        err = lib.ulAIGetInfo(self.__handle,
                              AiInfoItem.MAX_QUEUE_LENGTH_BY_MODE, input_mode,
                              byref(max_queue_length))
        if err != 0:
            raise ULException(err)
        return max_queue_length.value

    def get_queue_types(self):
        # type: () -> list[AiQueueType]
        """
        Gets a list of supported queue types for the device referenced
        by the :class:`AiInfo` object.

        Returns:
            list[AiQueueType]:

            The list of supported queue types.

        Raises:
            :class:`ULException`
        """
        queue_types_mask = c_longlong()
        err = lib.ulAIGetInfo(self.__handle, AiInfoItem.QUEUE_TYPES, 0,
                              byref(queue_types_mask))
        if err != 0:
            raise ULException(err)
        return enum_mask_to_list(AiQueueType, queue_types_mask.value)

    def get_chan_queue_limitations(self):
        # type: () -> list[AiChanQueueLimitation]
        """
        Gets a list of supported queue limitations for the device
        referenced by the :class:`AiInfo` object.

        Returns:
            list[AiChanQueueLimitation]:

            The list of queue limitations.

        Raises:
            :class:`ULException`
        """
        queue_limitations_mask = c_longlong()
        err = lib.ulAIGetInfo(self.__handle, AiInfoItem.QUEUE_LIMITS, 0,
                              byref(queue_limitations_mask))
        if err != 0:
            raise ULException(err)
        return enum_mask_to_list(AiChanQueueLimitation,
                                 queue_limitations_mask.value)

    def supports_iepe(self):
        # type: () -> bool
        """
        Determines whether the device referenced by the :class:`AiInfo` object
        supports IEPE excitation for analog input operations.

        Returns:
            bool:

            True if the device supports IEPE excitation.
            False if the device does not support IEPE excitation.

        Raises:
            :class:`ULException`
        """
        supports_iepe = c_longlong()
        err = lib.ulAIGetInfo(self.__handle, AiInfoItem.IEPE_SUPPORTED, 0,
                              byref(supports_iepe))
        if err != 0:
            raise ULException(err)
        return c_bool(supports_iepe).value

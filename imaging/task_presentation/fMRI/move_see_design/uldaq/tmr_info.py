"""
Created on Mar 23 2018

@author: MCC
"""
from .ul_c_interface import lib, TmrInfoItem, TmrInfoItemDbl
from ctypes import c_longlong, byref, c_double
from .ul_exception import ULException
from .ul_enums import TimerType


class TmrInfo:
    """
    An instance of the TmrInfo class is obtained by calling
    :func:`TmrDevice.get_info`.
    """

    def __init__(self, handle):
        self.__handle = handle

    def get_num_tmrs(self):
        # type: () -> int
        """
        Gets the total number of timers on the device referenced
        by the :class:`TmrInfo` object.

        Returns:
            int:

            The total number of timers.

        Raises:
            :class:`ULException`
        """
        number_of_tmrs = c_longlong()
        err = lib.ulTmrGetInfo(self.__handle, TmrInfoItem.NUM_TMRS, 0,
                               byref(number_of_tmrs))
        if err != 0:
            raise ULException(err)
        return number_of_tmrs.value

    def get_timer_type(self, timer_number):
        # type: (int) -> TimerType
        """
        Gets the timer type for the specified timer on the device referenced
        by the :class:`TmrInfo` object.

        Args:
            timer_number (int): The timer number.

        Returns:
            TimerType:

            The :class:`TimerType` for the specified timer.

        Raises:
            :class:`ULException`
        """
        timer_type = c_longlong()
        err = lib.ulTmrGetInfo(self.__handle, TmrInfoItem.TYPE, timer_number,
                               byref(timer_type))
        if err != 0:
            raise ULException(err)
        return TimerType(timer_type.value)

    def get_min_frequency(self):
        # type: () -> float
        """
        Gets the minimum output frequency for the specified timer
        on the device referenced by the :class:`TmrInfo` object.

        Returns:
            float:

            The minimum output frequency.

        Raises:
            :class:`ULException`
        """
        min_freq = c_double()
        err = lib.ulTmrGetInfoDbl(self.__handle, TmrInfoItemDbl.MIN_FREQ, 0,
                                  byref(min_freq))
        if err != 0:
            raise ULException(err)
        return min_freq.value

    def get_max_frequency(self):
        # type: () -> float
        """
        Gets the maximum output frequency for the specified timer
        on the device referenced by the :class:`TmrInfo` object.

        Returns:
            float:

            The maximum output frequency.

        Raises:
            :class:`ULException`
        """
        max_freq = c_double()
        err = lib.ulTmrGetInfoDbl(self.__handle, TmrInfoItemDbl.MAX_FREQ, 0,
                                  byref(max_freq))
        if err != 0:
            raise ULException(err)
        return max_freq.value

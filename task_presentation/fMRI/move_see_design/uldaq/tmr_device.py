"""
Created on Feb 16 2018

@author: MCC
"""
from ctypes import c_double, byref, c_uint
from .tmr_info import TmrInfo
from .ul_enums import TmrIdleState, PulseOutOption, TmrStatus, TriggerType
from .ul_c_interface import lib
from .ul_exception import ULException


class TmrDevice:
    """
    An instance of the TmrDevice class is obtained by calling
    :func:`DaqDevice.get_tmr_device`.
    """

    def __init__(self, handle):
        self.__handle = handle
        self.__tmr_info = TmrInfo(handle)

    def get_info(self):
        # type: () -> TmrInfo
        """
        Gets the timer information object for the device referenced by the
        :class:`TmrDevice` object.

        Returns:
            TmrInfo:

            An object used for retrieving information about the timer
            subsystem of the UL DAQ Device.
        """
        return self.__tmr_info

    def pulse_out_start(self, timer_number, frequency, duty_cycle, pulse_count,
                        initial_delay, idle_state, options):
        # type: (int, float, float, int, float, TmrIdleState, PulseOutOption) -> tuple[float, float, float]
        """
        Starts the specified timer on the device reference by the
        :class:`TmrDevice` object to generate digital pulses at a specified
        frequency and duty cycle.

        Args:
            timer_number (int): The timer number.
            frequency (float): The frequency of the timer pulse output.
            duty_cycle (float): The duty cycle of the timer pulse output.
            pulse_count (int): The number of pulses to generate;
                set to 0 for continuous pulse output
            initial_delay (float): The amount of time in seconds to wait before
                the first pulse is generated at the timer output.
            idle_state (TmrIdleState): The timer idle state.
            options (PulseOutOption): One or more of the
                :class:`PulseOutOption` attributes (suitable for bit-wise
                operations) specifying the optional conditions that will be
                applied to the output, such as external trigger or retrigger.

        Returns:
            float, float, float:

            A tuple containing the actual frequency, duty cycle, and initial
            delay values.

        Raises:
            :class:`ULException`
        """
        pulse_frequency = c_double(frequency)
        pulse_duty_cycle = c_double(duty_cycle)
        pulse_initial_delay = c_double(initial_delay)

        err = lib.ulTmrPulseOutStart(self.__handle, timer_number,
                                     byref(pulse_frequency),
                                     byref(pulse_duty_cycle),
                                     pulse_count, byref(pulse_initial_delay),
                                     idle_state, options)
        if err != 0:
            raise ULException(err)

        return (pulse_frequency.value, pulse_duty_cycle.value,
                pulse_initial_delay.value)

    def pulse_out_stop(self, timer_number):
        # type: (int) -> None
        """
        Stops the specified timer output on the device referenced by the
        :class:`TmrDevice` object.

        Args:
            timer_number (int): The timer number.

        Raises:
            :class:`ULException`
        """
        err = lib.ulTmrPulseOutStop(self.__handle, timer_number)
        if err != 0:
            raise ULException(err)

    def get_pulse_out_status(self, timer_number):
        # type: (int) -> TmrStatus
        """
        Gets the status of the timer output operation for the specified timer
        on the device referenced by the :class:`TmrDevice` object.

        Args:
            timer_number (int): The timer number.

        Returns:
            TmrStatus:

            A :class:`TmrStatus` value.

        Raises:
            :class:`ULException`
        """
        tmr_status = c_uint()
        err = lib.ulTmrPulseOutStatus(self.__handle, timer_number,
                                      byref(tmr_status))
        if err != 0:
            raise ULException(err)
        return TmrStatus(tmr_status.value)

    def set_trigger(self, trig_type, trig_chan, level, variance,
                    retrigger_count):
        # type: (TriggerType, int, float, float, int) -> None
        """
        Configures the trigger parameters that will be used when
        :func:`pulse_out_start` is called with
        :class:`~PulseOutOption.RETRIGGER` or
        :class:`~PulseOutOption.EXTTRIGGER`.
        referenced by the :class:`TmrDevice` object.

        Args:
            trig_type (TriggerType): The digital trigger type.
            trig_chan (int): Ignored.
            level (float): Ignored.
            variance (float): Ignored.
            retrigger_count (int): Ignored.

        Raises:
            :class:`ULException`
        """
        trig_level = c_double(level)
        trig_variance = c_double(variance)

        err = lib.ulCInSetTrigger(self.__handle, trig_type, trig_chan,
                                  trig_level, trig_variance, retrigger_count)
        if err != 0:
            raise ULException(err)

"""
Created on Feb 17 2018

@author: MCC
"""

from ctypes import c_longlong, c_double, byref, create_string_buffer
from .ul_exception import ULException
from .ul_c_interface import lib, AiConfigItem, AiConfigItemDbl, AiConfigItemStr
from .ul_enums import (AiChanType, TcType, AutoZeroMode, AdcTimingMode,
                       IepeMode, CouplingMode, SensorConnectionType, OtdMode,
                       TempUnit, CalibrationType, AiCalTableType,
                       AiRejectFreqType)


class AiConfig:
    """
    An instance of the AiConfig class is obtained by calling
    :func:`AiDevice.get_config`.
    """

    def __init__(self, handle):
        self.__handle = handle

    def set_chan_type(self, channel, chan_type):
        # type: (int, AiChanType) -> None
        """
        Configures the channel type for the specified A/D channel.

        Args:
            channel (int): The A/D channel number.
            chan_type (AiChanType): The channel type to be set.

        Raises:
            :class:`ULException`
        """
        err = lib.ulAISetConfig(self.__handle, AiConfigItem.CHAN_TYPE, channel,
                                chan_type)
        if err != 0:
            raise ULException(err)

    def get_chan_type(self, channel):
        # type: (int) -> AiChanType
        """
        Gets the channel type for the specified A/D channel.

        Args:
            channel (int): The A/D channel number.

        Returns:
            AiChanType:

            The channel type of the specified channel.

        Raises:
            :class:`ULException`
        """
        chan_type = c_longlong()
        err = lib.ulAIGetConfig(self.__handle, AiConfigItem.CHAN_TYPE, channel,
                                byref(chan_type))
        if err != 0:
            raise ULException(err)
        return AiChanType(chan_type.value)

    def set_chan_tc_type(self, channel, tc_type):
        # type: (int, TcType) -> None
        """
        Configures the thermocouple type for the specified A/D channel.

        Args:
            channel (int): The A/D channel number whose thermocouple type is
                being set.
            tc_type (TcType): The thermocouple type to set.

        Raises:
            :class:`ULException`
        """
        err = lib.ulAISetConfig(self.__handle, AiConfigItem.CHAN_TC_TYPE,
                                channel, tc_type)
        if err != 0:
            raise ULException(err)

    def get_chan_tc_type(self, channel):
        # type: (int) -> TcType
        """
        Gets the thermocouple type for the specified A/D channel.

        Args:
            channel (int): The A/D channel number whose thermocouple type is
                being determined.

        Returns:
            TcType:

            The thermocouple type of the specified channel.

        Raises:
            :class:`ULException`
        """
        tc_type = c_longlong()
        err = lib.ulAIGetConfig(self.__handle, AiConfigItem.CHAN_TC_TYPE,
                                channel, byref(tc_type))
        if err != 0:
            raise ULException(err)
        return TcType(tc_type.value)

    def set_chan_sensor_connection_type(self, channel, connection_type):
        # type: (int, SensorConnectionType) -> None
        """
        Sets the sensor connection type for the specified A/D channel.

        Args:
            channel (int): The A/D channel number whose sensor connection type
                is being set.
            connection_type (SensorConnectionType): The sensor connection type.

        Raises:
            :class:`ULException`
        """

        err = lib.ulAISetConfig(self.__handle,
                                AiConfigItem.CHAN_SENSOR_CONNECTION_TYPE,
                                channel, connection_type)
        if err != 0:
            raise ULException(err)

    def get_chan_sensor_connection_type(self, channel):
        # type: (int) -> SensorConnectionType
        """
        Gets the sensor connection type for the specified A/D channel.

        Args:
            channel (int): The A/D channel number whose sensor connection type
                is being determined.

        Returns:
            SensorConnectionType:

            The sensor connection type of the specified channel.

        Raises:
            :class:`ULException`
        """

        connection_type = c_longlong()
        err = lib.ulAIGetConfig(self.__handle,
                                AiConfigItem.CHAN_SENSOR_CONNECTION_TYPE,
                                channel, byref(connection_type))
        if err != 0:
            raise ULException(err)
        return SensorConnectionType(connection_type.value)

    def get_chan_sensor_coefficients(self, channel):
        # type: (int) -> str
        """
        Gets the sensor coefficients being used for the specified A/D channel.

        Args:
            channel (int): The A/D channel number whose sensor coefficients
                are being determined.

        Returns:
            str:

            The sensor coefficients of the specified channel.

        Raises:
            :class:`ULException`
        """

        coefficients = create_string_buffer(1000)
        err = lib.ulAIGetConfig(self.__handle,
                                AiConfigItemStr.CHAN_COEFS,
                                channel, coefficients)
        if err != 0:
            raise ULException(err)
        return coefficients.value.decode('utf-8')

    def set_auto_zero_mode(self, mode):
        # type: (AutoZeroMode) -> None

        err = lib.ulAISetConfig(self.__handle, AiConfigItem.AUTO_ZERO_MODE, 0,
                                mode)
        if err != 0:
            raise ULException(err)

    def get_auto_zero_mode(self):
        # type: () -> AutoZeroMode

        mode = c_longlong()
        err = lib.ulAIGetConfig(self.__handle, AiConfigItem.AUTO_ZERO_MODE, 0,
                                byref(mode))
        if err != 0:
            raise ULException(err)
        return AutoZeroMode(mode.value)

    def set_adc_timing_mode(self, mode):
        # type: (AdcTimingMode) -> None

        err = lib.ulAISetConfig(self.__handle, AiConfigItem.ADC_TIMING_MODE, 0,
                                mode)
        if err != 0:
            raise ULException(err)

    def get_adc_timing_mode(self):
        # type: () -> AdcTimingMode

        mode = c_longlong()
        err = lib.ulAIGetConfig(self.__handle, AiConfigItem.ADC_TIMING_MODE, 0,
                                byref(mode))
        if err != 0:
            raise ULException(err)
        return AdcTimingMode(mode.value)

    def set_chan_iepe_mode(self, channel, mode):
        # type: (int, IepeMode) -> None
        """
        Configures the IEPE mode for the specified A/D channel.

        Args:
            channel (int): The A/D channel number whose IEPE mode is being set.
            mode (IepeMode): The IEPE mode to set

        Raises:
            :class:`ULException`
        """

        err = lib.ulAISetConfig(self.__handle, AiConfigItem.CHAN_IEPE_MODE,
                                channel, mode)
        if err != 0:
            raise ULException(err)

    def get_chan_iepe_mode(self, channel):
        # type: (int) -> IepeMode
        """
        Gets the IEPE mode for the specified A/D channel.

        Args:
            channel (int): The A/D channel number whose IEPE mode is being
                determined.

        Returns:
            IepeMode:

            The IEPE mode of the specified channel.

        Raises:
            :class:`ULException`
        """

        mode = c_longlong()
        err = lib.ulAIGetConfig(self.__handle, AiConfigItem.CHAN_IEPE_MODE,
                                channel, byref(mode))
        if err != 0:
            raise ULException(err)
        return IepeMode(mode.value)

    def set_chan_coupling_mode(self, channel, mode):
        # type: (int, CouplingMode) -> None
        """
        Configures the coupling mode for the specified A/D channel.

        Args:
            channel (int): The A/D channel number whose coupling mode is being
                set.
            mode (CouplingMode): The coupling mode to set.

        Raises:
            :class:`ULException`
        """

        err = lib.ulAISetConfig(self.__handle, AiConfigItem.CHAN_COUPLING_MODE,
                                channel, mode)
        if err != 0:
            raise ULException(err)

    def get_chan_coupling_mode(self, channel):
        # type: (int) -> CouplingMode
        """
        Gets the coupling mode for the specified A/D channel.

        Args:
            channel (int): The A/D channel number whose coupling mode is being
                determined.

        Returns:
            CouplingMode:

            The coupling mode of the specified channel.

        Raises:
            :class:`ULException`
        """

        mode = c_longlong()
        err = lib.ulAIGetConfig(self.__handle, AiConfigItem.CHAN_COUPLING_MODE,
                                channel, byref(mode))
        if err != 0:
            raise ULException(err)
        return CouplingMode(mode.value)

    def set_chan_sensor_sensitivity(self, channel, sensitivity):
        # type: (int, float) -> None
        """
        Configures the sensory sensitivity for the specified A/D channel in
        Volts/unit.

        Args:
            channel (int): The A/D channel number whose sensor sensitivity is
                being set.
            sensitivity (float): The sensor sensitivity in Volts/unit.

        Raises:
            :class:`ULException`
        """

        err = lib.ulAISetConfigDbl(self.__handle,
                                   AiConfigItemDbl.CHAN_SENSOR_SENSIVITY,
                                   channel, sensitivity)
        if err != 0:
            raise ULException(err)

    def get_chan_sensor_sensitivity(self, channel):
        # type: (int) -> float
        """
        Gets the sensor sensitivity for the specified A/D channel in Volts/unit.

        Args:
            channel (int): The A/D channel number whose sensory sensitivity is
                being determined.

        Returns:
            float:

            The sensor sensitivity in Volts/unit.

        Raises:
            :class:`ULException`
        """

        sensitivity = c_double()
        err = lib.ulAIGetConfigDbl(self.__handle,
                                   AiConfigItemDbl.CHAN_SENSOR_SENSIVITY,
                                   channel, byref(sensitivity))
        if err != 0:
            raise ULException(err)
        return sensitivity.value

    def set_chan_slope(self, channel, slope):
        # type: (int, float) -> None
        """
        Configures the slope multiplier for the specified A/D channel.

        Args:
            channel (int): The A/D channel number whose slope is being set.
            slope (float): The slope multiplier value to set.

        Raises:
            :class:`ULException`
        """

        err = lib.ulAISetConfigDbl(self.__handle, AiConfigItemDbl.CHAN_SLOPE,
                                   channel, slope)
        if err != 0:
            raise ULException(err)

    def get_chan_slope(self, channel):
        # type: (int) -> float
        """
        Gets the slope multiplier of the specified A/D channel.

        Args:
            channel (int): The A/D channel number whose slope is being
                determined.

        Returns:
            float:
            The slope multiplier of the specified A/D channel.

        Raises:
            :class:`ULException`
        """

        slope = c_double()
        err = lib.ulAIGetConfigDbl(self.__handle, AiConfigItemDbl.CHAN_SLOPE,
                                   channel, byref(slope))
        if err != 0:
            raise ULException(err)
        return slope.value

    def set_chan_offset(self, channel, offset):
        # type: (int, float) -> None
        """
        Sets the offset value for the specified A/D channel.

        Args:
            channel (int): The A/D channel number whose offset is being set.
            offset (float): The offset value to set.

        Raises:
            :class:`ULException`
        """

        err = lib.ulAISetConfigDbl(self.__handle, AiConfigItemDbl.CHAN_OFFSET,
                                   channel, offset)
        if err != 0:
            raise ULException(err)

    def get_chan_offset(self, channel):
        # type: (int) -> float
        """
        Gets the offset value of the specified A/D channel.

        Args:
            channel (int): The A/D channel number whose offset is being
                determined.

        Returns:
            float:
            The offset of the specified A/D channel.

        Raises:
            :class:`ULException`
        """

        offset = c_double()
        err = lib.ulAIGetConfigDbl(self.__handle, AiConfigItemDbl.CHAN_OFFSET,
                                   channel, byref(offset))
        if err != 0:
            raise ULException(err)
        return offset.value

    def get_cal_date(self, cal_type=CalibrationType.FACTORY):
        # type: (CalibrationType) -> int
        """
        Gets the calibration date for the DAQ device.

        Args:
            cal_type (Optional[CalibrationType]): Optional parameter to set the
                type of calibration whose date is being determined. The default
                type is factory.

        Returns:
            int:

            The date when the device was calibrated last in UNIX Epoch time.

        Raises:
            :class:`ULException`
        """
        cal_date = c_longlong()
        err = lib.ulAIGetConfig(self.__handle, AiConfigItem.CAL_DATE, cal_type,
                                byref(cal_date))
        if err != 0:
            raise ULException(err)
        return cal_date.value

    def set_chan_otd_mode(self, channel, mode):
        # type: (int, OtdMode) -> None
        """
        Configures the open thermocouple detection mode for the specified A/D
        channel.

        Args:
            channel (int): The A/D channel number whose open thermocouple
                detection mode is being set.
            mode (OtdMode): The open thermocouple detection mode to set.

        Raises:
            :class:`ULException`
        """

        err = lib.ulAISetConfig(self.__handle, AiConfigItem.CHAN_OTD_MODE,
                                channel, mode)
        if err != 0:
            raise ULException(err)

    def get_chan_otd_mode(self, channel):
        # type: (int) -> OtdMode
        """
        Gets the open thermocouple detection mode for the specified A/D channel.

        Args:
            channel (int): The A/D channel number whose open thermocouple
                detection mode is being determined.

        Returns:
            OtdMode:

            The open thermocouple detection mode of the specified channel.

        Raises:
            :class:`ULException`
        """

        mode = c_longlong()
        err = lib.ulAIGetConfig(self.__handle, AiConfigItem.CHAN_OTD_MODE,
                                channel, byref(mode))
        if err != 0:
            raise ULException(err)
        return OtdMode(mode.value)

    def set_temp_unit(self, temp_unit):
        # type: (TempUnit) -> None
        """
        Configures the temperature unit for the specified A/D.

        Args:
            temp_unit (TempUnit): The temperature unit to set.

        Raises:
            :class:`ULException`
        """

        err = lib.ulAISetConfig(self.__handle, AiConfigItem.TEMP_UNIT, 0,
                                temp_unit)
        if err != 0:
            raise ULException(err)

    def get_temp_unit(self):
        # type: () -> TempUnit
        """
        Gets the temperature unit for the specified A/D.

        Returns:
            TempUnit:

            The scan temperature unit.

        Raises:
            :class:`ULException`
        """

        temp_unit = c_longlong()
        err = lib.ulAIGetConfig(self.__handle, AiConfigItem.TEMP_UNIT, 0,
                                byref(temp_unit))
        if err != 0:
            raise ULException(err)
        return TempUnit(temp_unit.value)

    def set_chan_data_rate(self, channel, rate):
        # type: (int, float) -> None
        """
        Configures the data rate for the specified A/D channel.

        Args:
            channel (int): The A/D channel number whose data rate is being set.
            rate (float): The data rate value to set.

        Raises:
            :class:`ULException`
        """

        err = lib.ulAISetConfigDbl(self.__handle,
                                   AiConfigItemDbl.CHAN_DATA_RATE, channel,
                                   rate)
        if err != 0:
            raise ULException(err)

    def get_chan_data_rate(self, channel):
        # type: (int) -> float
        """
        Gets the data rate of the specified A/D channel.

        Args:
            channel (int): The A/D channel number whose data rate is being
                determined.

        Returns:
            float:
            The data rate of the specified A/D channel.

        Raises:
            :class:`ULException`
        """

        rate = c_double()
        err = lib.ulAIGetConfigDbl(self.__handle,
                                   AiConfigItemDbl.CHAN_DATA_RATE, channel,
                                   byref(rate))
        if err != 0:
            raise ULException(err)
        return rate.value

    def set_otd_mode(self, mode):
        # type: (OtdMode) -> None
        """
        Configures the open thermocouple detection mode for the A/D.

        Args:
            mode (OtdMode): The open thermocouple detection mode to set.

        Raises:
            :class:`ULException`
        """

        err = lib.ulAISetConfig(self.__handle, AiConfigItem.OTD_MODE,
                                0, mode)
        if err != 0:
            raise ULException(err)

    def get_otd_mode(self):
        # type: () -> OtdMode
        """
        Gets the open thermocouple detection mode for the A/D.

        Returns:
            OtdMode:

            The open thermocouple detection mode of the A/D.

        Raises:
            :class:`ULException`
        """

        mode = c_longlong()
        err = lib.ulAIGetConfig(self.__handle, AiConfigItem.OTD_MODE,
                                0, byref(mode))
        if err != 0:
            raise ULException(err)
        return OtdMode(mode.value)

    def set_calibration_table_type(self, cal_type):
        # type: (AiCalTableType) -> None
        """
        Configures the calibration table type for the A/D.

        Args:
            cal_type (AiCalTableType): The calibration table type to set.

        Raises:
            :class:`ULException`
        """

        err = lib.ulAISetConfig(self.__handle, AiConfigItem.CAL_TABLE_TYPE,
                                0, cal_type)
        if err != 0:
            raise ULException(err)

    def get_calibration_table_type(self):
        # type: () -> AiCalTableType
        """
        Gets the calibration table type for the A/D.

        Returns:
            AiCalTableType:

            The calibration table type of the A/D.

        Raises:
            :class:`ULException`
        """

        cal_type = c_longlong()
        err = lib.ulAIGetConfig(self.__handle, AiConfigItem.CAL_TABLE_TYPE,
                                0, byref(cal_type))
        if err != 0:
            raise ULException(err)
        return AiCalTableType(cal_type.value)

    def set_reject_freq_type(self, reject_freq_type):
        # type: (AiRejectFreqType) -> None
        """
        Configures the rejection frequency type for the A/D.

        Args:
            reject_freq_type (AiRejectFreqType): The rejection frequency
                type to set.

        Raises:
            :class:`ULException`
        """

        err = lib.ulAISetConfig(self.__handle, AiConfigItem.REJECT_FREQ_TYPE,
                                0, reject_freq_type)
        if err != 0:
            raise ULException(err)

    def get_reject_freq_type(self):
        # type: () -> AiRejectFreqType
        """
        Gets the rejection frequency type for the A/D.

        Returns:
            AiRejectFreqType:

            The rejection frequency type of the A/D.

        Raises:
            :class:`ULException`
        """

        reject_freq_type = c_longlong()
        err = lib.ulAIGetConfig(self.__handle, AiConfigItem.REJECT_FREQ_TYPE,
                                0, byref(reject_freq_type))
        if err != 0:
            raise ULException(err)
        return AiRejectFreqType(reject_freq_type.value)

    def get_expansion_cal_date(self, cal_type=CalibrationType.FACTORY):
        # type: (CalibrationType) -> int
        """
        Gets the calibration date of the expansion board connected to the
        DAQ device.

        Args:
            cal_type (Optional[CalibrationType]): Optional parameter to set the
                type of calibration whose date is being determined; The default
                type is factory.

        Returns:
            int:

            The date when the device was calibrated last in UNIX Epoch time.

        Raises:
            :class:`ULException`
        """
        cal_date = c_longlong()
        err = lib.ulAIGetConfig(self.__handle, AiConfigItem.EXP_CAL_DATE,
                                cal_type, byref(cal_date))
        if err != 0:
            raise ULException(err)
        return cal_date.value

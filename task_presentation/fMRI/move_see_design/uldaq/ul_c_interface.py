"""
Created on Mar 7 2018

@author: MCC
"""
from ctypes import (CDLL, CFUNCTYPE, Structure, c_uint, c_int, c_longlong,
                    POINTER, c_double, c_char, py_object, c_ulonglong, cast,
                    c_char_p, c_byte)
from enum import IntEnum
from .ul_structs import DaqDeviceDescriptor, AiQueueElement, TransferStatus
from .ul_structs import DaqInChanDescriptor, MemDescriptor, DaqOutChanDescriptor, EventCallbackArgs
from .ul_enums import DaqEventType
from sys import platform

if platform.startswith('darwin'):
    lib = CDLL('libuldaq.dylib')
else:
    lib = CDLL('libuldaq.so')


#
# Structures
#


class EventParams(Structure):
    _fields_ = [("user_data", py_object),        # the user data
                ("user_callback", py_object), ]


#
# Enums
#


class UlInfoItem (IntEnum):
    """UL version information."""
    VER_STR = 2000,  #: UL version number
    IP_ADDR_STR = 2001,  #: Returns the IP address of the Ethernet DAQ device
    NET_IFC_STR = 2002,  #: Returns the name of the network interface which is used to connect to the Ethernet DAQ device

    
class DevItemInfo (IntEnum):
    """Device information types"""
    HAS_AI_DEV = 1,  #: The DAQ device has an analog input subsystem.
    HAS_AO_DEV = 2,  #: The DAQ device has an analog output subsystem.
    HAS_DIO_DEV = 3,  #: The DAQ device has a Digital I/O subsystem.
    HAS_CTR_DEV = 4,  #: The DAQ device has a counter input subsystem.
    HAS_TMR_DEV = 5,  #: The DAQ device has a timer output subsystem.
    HAS_DAQI_DEV = 6,  #: The DAQ device has a DAQ input subsystem.
    HAS_DAQO_DEV = 7,  #: The DAQ device has an DAQ output subsystem.
    DAQ_EVENT_TYPES = 8,  #: Event types supported by the DAQ device
    MEM_REGIONS = 9,  #: Memory regions supported by the DAQ device


class DevConfigItem (IntEnum):
    """Device Configuration Items"""
    HAS_EXP = 1,  #: The DAQ device has an expansion board attached.
    CONNECTION_CODE = 2,  #: Connection code of the Ethernet DAQ device.
    MEM_UNLOCK_CODE = 3,  #: Memory unlock code.
    RESET = 4,  #: Resets the DAQ device.

    
class AiInfoItem (IntEnum):
    """Use with ulAIGetInfo() to obtain AI subsystem information."""
    RESOLUTION = 1,  #: The A/D resolution in number of bits.
    NUM_CHANS = 2,  #: The number of A/D channels on the specified device.
    NUM_CHANS_BY_MODE = 3,  #: The number of A/D channels for the specified channel mode.
    NUM_CHANS_BY_TYPE = 4,  #: The number of A/D channels for the specified channel type.
    CHAN_TYPES = 5,  #: A bitmask of supported :func:'~ul_daq.AiChanType' values.
    SCAN_OPTIONS = 6,  #: A bitmask of supported :func:'~ul_daq.ScanOption' values.
    HAS_PACER = 7,  #: Paced operations are supported.
    NUM_DIFF_RANGES = 8,  #: A number of supported :func:'~ul_daq.Range' values for differential mode operations.
    NUM_SE_RANGES = 9,  #: A number of supported :func:'~ul_daq.Range' values for single-ended mode operations.
    DIFF_RANGE = 10,  #: The :func:'~ul_daq.Range' for the specified differential range index.
    SE_RANGE = 11,  #: The :func:'~ul_daq.Range' for the specified single-ended range index.
    TRIG_TYPES = 12,  #: A bitmask of supported :func:'~ul_daq.TriggerType' values.
    MAX_QUEUE_LENGTH_BY_MODE = 13,  #: The maximum length of the queue for the specified channel mode.
    QUEUE_TYPES = 14,  #: A bitmask of supported :func:'~ul_daq.AiQueueType' values supported for the specified device.
    QUEUE_LIMITS = 15,  #: A bitmask of supported :func:'~ul_daq.AiChanQueueLimitation' values.
    FIFO_SIZE = 16,  #: FIFO size in bytes.
    IEPE_SUPPORTED = 17,  #: Returns a zero or non-zero value to the infoValue argument. If non-zero, IEPE mode is supported.


class AiInfoItemDbl (IntEnum):
    """Use with ulAIGetInfoDbl() to obtain AI subsystem information."""
    MIN_SCAN_RATE = 1000,  #: The minimum scan rate of the specified device.
    MAX_SCAN_RATE = 1001,  #: The maximum scan rate of the specified device.
    MAX_THROUGHPUT = 1002,  #: The maximum throughput in samples per second of the specified device.
    MAX_BURST_RATE = 1003,  #: The maximum scan rate in samples per second when using :func:'~ul_daq.ScanOption.SO_BURSTIO' mode.
    MAX_BURST_THROUGHPUT = 1004,  #: The maximum throughput in samples per second when using :func:'~ul_daq.ScanOption.SO_BURSTIO' mode.
    
    
class AiConfigItem (IntEnum):
    """Use with ulSetConfig() and ulGetConfig() to perform configuration operations on the AI subsystem."""
    CHAN_TYPE = 1,  #: The channel type of the specified  channel. Set with :func:'~ul_daq.AiChanType'.
    CHAN_TC_TYPE = 2,  #: The thermocouple type of the specified channel. Set with :func:'~ul_daq.TcType'.
    CHAN_TEMP_UNIT = 3,  #: The temperature unit of the specified channel. Set with :func:'~ul_daq.TempUnit'.
    TEMP_UNIT = 4,  #: The temperature unit for the specified device. Set with :func:'~ul_daq.AiChanType'.
    ADC_TIMING_MODE = 5,  #: The timing mode. Set with :func:'~ul_daq.AdcTimingMode'.
    AUTO_ZERO_MODE = 6,  #: The auto zero mode. Set with :func:'~ul_daq.AutoZeroMode'.
    CAL_DATE = 7,  #: The date when the device was calibrated last.
    #: The IEPE current excitation mode for the specified channel. Set with :func:'~ul_daq.IepeMode'.
    CHAN_IEPE_MODE = 8,
    CHAN_COUPLING_MODE = 9,  #: The coupling mode for the specified device. Set with :func:'~ul_daq.CouplingMode'.
    CHAN_SENSOR_CONNECTION_TYPE = 10,  #: The connection type of the sensor connected to the specified channel.
    CHAN_OTD_MODE = 11,  #: The open thermocouple detection mode for the specified channel. Set with :func:'~ul_daq.OtdMode'.
    OTD_MODE = 12,  #: The open thermocouple detection mode.
    CAL_TABLE_TYPE = 13,  #: The calibration table type.
    REJECT_FREQ_TYPE = 14,  #: The rejection frequency type.
    #: The date when the expansion board was calibrated last in UNIX Epoch time.
    #: Set index to 0 for the factory calibration date, or 1 for the field
    #: calibration date. If the value read is not a valid date or the index is
    #: invalid, 0 (Unix Epoch) is returned.
    EXP_CAL_DATE = 15,

class AiConfigItemDbl  (IntEnum):
    """Use with ulSetConfigDbl() and ulGetConfigDbl() to perform configuration operations on the AI subsystem. """
    CHAN_SLOPE = 1000,  #: The custom slope of the specified channel.
    CHAN_OFFSET = 1001,  #: The custom offset of the specified channel.
    CHAN_SENSOR_SENSIVITY = 1002,  #: The sensitivity of the sensor connected to the specified channel.
    CHAN_DATA_RATE = 1003,  #: The data rate of the specified channel.


class AiConfigItemStr(IntEnum):
    #: Calibration date
    CAL_DATE = 2000,
    #: The channel coefficients used for the configured sensor.
    CHAN_COEFS = 2001,
    #: Returns the calibration date of expansion board. Set index to 0 for the
    #: factory calibration date, or 1 for the field calibration date.
    #: If the value read is not a valid date or the index is invalid,
    #: Unix Epoch is returned.
    EXP_CAL_DATE_STR = 2002,


class DioInfoItem (IntEnum):
    """Use with ulDIOGetInfo() to obtain information about the DIO subsystem."""
    NUM_PORTS = 1,  #: The number of ports on the specified device.
    PORT_TYPE = 2,  #: The port type for the specified port index.
    PORT_IO_TYPE = 3,  #: The #DigitalPortIoType for the specified port index.
    NUM_BITS = 4,  #: The number of bits on the port specified by the port index.
    HAS_PACER = 5,  #: Paced operations are supported for the specified digital direction.
    SCAN_OPTIONS = 6,  #: A bit mask of supported :func:'~ul_daq.ScanOption' values for the specified digital direction.
    TRIG_TYPES = 7,  #: A bitmask of supported :func:'~ul_daq.TriggerType' values for the specified digital direction.
    FIFO_SIZE = 8,  #: FIFO size in bytes for the specified digital direction.


class DioInfoItemDbl (IntEnum):
    """Use with ulDIOGetInfoDbl() to obtain information about the DIO subsystem."""
    MIN_SCAN_RATE = 1000,  #: The minimum scan rate of the specified device.
    MAX_SCAN_RATE = 1001,  #: The maximum scan rate of the specified device.
    MAX_THROUGHPUT = 1002,  #: The maximum scanning throughput of the specified device.


class DioConfigItem  (IntEnum):
    """ Use with ulDIOGetConfig() to obtain information about the DIO subsystem configuration. """
    #: The port direction. Set with :func:'~ul_daq.DigitalDirection'.
    PORT_DIRECTION_MASK = 1,
    #: Writes a value to the specified port number. This allows writing a value when the port is in
    #: input mode so that when the port is switched to output mode, the state of the bits is known.
    PORT_INITIAL_OUTPUT_VAL = 2,
    #: Returns or writes the low-pass filter setting. A 0 indicates that the filter is disabled for the
    #: corresponding bit.
    PORT_ISO_FILTER_MASK = 3,
    #: Returns the port logic. A 0 indicates non-invert mode, and a non-zero value indicates output inverted.
    PORT_LOGIC = 4,


class DaqIInfoItem (IntEnum):
    """Use with ulDaqIGetInfo() to obtain DAQ input subsystem information."""
    CHAN_TYPES = 1,  #: A bitmask of supported :func:'~ul_daq.DaqInChanType' values.
    SCAN_OPTIONS = 2,  #: A bit mask of supported :func:'~ul_daq.ScanOption' values.
    TRIG_TYPES = 3,  #: A bitmask of supported :func:'~ul_daq.TriggerType' values.
    FIFO_SIZE = 4,  #: FIFO size in bytes.


class DaqIInfoItemDbl (IntEnum):
    """Use with ulDaqIGetInfoDbl() to obtain information about the counter subsystem."""
    MIN_SCAN_RATE = 1000,  #: The minimum scan rate in samples per second.
    MAX_SCAN_RATE = 1001,  #: The maximum scan rate of the specified device.
    MAX_THROUGHPUT = 1002,  #: The maximum throughput of the specified device.


class AoConfigItem(IntEnum):
    SYNC_MODE = 1,  #: The sync mode. Set with AOutSyncMode.
    CHAN_SENSE_MODE = 2,  #: The channel sense mode.  Set with AOutSenseMode.


class AoInfoItem (IntEnum):
    """Use with ulAOGetInfo() to obtain information about the analog output subsystem."""
    RESOLUTION = 1,  #: The D/A resolution.
    NUM_CHANS = 2,  #: The number of D/A channels on the specified device.
    SCAN_OPTIONS = 3,  #: A bit mask of supported :func:'~ul_daq.ScanOption; values.
    HAS_PACER = 4,  #: Paced operations are supported.
    NUM_RANGES = 5,  #: The number of supported :func:'~ul_daq.Range' values for D/A operations.
    RANGE = 6,  #: The :func:'~ul_daq.Range' for the specified range index.
    TRIG_TYPES = 7,  #: A bitmask of supported :func:'~ul_daq.TriggerType' values.
    FIFO_SIZE = 8,  #: FIFO size in bytes.


class AoInfoItemDbl (IntEnum):
    """Use with ulAOGetInfoDbl() to obtain information about the Analog output subsystem."""
    MIN_SCAN_RATE = 1000,  #: The minimum scan rate of the specified device.
    MAX_SCAN_RATE = 1001,  #: The maximum scan rate of the specified device.
    MAX_THROUGHPUT = 1002,  #: The maximum scanning throughput of the specified device.


class DaqoInfoItem (IntEnum):
    """Use with ulDaqOGetInfo() to obtain information about the DAQ output subsystem."""
    CHAN_TYPES = 1,  #: A bit mask of supported :class:`DaqOutChanType` values.
    SCAN_OPTIONS = 2,  #: A bit mask of supported :class:`ScanOption` values.
    TRIG_TYPES = 3,  #: A bit mask of supported :class:`TriggerType` values.
    FIFO_SIZE = 4,  #: FIFO size in bytes.


class DaqoInfoItemDbl (IntEnum):
    """Use with ulDaqOGetInfoDbl() to obtain information about the DAQ output subsystem."""
    MIN_SCAN_RATE = 1000,  #: The minimum scan rate in samples per second.
    MAX_SCAN_RATE = 1001,  #: The maximum scan rate of the specified device.
    MAX_THROUGHPUT = 1002,  #: The maximum throughput of the specified device.


class CtrInfoItem (IntEnum):
    """Use with ulCtrGetInfo() to obtain information about the counter subsystem."""
    NUM_CTRS = 1,  #: The number of counter channels on the specified device.
    MEASUREMENT_TYPES = 2,  #: A bit mask of supported :class:`CounterMeasurementType` values.
    MEASUREMENT_MODES = 3,  #: A bit mask of supported :class:`CounterMeasurementType` values.
    REGISTER_TYPES = 4,  #: A bit mask of supported :class:`CounterRegisterType` values.
    RESOLUTION = 5,  #: The resolution of the specified counter channel.
    HAS_PACER = 6,  #: Paced operations are supported.
    SCAN_OPTIONS = 7,  #: A bit mask of supported :class:`ScanOption` values.
    TRIG_TYPES = 8,  #: A bit mask of supported :class:`TriggerType` values.
    FIFO_SIZE = 9,  #: FIFO size in bytes.


class CtrInfoItemDbl (IntEnum):
    """Use with ulCtrGetInfoDbl() to obtain information about the counter subsystem."""
    MIN_SCAN_RATE = 1000,  #: The minimum scan rate in samples per second.
    MAX_SCAN_RATE = 1001,  #: The maximum scan rate of the specified device.
    MAX_THROUGHPUT = 1002,  #: The maximum throughput of the specified device.


class CtrConfigItem (IntEnum):
    """Use with ulCtrSetConfig() and ulCtrGetConfig() to configure the Ctr subsystem."""
    REG = 1,  #: The counter(s) configuration register.


class TmrInfoItem (IntEnum):
    """Use with ulTmrGetInfo() to obtain information about the timer subsystem."""
    NUM_TMRS = 1,  #: The :class:`TimerType` of the specified timer index.
    TYPE = 2,  #: The number of bits on the port specified by the port index.


class TmrInfoItemDbl (IntEnum):
    """Use with ulTmrGetInfoDbl() to obtain information about the timer subsystem."""
    MIN_FREQ = 1000,  #: The minimum frequency of the specified device.
    MAX_FREQ = 1001,  #: The maximum frequency of the specified device.


# Prototypes for callbacks


InterfaceCallbackProcType = CFUNCTYPE(None, c_longlong, c_uint, c_ulonglong, POINTER(EventParams))


def interface_event_callback_function(handle, event_type, event_data, event_params):
    # type: (int, DaqEventType, py_object, py_object) -> None
    """Internal function used for handling event callbacks."""

    event_parameters = cast(event_params, POINTER(EventParams)).contents
    user_data = event_parameters.user_data

    cb = event_parameters.user_callback
    cb(EventCallbackArgs(event_type, event_data, user_data))

    return


# Prototypes for DAQ Device
lib.ulDevGetConfigStr.argtypes = (c_longlong, c_uint, c_uint, POINTER(c_char), POINTER(c_uint))
lib.ulDevGetConfig.argtypes = (c_longlong, c_uint, c_uint, POINTER(c_longlong))
lib.ulGetDaqDeviceDescriptor.argtypes = (c_longlong, POINTER(DaqDeviceDescriptor))
lib.ulDevGetInfo.argtypes = (c_longlong, c_uint, c_uint, POINTER(c_longlong))
lib.ulGetDaqDeviceInventory.argtypes = (c_uint, POINTER(DaqDeviceDescriptor), POINTER(c_uint))
lib.ulConnectDaqDevice.argtypes = (c_longlong,)
lib.ulEnableEvent.argtypes = (c_longlong, c_uint, c_ulonglong, InterfaceCallbackProcType, POINTER(EventParams))
lib.ulDisableEvent.argtypes = (c_longlong, c_uint)
lib.ulMemRead.argtypes = (c_longlong, c_uint, c_uint, POINTER(c_byte), c_uint)
lib.ulMemWrite.argtypes = (c_longlong, c_uint, c_uint, POINTER(c_byte), c_uint)
lib.ulCreateDaqDevice.argtypes = (DaqDeviceDescriptor,)
lib.ulReleaseDaqDevice.argtypes = (c_longlong,)
lib.ulIsDaqDeviceConnected.argtypes = (c_longlong, POINTER(c_int))
lib.ulDisconnectDaqDevice.argtypes = (c_longlong,)
lib.ulFlashLed.argtypes = (c_longlong, c_int)
lib.ulGetInfoStr.argtypes = (c_uint, c_uint, POINTER(c_char), POINTER(c_uint))
lib.ulSetConfig.argtypes = (c_uint, c_uint, c_longlong)
lib.ulGetConfig.argtypes = (c_uint, c_uint, POINTER(c_longlong))
lib.ulGetNetDaqDeviceDescriptor.argtypes = (c_char_p, c_uint, c_char_p,
                                            POINTER(DaqDeviceDescriptor),
                                            c_double)
lib.ulDaqDeviceConnectionCode.argtypes = (c_longlong, c_longlong)
# Prototypes for the analog input subsystem
lib.ulAIn.argtypes = (c_longlong, c_int, c_uint, c_uint, c_uint, POINTER(c_double))
lib.ulAInScan.argtypes = (c_longlong, c_int, c_int, c_uint, c_uint, c_int, POINTER(c_double), c_uint, c_uint,
                          POINTER(c_double))
lib.ulAInScanWait.argtypes = (c_longlong, c_uint, c_longlong, c_double)
lib.ulAInLoadQueue.argtypes = (c_longlong, POINTER(AiQueueElement), c_uint)
lib.ulAInSetTrigger.argtypes = (c_longlong, c_uint, c_int, c_double, c_double, c_uint)
lib.ulAInScanStatus.argtypes = (c_longlong, POINTER(c_uint), POINTER(TransferStatus))
lib.ulAISetConfig.argtypes = (c_longlong, c_uint, c_uint, c_longlong)
lib.ulAIGetConfig.argtypes = (c_longlong, c_uint, c_uint, POINTER(c_longlong))
lib.ulAISetConfigDbl.argtypes = (c_longlong, c_uint, c_uint, c_double)
lib.ulAIGetConfigDbl.argtypes = (c_longlong, c_uint, c_uint, POINTER(c_double))
lib.ulAIGetInfo.argtypes = (c_longlong, c_uint, c_uint, POINTER(c_longlong))
lib.ulAIGetInfoDbl.argtypes = (c_longlong, c_uint, c_uint, POINTER(c_double))
lib.ulAInScanStop.argtypes = (c_longlong,)
lib.ulAIGetConfigStr.argtypes = (c_longlong, c_uint, c_uint, POINTER(c_char), POINTER(c_uint))
lib.ulTIn.argtypes = (c_longlong, c_int, c_uint, c_uint, POINTER(c_double))
lib.ulTInArray.argtypes = (c_longlong, c_int, c_int, c_uint, c_uint,
                           POINTER(c_double))
# Prototypes for the analog output subsystem
lib.ulAOut.argtypes = (c_longlong, c_int, c_uint, c_uint, c_double)
lib.ulAOutScan.argtypes = (c_longlong, c_int, c_int, c_uint, c_int, POINTER(c_double), c_uint, c_uint,
                           POINTER(c_double))
lib.ulAOutScanWait.argtypes = (c_longlong, c_uint, c_longlong, c_double)
lib.ulAOutScanStatus.argtypes = (c_longlong, POINTER(c_uint), POINTER(TransferStatus))
lib.ulAOutScanStop.argtypes = (c_longlong,)
lib.ulAOutSetTrigger.argtypes = (c_longlong, c_uint, c_int, c_double, c_double, c_uint)
lib.ulAOGetInfo.argtypes = (c_longlong, c_uint, c_uint, POINTER(c_longlong))
lib.ulAOGetInfoDbl.argtypes = (c_longlong, c_uint, c_uint, POINTER(c_double))
lib.ulAOutArray.argtypes = (c_longlong, c_int, c_int, POINTER(c_uint), c_uint,
                            POINTER(c_double))
# Prototypes for the DAQ input subsystem
lib.ulDaqInSetTrigger.argtypes = (c_longlong, c_uint, DaqInChanDescriptor, c_double, c_double, c_uint)
lib.ulDaqInScan.argtypes = (c_longlong, POINTER(DaqInChanDescriptor), c_int, c_int, POINTER(c_double), c_uint, c_uint,
                            POINTER(c_double))
lib.ulDaqInScanStatus.argtypes = (c_longlong, POINTER(c_uint), POINTER(TransferStatus))
lib.ulDaqInScanStop.argtypes = (c_longlong,)
lib.ulDaqInScanWait.argtypes = (c_longlong, c_uint, c_longlong, c_double)
lib.ulDaqIGetInfo.argtypes = (c_longlong, c_uint, c_uint, POINTER(c_longlong))
lib.ulDaqIGetInfoDbl.argtypes = (c_longlong, c_uint, c_uint, POINTER(c_double))
# Prototypes for DIO subsystem
lib.ulDIn.argtypes = (c_longlong, c_uint, POINTER(c_ulonglong))
lib.ulDOut.argtypes = (c_longlong, c_uint, c_ulonglong)
lib.ulDBitIn.argtypes = (c_longlong, c_uint, c_int, POINTER(c_uint))
lib.ulDBitOut.argtypes = (c_longlong, c_uint, c_int, c_uint)
lib.ulDInScan.argtypes = (c_longlong, c_uint, c_uint, c_int, POINTER(c_double), c_uint, c_uint, POINTER(c_ulonglong))
lib.ulDOutScan.argtypes = (c_longlong, c_uint, c_uint, c_int, POINTER(c_double), c_uint, c_uint, POINTER(c_ulonglong))
lib.ulDInScanStatus.argtypes = (c_longlong, POINTER(c_uint), POINTER(TransferStatus))
lib.ulDOutScanStatus.argtypes = (c_longlong, POINTER(c_uint), POINTER(TransferStatus))
lib.ulDOutScanStop.argtypes = (c_longlong,)
lib.ulDInScanStop.argtypes = (c_longlong,)
lib.ulDInScanWait.argtypes = (c_longlong, c_uint, c_longlong, c_double)
lib.ulDOutScanWait.argtypes = (c_longlong, c_uint, c_longlong, c_double)
lib.ulDInSetTrigger.argtypes = (c_longlong, c_uint, c_int, c_double, c_double, c_uint)
lib.ulDOutSetTrigger.argtypes = (c_longlong, c_uint, c_int, c_double, c_double, c_uint)
lib.ulDConfigPort.argtypes = (c_longlong, c_uint, c_uint)
lib.ulDConfigBit.argtypes = (c_longlong, c_uint, c_int, c_uint)
lib.ulDIOGetInfo.argtypes = (c_longlong, c_uint, c_uint, POINTER(c_longlong))
lib.ulDIOGetInfoDbl.argtypes = (c_longlong, c_uint, c_uint, POINTER(c_double))
lib.ulDIOGetConfig.argtypes = (c_longlong, c_uint, c_uint, POINTER(c_longlong))
lib.ulDIOSetConfig.argtypes = (c_longlong, c_uint, c_uint, c_longlong)
lib.ulDInArray.argtypes = (c_longlong, c_uint, c_uint, POINTER(c_ulonglong))
lib.ulDOutArray.argtypes = (c_longlong, c_uint, c_uint, POINTER(c_ulonglong))
# prototypes for DAQ output subsystem
lib.ulDaqOutScan.argtypes = (c_longlong, POINTER(DaqOutChanDescriptor), c_int, c_int, POINTER(c_double), c_uint,
                             c_uint, POINTER(c_double))
lib.ulDaqOutScanWait.argtypes = (c_longlong, c_uint, c_longlong, c_double)
lib.ulDaqOutScanStatus.argtypes = (c_longlong, POINTER(c_uint), POINTER(TransferStatus))
lib.ulDaqOutScanStop.argtypes = (c_longlong,)
lib.ulDaqOutSetTrigger.argtypes = (c_longlong, c_uint, DaqInChanDescriptor, c_double, c_double, c_uint)
lib.ulDaqOGetInfo.argtypes = (c_longlong, c_uint, c_uint, POINTER(c_longlong))
lib.ulDaqOGetInfoDbl.argtypes = (c_longlong, c_uint, c_uint, POINTER(c_double))
# prototypes for counter subsystem
lib.ulCIn.argtypes = (c_longlong, c_int, POINTER(c_ulonglong))
lib.ulCRead.argtypes = (c_longlong, c_int, c_uint, POINTER(c_ulonglong))
lib.ulCLoad.argtypes = (c_longlong, c_int, c_uint, c_ulonglong)
lib.ulCClear.argtypes = (c_longlong, c_int)
lib.ulCConfigScan.argtypes = (c_longlong, c_int, c_uint, c_uint, c_uint, c_uint, c_uint, c_uint, c_uint)
lib.ulCInScan.argtypes = (c_longlong, c_int, c_int, c_int, POINTER(c_double), c_uint, c_uint, POINTER(c_ulonglong))
lib.ulCInSetTrigger.argtypes = (c_longlong, c_uint, c_int, c_double, c_double, c_uint)
lib.ulCInScanStatus.argtypes = (c_longlong, POINTER(c_uint), POINTER(TransferStatus))
lib.ulCInScanStop.argtypes = (c_longlong,)
lib.ulCInScanWait.argtypes = (c_longlong, c_uint, c_longlong, c_double)
lib.ulCtrGetInfo.argtypes = (c_longlong, c_uint, c_uint, POINTER(c_longlong))
lib.ulCtrGetInfoDbl.argtypes = (c_longlong, c_uint, c_uint, POINTER(c_double))
lib.ulCtrSetConfig.argtypes = (c_longlong, c_uint, c_uint, c_longlong)
lib.ulCtrGetConfig.argtypes = (c_longlong, c_uint, c_uint, POINTER(c_longlong))
# Prototypes for the timer subsystem
lib.ulTmrPulseOutStart.argtypes = (c_longlong, c_int, POINTER(c_double), POINTER(c_double), c_ulonglong,
                                   POINTER(c_double), c_uint, c_uint)
lib.ulTmrPulseOutStop.argtypes = (c_longlong, c_int)
lib.ulTmrPulseOutStatus.argtypes = (c_longlong, c_int, POINTER(c_uint))
lib.ulTmrSetTrigger.argtypes = (c_longlong, c_uint, c_int, c_double, c_double, c_uint)
lib.ulTmrGetInfo.argtypes = (c_longlong, c_uint, c_uint, POINTER(c_longlong))
lib.ulTmrGetInfoDbl.argtypes = (c_longlong, c_uint, c_uint, POINTER(c_double))
# Other Prototypes
lib.ulGetErrMsg.argtypes = (c_uint, POINTER(c_char))
lib.ulDevGetInfo.argtypes = (c_longlong, c_uint, c_uint, POINTER(c_longlong))
lib.ulMemGetInfo.argtypes = (c_longlong, c_uint, POINTER(MemDescriptor))

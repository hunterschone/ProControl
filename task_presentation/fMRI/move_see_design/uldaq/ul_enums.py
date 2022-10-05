"""
Created on Mar 29 2018

@author: MCC
"""
from enum import IntEnum


class ULError(IntEnum):
    """Error codes for Universal Library."""
    NO_ERROR = 0,  #: No error has occurred
    UNHANDLED_EXCEPTION = 1,  #: Unhandled internal exception
    BAD_DEV_HANDLE = 2,  #: Invalid device handle
    BAD_DEV_TYPE = 3,  #: This function cannot be used with this device
    USB_DEV_NO_PERMISSION = 4,  #: Insufficient permission to access this device
    USB_INTERFACE_CLAIMED = 5,  #: USB interface is already claimed
    DEV_NOT_FOUND = 6,  #: Device not found
    DEV_NOT_CONNECTED = 7,  #: Device not connected or connection lost
    DEAD_DEV = 8,  #: Device no longer responding
    BAD_BUFFER_SIZE = 9,  #: Buffer too small for operation
    BAD_BUFFER = 10,  #: Invalid buffer
    BAD_MEM_TYPE = 11,  #: Invalid memory type
    BAD_MEM_REGION = 12,  #: Invalid memory region
    BAD_RANGE = 13,  #: Invalid range
    BAD_AI_CHAN = 14,  #: Invalid analog input channel specified
    BAD_INPUT_MODE = 15,  #: Invalid input mode specified
    ALREADY_ACTIVE = 16,  #: A background process is already in progress
    BAD_TRIG_TYPE = 17,  #: Invalid trigger type specified
    OVERRUN = 18,  #: FIFO overrun, data was not transferred from device fast enough
    UNDERRUN = 19,  #: FIFO underrun, data was not transferred to device fast enough
    TIMEDOUT = 20,  #: Operation timed out
    BAD_OPTION = 21,  #: Invalid option specified
    BAD_RATE = 22,  #: Invalid sampling rate specified
    BAD_BURSTIO_COUNT = 23,  #: Sample count cannot be greater than FIFO size for BURSTIO scans
    CONFIG_NOT_SUPPORTED = 24,  #: Configuration not supported
    BAD_CONFIG_VAL = 25,  #: Invalid configuration value
    BAD_AI_CHAN_TYPE = 26,  #: Invalid analog input channel type specified
    ADC_OVERRUN = 27,  #: ADC overrun occurred
    BAD_TC_TYPE = 28,  #: Invalid thermocouple type specified
    BAD_UNIT = 29,  #: Invalid unit specified
    BAD_QUEUE_SIZE = 30,  #: Invalid queue size
    BAD_CONFIG_ITEM = 31,  #: Invalid config item specified
    BAD_INFO_ITEM = 32,  #: Invalid info item specified
    BAD_FLAG = 33,  #: Invalid flag specified
    BAD_SAMPLE_COUNT = 34,  #: Invalid sample count specified
    INTERNAL = 35,  #: Internal error
    BAD_COUPLING_MODE = 36,  #: Invalid coupling mode
    BAD_SENSOR_SENSITIVITY = 37,  #: Invalid sensor sensitivity
    BAD_IEPE_MODE = 38,  #: Invalid IEPE mode
    BAD_AI_CHAN_QUEUE = 39,  #: Invalid channel queue specified
    BAD_AI_GAIN_QUEUE = 40,  #: Invalid gain queue specified
    BAD_AI_MODE_QUEUE = 41,  #: Invalid mode queue specified
    FPGA_FILE_NOT_FOUND = 42,  #: FPGA file not found
    UNABLE_TO_READ_FPGA_FILE = 43,  #: Unable to read FPGA file
    NO_FPGA = 44,  #: FPGA not loaded
    BAD_ARG = 45,  #: Invalid argument
    MIN_SLOPE_VAL_REACHED = 46,  #: Minimum slope value reached
    MAX_SLOPE_VAL_REACHED = 47,  #: Maximum slope value reached
    MIN_OFFSET_VAL_REACHED = 48,  #: Minimum offset value reached
    MAX_OFFSET_VAL_REACHED = 49,  #: Maximum offset value reached
    BAD_PORT_TYPE = 50,  #: Invalid port type specified
    WRONG_DIG_CONFIG = 51,  #: Digital I/O is configured incorrectly
    BAD_BIT_NUM = 52,  #: Invalid bit number
    BAD_PORT_VAL = 53,  #: Invalid port value specified
    BAD_RETRIG_COUNT = 54,  #: Invalid re-trigger count
    BAD_AO_CHAN = 55,  #: Invalid analog output channel specified
    BAD_DA_VAL = 56,  #: Invalid D/A output value specified
    BAD_TMR = 57,  #: Invalid timer specified
    BAD_FREQUENCY = 58,  #: Invalid frequency specified
    BAD_DUTY_CYCLE = 59,  #: Invalid duty cycle specified
    BAD_INITIAL_DELAY = 60,  #: Invalid initial delay specified
    BAD_CTR = 61,  #: Invalid counter specified
    BAD_CTR_VAL = 62,  #: Invalid counter value specified
    BAD_DAQI_CHAN_TYPE = 63,  #: Invalid DAQ input channel type specified
    BAD_NUM_CHANS = 64,  #: Invalid number of channels specified
    BAD_CTR_REG = 65,  #: Invalid counter register specified
    BAD_CTR_MEASURE_TYPE = 66,  #: Invalid counter measurement type specified
    BAD_CTR_MEASURE_MODE = 67,  #: Invalid counter measurement mode specified
    BAD_DEBOUNCE_TIME = 68,  #: Invalid debounce time specified
    BAD_DEBOUNCE_MODE = 69,  #: Invalid debounce mode specified
    BAD_EDGE_DETECTION = 70,  #: Invalid edge detection mode specified
    BAD_TICK_SIZE = 71,  #: Invalid tick size specified
    BAD_DAQO_CHAN_TYPE = 72,  #: Invalid DAQ output channel type specified
    NO_CONNECTION_ESTABLISHED = 73,  #: No connection established
    BAD_EVENT_TYPE = 74,  #: Invalid event type specified
    EVENT_ALREADY_ENABLED = 75,  #: An event handler has already been enabled for this event type
    BAD_EVENT_SIZE = 76,  #: Invalid event count specified
    BAD_CALLBACK_FUCNTION = 77,  #: Invalid callback function specified
    BAD_MEM_ADDRESS = 78,  #: Invalid memory address
    MEM_ACCESS_DENIED = 79,  #: Memory access denied
    DEV_UNAVAILABLE = 80,  #: Device is not available at time of request
    BAD_RETRIG_TRIG_TYPE = 81,  #: Re-trigger option is not supported for the specified trigger type
    BAD_DEV_VER = 82,  #: This function cannot be used with this version of the device
    BAD_DIG_OPERATION = 83,  #: This digital operation is not supported on the specified port
    BAD_PORT_INDEX = 84,  #: Invalid digital port index specified
    OPEN_CONNECTION = 85,  #: Temperature input has open connection
    DEV_NOT_READY = 86,  #: Device is not ready to send data
    PACER_OVERRUN = 87,  #: Pacer overrun, external clock rate too fast
    BAD_TRIG_CHANNEL = 88,  #: Invalid trigger channel specified
    BAD_TRIG_LEVEL = 89,  #: Invalid trigger level specified
    BAD_CHAN_ORDER = 90,  #: Invalid channel order
    TEMP_OUT_OF_RANGE = 91,  #: Temperature input is out of range
    TRIG_THRESHOLD_OUT_OF_RANGE = 92,  #: Trigger threshold is out of range
    INCOMPATIBLE_FIRMWARE = 93,  #: Incompatible firmware version, firmware update required
    BAD_NET_IFC = 94,  #: Specified network interface is not available or disconnected
    BAD_NET_HOST = 95,  #: Invalid host specified
    BAD_NET_PORT = 96,  #: Invalid port specified
    NET_IFC_UNAVAILABLE = 97,  #: Network interface used to obtain the device descriptor not available or disconnected
    NET_CONNECTION_FAILED = 98,  #: Network connection failed
    BAD_CONNECTION_CODE = 99,  #: Invalid connection code
    CONNECTION_CODE_IGNORED = 100,  #: Connection code ignored
    NET_DEV_IN_USE = 101,  #: Network device already in use
    BAD_NET_FRAME = 102,  #: Invalid network frame
    NET_TIMEOUT = 103,  #: Network device did not respond within expected time
    DATA_SOCKET_CONNECTION_FAILED = 104,  #: Data socket connection failed
    PORT_USED_FOR_ALARM = 105,  #: One or more bits on the specified port are used for alarm
    BIT_USED_FOR_ALARM = 106,  #: The specified bit is used for alarm
    CMR_EXCEEDED = 107,  #: Common - mode voltage range exceeded
    NET_BUFFER_OVERRUN = 108,  #: Network buffer overrun, data was not transferred from buffer fast enough
    BAD_NET_BUFFER = 109,  #: Invalid network buffer
    BAD_DESCRIPTOR = 100001,  #: Invalid descriptor


class InterfaceType(IntEnum):
    """
    Contains attributes suitable for bit-wise operations indicating the physical
    connection interface used to communicate with a DAQ device. Values can be
    OR'd together to specify multiple interfaces.
    """
    USB = 1 << 0  #: USB interface
    BLUETOOTH = 1 << 1  #: Bluetooth interface
    ETHERNET = 1 << 2  #: Ethernet interface
    ANY = USB | BLUETOOTH | ETHERNET  #: Any interface


class DaqEventType(IntEnum):
    """
    Contains attributes suitable for bit-wise operations indicating the types
    of conditions that trigger an event. Used as the event_type argument value
    for :func:`~DaqDevice.enable_event` and :func:`~DaqDevice.disable_event`.
    Values can be OR'd together to enable or disable multiple events.
    Returned as a bit-wise operable list using
    :class:`~DaqDeviceInfo.get_event_types`.
    """
    #: No event type. Possible return value for get_info(). Not a valid value for
    #: :func:`~DaqDevice.enable_event` and :func:`~DaqDevice.disable_event`.
    NONE = 0,
    #: Defines an event trigger condition that occurs
    #: when a specified number of samples are available.
    ON_DATA_AVAILABLE = 1 << 0,
    #: Defines an event trigger condition that occurs
    #: when an input scan error occurs.
    ON_INPUT_SCAN_ERROR = 1 << 1,
    #: Defines an event trigger condition that occurs
    #: upon completion of an input scan operation such as :func:`~AiDevice.a_in_scan`.
    ON_END_OF_INPUT_SCAN = 1 << 2,
    #: Defines an event trigger condition that occurs
    #: when an output scan error occurs.
    ON_OUTPUT_SCAN_ERROR = 1 << 3,
    #: Defines an event trigger condition that occurs
    #: upon completion of an output scan operation such as :func:`~AoDevice.a_out_scan`.
    ON_END_OF_OUTPUT_SCAN = 1 << 4,


class WaitType(IntEnum):
    """
    Used with the subsystem scan_wait functions as the wait_type argument
    value for the specified device.
    """
    #: Function returns when the scan operation completes or the time specified by the timeout argument value elapses.
    WAIT_UNTIL_DONE = 1 << 0,


class DevVersionType(IntEnum):
    """
    Use as the version_type argument for :func:`~DaqDeviceConfig.get_version`
    for the specified device.
    """
    #: Firmware version installed on the current device.
    FW_MAIN = 0,
    #: FPGA version installed on the current device.
    FPGA = 1,
    #: Radio firmware version installed on the current device.
    RADIO = 2,
    #: Measurement firmware version installed on the current device.
    FW_MEASUREMENT = 3,
    #: Measurement firmware version installed on the expansion board attached
    #: to the current device.
    FW_MEASUREMENT_EXP = 4,


class MemAccessType(IntEnum):
    """
    Contains attributes suitable for bit-wise operations indicating the
    level of user access to various memory locations on the device.
    Returned by :class:`~DaqDevice.get_info` as the field types attribute list
    returned in the :class:`MemDescriptor` object.
    """
    #: Indicates read access for the location specified by MemRegion()
    READ = 1 << 0,
    #: Indicates write access for the location specified by MemRegion()
    WRITE = 1 << 1,


class MemRegion(IntEnum):
    """
    Contains attributes suitable for bit-wise operations indicating the
    type of memory region on a device. Returned as a list by
    :class:`~DaqDevice.get_info`.
    Use with :class:`~DevMemInfo.get_mem_descriptor` as the mem_region argument
    to specify the memory location on the specified device.
    """
    #: Specifies the calibration data region information returned to the
    #: MemDescriptor struct.
    CAL = 1 << 0,
    #: Specifies the user data region information returned to the
    #: MemDescriptor struct.
    USER = 1 << 1,
    #: Specifies the data settings region information returned to the
    #: MemDescriptor struct.
    SETTINGS = 1 << 2,
    #: Specifies the first reserved region information returned to the
    #: :class:`MemDescriptor`
    RESERVED0 = 1 << 3,


class AiInputMode(IntEnum):
    """
    Contains attributes indicating A/D channel input modes. Used with most
    analog input methods and with many of the :class:`~AiDevice.get_info`
    methods.
    """
    DIFFERENTIAL = 1,  #: Differential
    SINGLE_ENDED = 2,  #: Single-ended
    PSEUDO_DIFFERENTIAL = 3,  #: Pseudo-differential


class AiChanType(IntEnum):
    """
    Contains attributes suitable for bit-wise operations describing channel
    types. Returned by :class:`~AiInfo.get_chan_types`.
    """
    #: Voltage
    VOLTAGE = 1 << 0,
    #: Thermocouple
    TC = 1 << 1,
    #: Resistance Temperature Detector (RTD)
    RTD = 1 << 2,
    #: Thermistor
    THERMISTOR = 1 << 3,
    #: Semiconductor
    SEMICONDUCTOR = 1 << 4,
    #: Disabled
    DISABLED = 1 << 30,


class AInFlag(IntEnum):
    """
    Contains attributes indicating conditioning to apply to analog
    input data before it's returned. Use as the flags argument
    value for :func:`~AiDevice.a_in`.
    """
    DEFAULT = 0,  #: Data is returned with scaling and calibration factors applied.
    #: Data is returned in native format, without scaling applied.
    NOSCALEDATA = 1 << 0,
    #: Data is returned without calibration factors applied.
    NOCALIBRATEDATA = 1 << 1,


class AInScanFlag(IntEnum):
    """
    Contains attributes indicating conditioning to apply to analog input data
    before it's returned. Use as the flags argument value for
    :func:`~AiDevice.a_in_scan`.
    """
    #: User data should be in *scaled* format (usually volts).
    #: The data is then written to the device after converting to native device
    #: format and calibration factors (if any) applied.
    DEFAULT = 0,
    #: Data is returned in native format, without scaling applied.
    NOSCALEDATA = 1 << 0,
    #: Data is returned without calibration factors applied.
    NOCALIBRATEDATA = 1 << 1,


class Range(IntEnum):
    """Used with many analog input and output functions, as well as a
    return value for get_ranges()."""
    BIP60VOLTS = 1,  #: -60 to +60 Volts
    BIP30VOLTS = 2,  #: -30 to +30 Volts
    BIP15VOLTS = 3,  #: -15 to +15 Volts
    BIP20VOLTS = 4,  #: -20 to +20 Volts
    BIP10VOLTS = 5,  #: -10 to +10 Volts
    BIP5VOLTS = 6,  #: -5 to +5 Volts
    BIP4VOLTS = 7,  #: -4 to +4 Volts
    BIP2PT5VOLTS = 8,  #: -2.5 to +2.5 Volts
    BIP2VOLTS = 9,  #: -2.0 to +2.0 Volts
    BIP1PT25VOLTS = 10,  #: -1.25 to +1.25 Volts
    BIP1VOLTS = 11,  #: -1 to +1 Volts
    BIPPT625VOLTS = 12,  #: -.625 to +.625 Volts
    BIPPT5VOLTS = 13,  #: -.5 to +.5 Volts
    BIPPT25VOLTS = 14,  #: -0.25 to +0.25 Volts
    BIPPT125VOLTS = 15,  #: -0.125 to +0.125 Volts
    BIPPT2VOLTS = 16,  #: -0.2 to +0.2 Volts
    BIPPT1VOLTS = 17,  #: -.1 to +.1 Volts
    BIPPT078VOLTS = 18,  #: -0.078 to +0.078 Volts
    BIPPT05VOLTS = 19,  #: -.05 to +.05 Volts
    BIPPT01VOLTS = 20,  #: -.01 to +.01 Volts
    BIPPT005VOLTS = 21,  #: -.005 to +.005 Volts
    BIP3VOLTS = 22,  #: -3.0 to +3.0 Volts
    BIPPT312VOLTS = 23,  #: -0.312 to +0.312 Volts
    BIPPT156VOLTS = 24,  #: -0.156 to +0.156 Volts
    UNI60VOLTS = 1001,  #: 0 to +60 Volts
    UNI30VOLTS = 1002,  #: 0 to +30 Volts
    UNI15VOLTS = 1003,  #: 0 to +15 Volts
    UNI20VOLTS = 1004,  #: 0 to +20 Volts
    UNI10VOLTS = 1005,  #: 0 to +10 Volts
    UNI5VOLTS = 1006,  #: 0 to +5 Volts
    UNI4VOLTS = 1007,  #: 0 to +4 Volts
    UNI2PT5VOLTS = 1008,  #: 0 to +2.5 Volts
    UNI2VOLTS = 1009,  #: 0 to +2.0 Volts
    UNI1PT25VOLTS = 1010,  #: 0 to +1.25 Volts
    UNI1VOLTS = 1011,  #: 0 to +1 Volts
    UNIPT625VOLTS = 1012,  #: 0 to +.625 Volts
    UNIPT5VOLTS = 1013,  #: 0 to +.5 Volts
    UNIPT25VOLTS = 1014,  #: 0 to +0.25 Volts
    UNIPT125VOLTS = 1015,  #: 0 to +0.125 Volts
    UNIPT2VOLTS = 1016,  #: 0 to +0.2 Volts
    UNIPT1VOLTS = 1017,  #: 0 to +.1 Volts
    UNIPT078VOLTS = 1018,  #: 0 to +0.078 Volts
    UNIPT05VOLTS = 1019,  #: 0 to +.05 Volts
    UNIPT01VOLTS = 1020,  #: 0 to +.01 Volts
    UNIPT005VOLTS = 1021,  #: 0 to +.005 Volts
    MA0TO20 = 2000,  #: 0 to 20 Milliamps


class ScanOption(IntEnum):
    """
    Contains attributes suitable for bit-wise operations indicating optional
    scan modes. These values can be OR'd together to specify multiple options.
    Used with many analog input and output scan functions, as well as a return
    value for :class:`AiInfo.get_scan_options`.
    """
    DEFAULTIO = 0,  #: Transfers A/D data based on the board type and sampling speed.
    #: Transfers one packet of data at a time.
    SINGLEIO = 1 << 0,
    #: Transfers A/D data in blocks.
    BLOCKIO = 1 << 1,
    #: Transfers A/D data from the FIFO after the scan completes.
    #: Allows maximum rates for finite scans up to the full
    #: capacity of the FIFO. Not recommended for slow acquisition rates.
    BURSTIO = 1 << 2,
    #: Scans data in an endless loop. The only way to stop the operation is
    #: with the subsystem scan_stop() function.
    CONTINUOUS = 1 << 3,
    #: Data conversions are controlled by an external clock signal.
    EXTCLOCK = 1 << 4,
    #: Sampling begins when a trigger condition is met.
    EXTTRIGGER = 1 << 5,
    #: Re-arms the trigger after a trigger event is performed.
    RETRIGGER = 1 << 6,
    #: Enables burst mode sampling, minimizing the channel skew.
    BURSTMODE = 1 << 7,
    #: Enables or disables the internal pacer output on a DAQ device.
    PACEROUT = 1 << 8,
    #: Data conversions are controlled by an external timebase signal.
    EXTTIMEBASE = 1 << 9,
    #: Enables or disables the internal timebase output on a DAQ device.
    TIMEBASEOUT = 1<< 10,


class ScanStatus(IntEnum):
    """Scan status."""
    IDLE = 0,  #: The scan is idle.
    RUNNING = 1,  #: The scan is running.


class TriggerType(IntEnum):
    """Used as an individual value with subsystem set_trigger() functions as
    the trig_type argument, or as a list of bit-wise operable values returned
    from  get_info() methods.
    """
    #: No trigger type. Valid for subsystem get_info() functions; not a valid value
    #: for subsystem set_trigger functions.
    NONE = 0,
    #: A digital trigger. The trigger condition is met when the trigger input
    #: transitions from a logic low level to a logic high level. This is the
    #: default condition when triggering is enabled. All others require
    #: configuration using the subsystem set_trigger() functions.
    POS_EDGE = 1 << 0,
    #: A digital trigger. The trigger condition is met when the trigger input
    #: transitions from a logic high level to a logic low level.
    NEG_EDGE = 1 << 1,
    #: A digital trigger. The trigger condition is met when the trigger input
    #: is at a logic high level.
    HIGH = 1 << 2,
    #: A digital trigger. The trigger condition is met when the trigger input
    #: is at a logic low level.
    LOW = 1 << 3,
    #: A digital gate. The operation is enabled only when the trigger input
    #: is at a logic high level.
    GATE_HIGH = 1 << 4,
    #: A digital gate. The operation is enabled only when the trigger input
    #: is at a logic low level.
    GATE_LOW = 1 << 5,
    #: An analog trigger. The trigger condition is met when the trigger input
    #: transitions from below the threshold specified by (the level argument
    #: value minus the variance argument value) to above the threshold
    #: specified by the level argument value.
    RISING = 1 << 6,
    #: An analog trigger. The trigger condition is met when the trigger input
    #: transitions from above the threshold specified by (the level argument
    #: value minus the variance argument value) to below the threshold
    #: specified by the level argument value.
    FALLING = 1 << 7,
    #: An analog trigger. The trigger condition is met when the trigger input
    #: is above the threshold specified by the level argument value.
    ABOVE = 1 << 8,
    #: An analog trigger. The trigger condition is met when the trigger input
    #: is below the threshold specified by the level argument value.
    BELOW = 1 << 9,
    #: An analog trigger. The trigger condition is met only when the trigger
    #: input is above the threshold specified by the level argument value.
    GATE_ABOVE = 1 << 10,
    #: An analog trigger. The trigger condition is met only when the trigger
    #: input is below the threshold specified by the level argument value.
    GATE_BELOW = 1 << 11,
    #: Scanning is enabled as long as the external analog trigger is inside
    #: the region defined by the level argument value and the
    #: variance argument value.
    GATE_IN_WINDOW = 1 << 12,
    #: Scanning is enabled as long as the external analog trigger is outside
    #: the region defined by the level argument value and the
    #: variance argument value.
    GATE_OUT_WINDOW = 1 << 13,
    #: A digital pattern trigger. The trigger condition is met when the
    #: digital pattern at the trigger input is equal to the pattern
    #: specified by the level argument value ANDed with bitwise mask
    #: specified by the variance argument value of the
    #: set_trigger function for each subsystem.
    PATTERN_EQ = 1 << 14,
    #: A digital pattern trigger. The trigger condition is met when the
    #: digital pattern at the trigger input is not equal to the pattern
    #: specified by the level argument value ANDed with bitwise mask
    #: specified by the variance argument value of the
    #: set_trigger function for each subsystem.
    PATTERN_NE = 1 << 15,
    #: A digital pattern trigger. The trigger condition is met when the
    #: digital pattern at the trigger input is greater than the pattern
    #: specified by the level argument value ANDed with bitwise mask
    #: specified by the variance argument value of the
    #: set_trigger function for each subsystem. Value is determined by
    #: additive bit weights.
    PATTERN_ABOVE = 1 << 16,
    #: A digital pattern trigger. The trigger condition is met when the
    #: digital pattern at the trigger input is less than the pattern
    #: specified by the level argument value ANDed with bitwise mask
    #: specified by the variance argument value of the
    #: set_trigger function for each subsystem. Value is determined by
    #: additive bit weights.
    PATTERN_BELOW = 1 << 17,


class AdcTimingMode(IntEnum):
    """ADC timing modes."""
    AUTO = 1,  #: The timing mode is set automatically based on TBD
    HIGH_RES = 2,  #: High resolution timing mode
    HIGH_SPEED = 3,  #: High speed timing mode


class AiQueueType(IntEnum):
    """
    Contains attributes describing queue types (the :CLASS:`AiQueueElement`
    attributes that are allowed to change within a list of
    AiQueueElement). Many devices only support a subset of :CLASS:`AiQueueType`.
    """
    #: The AI subsystem supports a channel queue.
    CHAN = 1 << 0,
    #: The AI subsystem supports a gain queue.
    GAIN = 1 << 1,
    #: The AI subsystem supports a mode queue.
    MODE = 1 << 2,


class AiChanQueueLimitation(IntEnum):
    """
    Contains attributes suitable for bit-wise operations indicating device
    queue limitations. Used with :class:`~AiInfo.get_chan_queue_limitations`.
    See also :class:`~AiInfo.get_queue_types` and
    :class:`~AiInfo.get_max_queue_length` to determine queue capabilities
    """
    #: A particular channel number cannot appear more than once in the queue.
    UNIQUE_CHAN = 1 << 0,
    #: Channel numbers must be listed in ascending order within the queue.
    ASCENDING_CHAN = 1 << 1,
    #: Channel numbers must be listed in consecutive order within the queue.
    CONSECUTIVE_CHAN = 1 << 2,


class AiCalTableType(IntEnum):
    """Analog input calibration table types."""
    FACTORY = 1,  #: Factory calibration table
    FIELD = 2,  #: Field calibration table


class AiRejectFreqType(IntEnum):
    """Analog input rejection frequency types."""
    AI_RFT_60HZ = 1,  #: 60 Hz rejection frequency
    AI_RFT_50HZ = 2,  #: 50 Hz rejection frequency


class AutoZeroMode(IntEnum):
    NONE = 1,
    EVERY_SAMPLE = 2,
    ONCE = 3,


class CouplingMode(IntEnum):
    """Coupling modes."""
    DC = 1,  #: DC coupling
    AC = 2,  #: AC coupling


class IepeMode(IntEnum):
    """IEPE modes."""
    DISABLED = 1,  #: IEPE excitation current is disabled
    ENABLED = 2,  #: IEPE excitation current is enabled


class OtdMode(IntEnum):
    """Open Thermocouple detection modes."""
    DISABLED = 1,  #: Open Thermocouple detection mode is disabled.
    ENABLED = 2,  #: Open Thermocouple detection mode is enabled.


class TcType(IntEnum):
    """
    Thermocouple types.
    """
    J = 1,  #: Type J
    K = 2,  #: Type K
    T = 3,  #: Type T
    E = 4,  #: Type E
    R = 5,  #: Type R
    S = 6,  #: Type S
    B = 7,  #: Type B
    N = 8,  #: Type N


class TempUnit(IntEnum):
    """
    Temperature units.
    """
    CELSIUS = 1,  #: Celcius
    FAHRENHEIT = 2,  #: Fahrenheit
    KELVIN = 3,  #: Kelvin


class TempScale(IntEnum):
    """
    Temperature scaling options.
    """
    CELSIUS = 1,  #: Celsius
    FAHRENHEIT = 2,  #: Fahrenheit
    KELVIN = 3,  #: Kelvin
    VOLTS = 4,  #: Volts
    NOSCALE = 5,  #: No scale (Raw)


class DigitalDirection(IntEnum):
    """
    Used with most digital IO methods to specify the direction of programmable
    ports or bits and with  :func:`~DioInfo.get_port_info` as the list returned
    indicating the current direction that each bit in the specified port type is
    configured for.

    """
    INPUT = 1,  #: Input
    OUTPUT = 2,  #: Output


class DigitalPortIoType(IntEnum):
    """
    Contains attributes indicating the fixed direction or direction
    programmability of the specified digital port. Returned by
    :func:`~DioInfo.get_port_info`.
    """
    IN = 1,  #: Fixed input port
    OUT = 2,  #: Fixed output port
    IO = 3,  #: Bidirectional (input or output) port
    BITIO = 4,  #: Bitwise configurable
    NONCONFIG = 5,  #: Bidirectional (input or output) port; configuration is not required.


class DigitalPortType(IntEnum):
    """
    Used with most digital IO methods as the port_type argument to specify the
    port on the device and as a list returned from
    :func:`~DioInfo.get_port_types` indicating the ports available on the
    device.
    """
    AUXPORT = 1,  #: AuxPort
    AUXPORT0 = 1,  #: AuxPort0
    AUXPORT1 = 2,  #: AuxPort1
    AUXPORT2 = 3,  #: AuxPort2
    FIRSTPORTA = 10,  #: FirstPortA
    FIRSTPORTB = 11,  #: FirstPortB
    FIRSTPORTC = 12,  #: FirstPortC
    FIRSTPORTCL = 12,  #: FirstPortC Low
    FIRSTPORTCH = 13,  #: FirstPortC High
    SECONDPORTA = 14,  #: SecondPortA
    SECONDPORTB = 15,  #: SecondPortB
    SECONDPORTCL = 16,  #: SecondPortC Low
    SECONDPORTCH = 17,  #: SecondPortC High
    THIRDPORTA = 18,  #: ThirdPortA
    THIRDPORTB = 19,  #: ThirdPortB
    THIRDPORTCL = 20,  #: ThirdPortC Low
    THIRDPORTCH = 21,  #: ThirdPortC High
    FOURTHPORTA = 22,  #: FourthPortA
    FOURTHPORTB = 23,  #: FourthPortB
    FOURTHPORTCL = 24,  #: FourthPortC Low
    FOURTHPORTCH = 25,  #: FourthPortC High
    FIFTHPORTA = 26,  #: FifthPortA
    FIFTHPORTB = 27,  #: FifthPortB
    FIFTHPORTCL = 28,  #: FifthPortC Low
    FIFTHPORTCH = 29,  #: FifthPortC High
    SIXTHPORTA = 30,  #: SixthPortA
    SIXTHPORTB = 31,  #: SixthPortB
    SIXTHPORTCL = 32,  #: SixthPortC Low
    SIXTHPORTCH = 33,  #: SixthPortC High
    SEVENTHPORTA = 34,  #: SeventhPortA
    SEVENTHPORTB = 35,  #: SeventhPortB
    SEVENTHPORTCL = 36,  #: SeventhPortC Low
    SEVENTHPORTCH = 37,  #: SeventhPortC High
    EIGHTHPORTA = 38,  #: EighthPortA
    EIGHTHPORTB = 39,  #: EighthPortB
    EIGHTHPORTCL = 40,  #: EighthPortC Low
    EIGHTHPORTCH = 41,  #: EighthPortC High


class DInScanFlag(IntEnum):
    """
    The flags argument value for :func:`~DioDevice.d_in_scan`.
    """
    DEFAULT = 0,  #: Placeholder value; standard functionality.


class DOutScanFlag(IntEnum):
    """
    The flags argument value for :func:`~DioDevice.d_out_scan`.
    """
    DEFAULT = 0,  #: Placeholder value; standard functionality.


class DaqInScanFlag(IntEnum):
    """
    Contains attributes indicating conditioning to apply to analog input data
    before it's returned. Use as the flags argument value for
    :class:`~DaqiDevice.daq_in_scan`.
    """
    DEFAULT = 0,  #: Data is returned with scaling and calibration factors applied to analog channel data.
    #: Data for analog channels is returned in native format, without scaling applied.
    NOSCALEDATA = 1 << 0,
    #: Data for analog channels is returned without calibration factors applied.
    NOCALIBRATEDATA = 1 << 1,
    #: Counters are not cleared (set to 0) when a scan starts
    NOCLEAR = 1 << 3,


class DaqInChanType(IntEnum):
    """
    Contains attributes suitable for bit-wise operations indicating channel
    types for the :func:`~DaqiDevice.daq_in_scan` method. Used with synchronous
    input scanning operations as a property in the :class:`DaqInChanDescriptor`
    object, and as the list of bit-wise operable attributes using
    :func:`DaqiDevice.get_info`.
    """
    ANALOG_DIFF = 1 << 0,  #: Analog input channel, differential mode
    ANALOG_SE = 1 << 1,  #: Analog input channel, single-ended mode
    DIGITAL = 1 << 2,  #: Digital channel
    CTR16 = 1 << 3,  #: 16-bit counter channel
    CTR32 = 1 << 4,  #: 32-bit counter channel
    CTR48 = 1 << 5,  #: 48-bit counter channel
    DAC = 1 << 7,  #: Analog output channel


class AOutFlag(IntEnum):
    """
    Contains attributes indicating conditioning to apply to analog output data
    before it is written to the D/A. Use as the flags argument value for
    :func:`~AoDevice.a_out`.
    """
    #: User data should be in *scaled* format (usually volts). The data is then written
    #: to the device after converting to native device format and calibration factors
    #: (if any) applied.
    DEFAULT = 0,
    #: User data should be in native device format (usually integer in the range
    #: 0 to 2\ :sup:`resolution`\ - 1). The data is written to the device without conversion.
    NOSCALEDATA = 1 << 0,
    #: Calibration factors (if any) are not applied to the data before writing.
    NOCALIBRATEDATA = 1 << 1,


class AOutScanFlag(IntEnum):
    """
    Contains attributes indicating the conditioning to apply to analog output
    data before it's written to the D/A. Use as the flags argument value for
    :func:`~AoDevice.a_out_scan`.
    """
    #: User data should be in *scaled* format (usually volts). The data is then written
    #: to the device after converting to native device format and calibration factors
    #: (if any) applied.
    DEFAULT = 0,
    #: User data should be in native device format (usually integer in the range
    #: 0 to 2\ :sup:`resolution`\ - 1). The data is written to the device without conversion.
    NOSCALEDATA = 1 << 0,
    #: Calibration factors (if any) are not applied to the data before writing.
    NOCALIBRATEDATA = 1 << 1,


class DaqOutChanType(IntEnum):
    """
    Contains attributes suitable for bit-wise operations indicating channel
    types for the :func:`~DaqoDevice.daq_out_scan` method. Used with synchronous
    output scanning operations as a property in the
    :class:`DaqOutChanDescriptor` object, and as the list of bit-wise operable
    attributes using :func:`DaqoDevice.get_info`
    """
    #: Analog output channel.
    ANALOG = 1 << 0,
    #: Digital output channel.
    DIGITAL = 1 << 1,


class DaqOutScanFlag(IntEnum):
    """
    Contains attributes indicating conditioning to apply to analog output data
    before it's written to the D/A. Use as the flags argument value for
    :class:`~DaqoDevice.daq_out_scan`.
    """
    #: The data buffer contains scaled data for analog channels, and calibration factors are applied to analog outputs.
    DEFAULT = 0,
    #: Data for analog channels is in native format, without scaling applied.
    NOSCALEDATA = 1 << 0,
    #: Data for analog channels is output without calibration factors applied.
    NOCALIBRATEDATA = 1 << 1,


class CConfigScanFlag(IntEnum):
    """
    Use as the flags argument value for :func:`~CtrDevice.c_in_scan`
    to set the properties of data returned.
    """
    DEFAULT = 0,  #: Placeholder value; standard functionality.


class CInScanFlag(IntEnum):
    """
    Use as the flags argument value for c_in_scan() to set the properties of
    data returned.
    """
    #: Default counter behavior.
    DEFAULT = 0,
    #: Sets up the counter as a 16-bit counter channel.
    CTR16_BIT = 1 << 0,
    #: Sets up the counter as a 32-bit counter channel.
    CTR32_BIT = 1 << 1,
    #: Sets up the counter as a 64-bit counter channel.
    CTR64_BIT = 1 << 2,
    #: Does not clear the counter to 0 at the start of each scan.
    NOCLEAR = 1 << 3,


class CounterDebounceMode(IntEnum):
    """
    Use as the debounce_mode argument for :func:`~CtrDevice.c_config_scan` to
    set the glitch rejection properties of a counter.
    """
    #: Disables the debounce feature.
    NONE = 0,
    #: The counter is incremented only after the counter input is stable for a
    #:  period of a length defined by :class:`CounterDebounceTime`.
    TRIGGER_AFTER_STABLE = 1,
    #: The counter is incremented on the first edge at the counter input, then waits
    #: for a stable period of a length defined by :class:`CounterDebounceTime` before
    #: counting the next edge.
    TRIGGER_BEFORE_STABLE = 2,


class CounterDebounceTime(IntEnum):
    """
    Use as the value for the debounce_time argument for
    :func:`~CtrDevice.c_config_scan` when :class:`CounterDebounceMode` is not
    NONE.
    """
    #: Disables the debounce feature. Valid only when :class:`CounterDebounceMode`
    #: is set to None.
    DEBOUNCE_0ns = 0,
    #: Sets the time period that the counter input must be stable when using
    #: :class:`~CounterDebounceMode.TRIGGER_AFTER_STABLE` or
    #: :class:`~CounterDebounceMode.TRIGGER_BEFORE_STABLE` CounterDebounceModes to 500 ns.
    DEBOUNCE_500ns = 1,
    #: Sets the time period that the counter input must be stable when using
    #: :class:`~CounterDebounceMode.TRIGGER_AFTER_STABLE` or
    #: :class:`~CounterDebounceMode.TRIGGER_BEFORE_STABLE` CounterDebounceModes to 1500 ns.
    DEBOUNCE_1500ns = 2,
    #: Sets the time period that the counter input must be stable when using
    #: :class:`~CounterDebounceMode.TRIGGER_AFTER_STABLE` or
    #: :class:`~CounterDebounceMode.TRIGGER_BEFORE_STABLE` CounterDebounceModes to 3500 ns.
    DEBOUNCE_3500ns = 3,
    #: Sets the time period that the counter input must be stable when using
    #: :class:`~CounterDebounceMode.TRIGGER_AFTER_STABLE` or
    #: :class:`~CounterDebounceMode.TRIGGER_BEFORE_STABLE` CounterDebounceModes to 7500 ns.
    DEBOUNCE_7500ns = 4,
    #: Sets the time period that the counter input must be stable when using
    #: :class:`~CounterDebounceMode.TRIGGER_AFTER_STABLE` or
    #: :class:`~CounterDebounceMode.TRIGGER_BEFORE_STABLE` CounterDebounceModes to 15500 ns.
    DEBOUNCE_15500ns = 5,
    #: Sets the time period that the counter input must be stable when using
    #: :class:`~CounterDebounceMode.TRIGGER_AFTER_STABLE` or
    #: :class:`~CounterDebounceMode.TRIGGER_BEFORE_STABLE` CounterDebounceModes to 31500 ns.
    DEBOUNCE_31500ns = 6,
    #: Sets the time period that the counter input must be stable when using
    #: :class:`~CounterDebounceMode.TRIGGER_AFTER_STABLE` or
    #: :class:`~CounterDebounceMode.TRIGGER_BEFORE_STABLE` CounterDebounceModes to 63500 ns.
    DEBOUNCE_63500ns = 7,
    #: Sets the time period that the counter input must be stable when using
    #: :class:`~CounterDebounceMode.TRIGGER_AFTER_STABLE` or
    #: :class:`~CounterDebounceMode.TRIGGER_BEFORE_STABLE` CounterDebounceModes to 127500 ns.
    DEBOUNCE_127500ns = 8,
    #: Sets the time period that the counter input must be stable when using
    #: :class:`~CounterDebounceMode.TRIGGER_AFTER_STABLE` or
    #: :class:`~CounterDebounceMode.TRIGGER_BEFORE_STABLE` CounterDebounceModes to 100 us.
    DEBOUNCE_100us = 9,
    #: Sets the time period that the counter input must be stable when using
    #: :class:`~CounterDebounceMode.TRIGGER_AFTER_STABLE` or
    #: :class:`~CounterDebounceMode.TRIGGER_BEFORE_STABLE` CounterDebounceModes to 300 us.
    DEBOUNCE_300us = 10,
    #: Sets the time period that the counter input must be stable when using
    #: :class:`~CounterDebounceMode.TRIGGER_AFTER_STABLE` or
    #: :class:`~CounterDebounceMode.TRIGGER_BEFORE_STABLE` CounterDebounceModes to 700 us.
    DEBOUNCE_700us = 11,
    #: Sets the time period that the counter input must be stable when using
    #: :class:`~CounterDebounceMode.TRIGGER_AFTER_STABLE` or
    #: :class:`~CounterDebounceMode.TRIGGER_BEFORE_STABLE` CounterDebounceModes to 1500 us.
    DEBOUNCE_1500us = 12,
    #: Sets the time period that the counter input must be stable when using
    #: :class:`~CounterDebounceMode.TRIGGER_AFTER_STABLE` or
    #: :class:`~CounterDebounceMode.TRIGGER_BEFORE_STABLE` CounterDebounceModes to 3100 us.
    DEBOUNCE_3100us = 13,
    #: Sets the time period that the counter input must be stable when using
    #: :class:`~CounterDebounceMode.TRIGGER_AFTER_STABLE` or
    #: :class:`~CounterDebounceMode.TRIGGER_BEFORE_STABLE` CounterDebounceModes to 6300 us.
    DEBOUNCE_6300us = 14,
    #: Sets the time period that the counter input must be stable when using
    #: :class:`~CounterDebounceMode.TRIGGER_AFTER_STABLE` or
    #: :class:`~CounterDebounceMode.TRIGGER_BEFORE_STABLE` CounterDebounceModes to 12700 us.
    DEBOUNCE_12700us = 15,
    #: Sets the time period that the counter input must be stable when using
    #: :class:`~CounterDebounceMode.TRIGGER_AFTER_STABLE` or
    #: :class:`~CounterDebounceMode.TRIGGER_BEFORE_STABLE` CounterDebounceModes to 25500 us.
    DEBOUNCE_25500us = 16,


class CounterEdgeDetection(IntEnum):
    """
    Use as the value for the edge_detection argument for
    :func:`~CtrDevice.c_config_scan`.
    """
    RISING_EDGE = 1,  #: Rising edge
    FALLING_EDGE = 2,  #: Falling edge


class CounterMeasurementMode(IntEnum):
    """
    Contains attributes suitable for bit-wise operations indicating counter
    operation modes. Compatible values can be OR'd together. Use as the value
    for the measurement_mode argument for :func:`~CtrDevice.c_config_scan`.
    This value should be set consistent with the measurement_type argument
    value.
    """
    #: Configures the counter for default counting modes for the
    #: :class:`~CounterMeasurementType.COUNT` measurement type.
    DEFAULT = 0,
    #: Configures the counter to clear after every read for the
    #: :class:`~CounterMeasurementType.COUNT` measurement type.
    CLEAR_ON_READ = 1 << 0,
    #: Configures the counter to count down for the :class:`~CounterMeasurementType.COUNT`
    #: measurement type.
    COUNT_DOWN = 1 << 1,
    #: Configures the counter to  increment when the gate pin is high, and
    #: decrement when the gate pin is low for the :class:`~CounterMeasurementType.COUNT`
    #: measurement type.
    GATE_CONTROLS_DIR = 1 << 2,
    #: Configures the counter to clear when the gate input is high for the
    #: :class:`~CounterMeasurementType.COUNT` measurement type.
    GATE_CLEARS_CTR = 1 << 3,
    #: Configures the counter to start counting when the gate input goes active
    #: for the :class:`~CounterMeasurementType.COUNT` measurement type. By default, active is on the
    #: rising edge. The gate is re-armed when the counter is loaded and
    #: when :func:`~CtrDevice.c_config_scan` is called.
    GATE_TRIG_SRC = 1 << 4,
    #: Configures the counter output to go high when the counter reaches
    #: the value of output register 0 for the :class:`~CounterMeasurementType.COUNT` measurement type, and go
    #: low when the counter reaches the value of output register 1.
    #: Use :func:`~CtrDevice.c_load` to set or read the value of the output registers.
    OUTPUT_ON = 1 << 5,
    #: Configures the initial state of the counter output pin high for the
    #: :class:`~CounterMeasurementType.COUNT` measurement type.
    OUTPUT_INITIAL_STATE_HIGH = 1 << 6,
    #: Configures the counter to restart when a clear or load operation is
    #: performed, or the count direction changes for the :class:`~CounterMeasurementType.COUNT`
    #: measurement type.
    NO_RECYCLE = 1 << 7,
    #: When counting up, configures the counter to roll over to the min limit
    #: when the max limit is reached for the :class:`~CounterMeasurementType.COUNT` measurement type.
    #: When counting down, configures the counter to roll over to max limit
    #: when the min limit is reached. When counting up with
    #: :class:`~CounterMeasurementMode.NO_RECYCLE` enabled,
    #: the counter freezes whenever the count reaches the value that was loaded
    #: into the max limit register. When counting down with
    #: :class:`~CounterMeasurementMode.NO_RECYCLE` enabled,
    #: the counter freezes whenever the count reaches the value that was loaded
    #: into the min limit register. Counting resumes if the counter is reset
    #: or the direction changes.
    RANGE_LIMIT_ON = 1 << 8,
    #: Enables the counter when the mapped channel or gate pin is high for
    #: the :class:`~CounterMeasurementType.COUNT` measurement type.
    GATING_ON = 1 << 9,
    #: Inverts the polarity of the gate input for the :class:`~CounterMeasurementType.COUNT`
    #: measurement type.
    INVERT_GATE = 1 << 10,
    #: Latches the counter measurement each time 1 complete period is observed
    #: for the :class:`~CounterMeasurementType.PERIOD` measurement type.
    PERIOD_X1 = 0,
    #: Latches the counter measurement each time 10 complete periods are
    #: observed for the :class:`~CounterMeasurementType.PERIOD` measurement type.
    PERIOD_X10 = 1 << 11,
    #: Latches the counter measurement each time 100 complete periods are
    #: observed for the :class:`~CounterMeasurementType.PERIOD` measurement type.
    PERIOD_X100 = 1 << 12,
    #: Latches the counter measurement each time 1000 complete periods are
    #: observed for the :class:`~CounterMeasurementType.PERIOD` measurement type.
    PERIOD_X1000 = 1 << 13,
    #: Inverts the polarity of the gate input for the :class:`~CounterMeasurementType.PERIOD`
    #: measurement type.
    PERIOD_GATING_ON = 1 << 14,
    #: Inverts the polarity of the gate input for the :class:`~CounterMeasurementType.PERIOD`
    #: measurement type.
    PERIOD_INVERT_GATE = 1 << 15,
    #: Configures the counter for default pulse width modes
    # for the :class:`~CounterMeasurementType.PULSE_WIDTH` measurement type.
    PULSE_WIDTH_DEFAULT = 0,
    #: Enables the counter when the mapped channel or gate pin is high
    # for the :class:`~CounterMeasurementType.PULSE_WIDTH` measurement type.
    PULSE_WIDTH_GATING_ON = 1 << 16,
    #: Inverts the polarity of the gate input for the :class:`~CounterMeasurementType.PULSE_WIDTH`
    #: measurement type.
    PULSE_WIDTH_INVERT_GATE = 1 << 17,
    #: Configures the counter for default timing modes
    #: for the :class:`~CounterMeasurementType.TIMING` measurement type.
    TIMING_DEFAULT = 0,
    #: Inverts the polarity of the gate input for the
    #: :class:`~CounterMeasurementType.TIMING` measurement type.
    TIMING_MODE_INVERT_GATE = 1 << 18,
    #: Sets the encoder measurement mode to X1 for the
    #: :class:`~CounterMeasurementType.ENCODER` measurement type.
    ENCODER_X1 = 0,
    #: Sets the encoder measurement mode to X2 for the
    #: :class:`~CounterMeasurementType.ENCODER` measurement type.
    ENCODER_X2 = 1 << 19,
    #: Sets the encoder measurement mode to X4 for the
    #: :class:`~CounterMeasurementType.ENCODER` measurement type.
    ENCODER_X4 = 1 << 20,
    #: Configures the encoder Z mapped signal to latch the counter outputs
    #: for the :class:`~CounterMeasurementType.ENCODER` measurement type.
    ENCODER_LATCH_ON_Z = 1 << 21,
    #: Clears the counter when the index (Z input) goes active
    #: for the :class:`~CounterMeasurementType.ENCODER` measurement type.
    ENCODER_CLEAR_ON_Z = 1 << 22,
    #: Disables the counter when a count overflow or underflow occurs
    #: for the :class:`~CounterMeasurementType.ENCODER` measurement type;
    #: re-enables when a clear or load operation is performed on the counter.
    ENCODER_NO_RECYCLE = 1 << 23,
    #: Enables upper and lower limits for the :class:`~CounterMeasurementType.ENCODER`
    #: measurement type.
    ENCODER_RANGE_LIMIT_ON = 1 << 24,
    #: Sets the encoder Z signal as the active edge for the
    #: :class:`~CounterMeasurementType.ENCODER` measurement type.
    ENCODER_Z_ACTIVE_EDGE = 1 << 25,
    #: Configures the counter to be latched by the signal on the index pin for
    #: the :class:`~CounterMeasurementType.COUNT` measurement type.
    LATCH_ON_INDEX = 1 << 26,
    #: Configures the counter to increment when the phase B pin is high, and
    #: decrement when the phase B pin is low for the
    #: :class:`~CounterMeasurementType.COUNT` measurement type.
    PHB_CONTROLS_DIR = 1 << 27,
    #: Configures the counter to decrement by the signal on the mapped channel
    #: for the :class:`~CounterMeasurementType.COUNT` measurement type.
    DECREMENT_ON = 1 << 28,


class CounterMeasurementType(IntEnum):
    """
    Contains attributes suitable for bit-wise operations indicating counter
    operation modes. Use individually as the value for the measurement_type
    argument for :func:`~CtrDevice.c_config_scan`.
    Use :class:`~CtrDevice.get_info` with :func:`~CtrInfo.get_measurement_types`
    to get a list of bit-wise operable attributes to check device capabilities.
"""
    #: Counter measurement. The counter increments on the active edge
    #: of the input.
    COUNT = 1 << 0,
    #: Period measurement. Measures the number of ticks between
    #: active edges of the input, with the granularity of measurement
    #: set by the tick_size argument of :func:`~CtrDevice.c_config_scan`.
    PERIOD = 1 << 1,
    #: Pulse width measurement. Measures the number of ticks between the
    #: active edge of the counter input and the following edge of the
    #: counter input, with the granularity of measurement
    #: set by the tick_size argument of :func:`~CtrDevice.c_config_scan`.
    PULSE_WIDTH = 1 << 2,
    #: Timing measurement. Measures the number of ticks between the
    #: between the active edge of the counter input and the
    #: active edge of the gate input, with the granularity of measurement
    #: set by the tick_size argument of :func:`~CtrDevice.c_config_scan`.
    TIMING = 1 << 3,
    #: Encoder measurement. Configures the counter as an encoder, if supported.
    ENCODER = 1 << 4,


class CounterRegisterType(IntEnum):
    """
    Contains attributes suitable for bit-wise operations indicating counter
    register types available. Used individually for the
    :class:`~CtrDevice.c_load` register_type argument, and as the value returned
    by to get a list of bit-wise operable attributes using
    :func:`~CtrInfo.get_register_types` to check device capabilities.
    """
    #: Counter register
    COUNT = 1 << 0,
    #: Load register
    LOAD = 1 << 1,
    #: Max Limit register
    MIN_LIMIT = 1 << 2,
    #: Min Limit register
    MAX_LIMIT = 1 << 3,
    #: The register that sets the count value at which the counter output
    #: will change state from its original state.
    OUTPUT_VAL0 = 1 << 4,
    #: The register that sets the count value at which the counter output
    #: will reset to its original state.
    OUTPUT_VAL1 = 1 << 5,


class CounterTickSize(IntEnum):
    """
    Use as the value for the tick_size argument for
    :class:`~CtrDevice.c_config_scan` when :class:`~CounterMeasurementType` is
    set to :class:`~CounterMeasurementType.PERIOD`,
    :class:`~CounterMeasurementType.PULSE_WIDTH`, or
    :class:`~CounterMeasurementType.TIMING`.
    Refer to the device hardware manual to determine which sizes are compatible
    with your device.
    """
    TICK_20PT83ns = 1,  #: Sets the tick size to 20.83 ns
    TICK_208PT3ns = 2,  #: Sets the tick size to 208.3 ns
    TICK_2083PT3ns = 3,  #: Sets the tick size to 2083.3 ns
    TICK_20833PT3ns = 4,  #: Sets the tick size to 20833.3 ns
    TICK_20ns = 11,  #: Sets the tick size to 20 ns
    TICK_200ns = 12,  #: Sets the tick size to 200 ns
    TICK_2000ns = 13,  #: Sets the tick size to 2000 ns
    TICK_20000ns = 14,  #: Sets the tick size to 20000 ns


class TimerType(IntEnum):
    """
    Types of timer channels. Returned by :class:`~TmrInfo.get_timer_type`.
    """
    #: Programmable frequency timer
    STANDARD = 1,
    #: Programmable frequency timer, plus other attributes such as pulse width.
    ADVANCED = 2,


class TmrIdleState(IntEnum):
    """
    Timer idle state. Used as the idle_state argument of
    :class:`~TmrDevice.pulse_out_start`.
    """
    LOW = 1,  #: Idle low
    HIGH = 2,  #: Idle high


class TmrStatus(IntEnum):
    """
    Used with :class:`~TmrDevice.get_pulse_out_status`, as the timer status
    returned for the specified device.
    """
    IDLE = 0,  #: The timer is currently idle.
    RUNNING = 1,  #: The timer is currently running.


class PulseOutOption(IntEnum):
    """
    Used with :class:`~TmrDevice.pulse_out_start` as the options argument value
    to set advanced options for the specified device.
    """
    #: No PulseOutOption values are applied.
    DEFAULT = 0,
    #: The output operation is held off until the specified trigger condition
    #: is met. Trigger conditions may be modified using :class:`~TmrDevice.set_trigger`.
    EXTTRIGGER = 1 << 5,
    #: The output operation is held off until the specified trigger condition
    #: is met. The trigger is then re-armed and output is held off until
    #: the next trigger. This mode is intended for finite timer operation.
    RETRIGGER = 1 << 6,


class SensorConnectionType(IntEnum):
    """
    Used with :class:`~AiConfig.set_chan_sensor_connection_type` and
    :class:`~AiConfig.get_chan_sensor_connection_type` to specify
    the sensor connection type for a specified A/D channel.
    """
    #: 2-wire with a single sensor per differential channel pair
    SCT_2_WIRE_1 = 1,
    #: 2-wire with two sensors per differential channel pair
    SCT_2_WIRE_2 = 2,
    #: 3-wire with a single sensor per differential channel pair
    SCT_3_WIRE = 3,
    #: 4-wire with a single sensor per differential channel pair
    SCT_4_WIRE = 4,


class TInListFlag(IntEnum):
    """Used with :class:`~AiDevice.t_in_list`."""
    DEFAULT = 0,  #: Placeholder value. Standard functionality.
    WAIT_FOR_NEW_DATA = 1,  #: Wait for new data before returning.


class TInFlag(IntEnum):
    """Used with :class:`~AiDevice.t_in`."""
    DEFAULT = 0,  #: Placeholder value. Standard functionality.
    WAIT_FOR_NEW_DATA = 1,  #: Wait for new data before returning.


class AOutListFlag(IntEnum):
    """
    Contains attributes indicating the conditioning to apply to analog output
    data before it's written to the D/A.
    Used as the flags argument for :class:`~AoDevice.a_out_list`.
    """
    #: Scaled data is supplied and calibration factors are applied to output.
    DEFAULT = 0,
    #: Data is supplied in native format (usually, values ranging from
    #: 0 to 2\ :sup:`resolution`\ - 1).
    NOSCALEDATA = 1 << 0,
    #: Data is output without calibration factors applied.
    NOCALIBRATEDATA = 1 << 1,
    #: All of the specified channels will be updated simultaneously.
    SIMULTANEOUS = 1 << 2,


class AOutSyncMode(IntEnum):
    """
    Used with :class:`~AoConfig.set_sync_mode` and
    :class:`~AoConfig.get_sync_mode` to specify the
    synchronization mode for an analog output subsystem.
    """
    SLAVE = 0,  #: Receive the D/A Load signal from an external source
    MASTER = 1  #: Output the internal D/A Load signal


class AOutSenseMode(IntEnum):
    """
    Used with :class:`~AoConfig.set_chan_sense_mode` and
    :class:`~AoConfig.get_chan_sense_mode` to specify the
    sense mode of a DAC channel.
    """
    DISABLED = 1,  #: Sense mode is disabled.
    ENABLED = 2,   #: Sense mode is enabled.


class CalibrationType(IntEnum):
    """
    Used with :class:`~AiConfig.get_cal_date` to get the calibration
    date for a DAQ device.
    """
    FACTORY = 0,  #: Factory calibration type.
    FIELD = 1,  #: Field calibration type.

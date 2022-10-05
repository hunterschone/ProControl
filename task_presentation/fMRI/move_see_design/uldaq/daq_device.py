"""
Created on Feb 14 2018

@author: MCC
"""
from ctypes import c_int, c_byte, c_longlong, c_ulonglong, py_object, byref
from .ul_enums import DaqEventType, MemRegion, ULError, InterfaceType
from .ul_structs import DaqDeviceDescriptor
from .ul_exception import ULException
from .ul_c_interface import lib, EventParams
from .ul_c_interface import (InterfaceCallbackProcType,
                             interface_event_callback_function, DevConfigItem)
from .daq_device_info import DaqDeviceInfo
from .daq_device_config import DaqDeviceConfig
from .ai_device import AiDevice
from .ao_device import AoDevice
from .dio_device import DioDevice
from .ctr_device import CtrDevice
from .tmr_device import TmrDevice
from .daqi_device import DaqiDevice
from .daqo_device import DaqoDevice
from .utils import enum_mask_to_list


class DaqDevice:
    """
    Creates a :class:`DaqDevice` object based on the daq_device_descriptor
    (usually obtained using :func:`get_daq_device_inventory`). The DaqDevice
    object allows access to all of the classes, methods, and attributes for the
    associated MCC device.

    Args:
        daq_device_descriptor (DaqDeviceDescriptor): The object that describes
            the DAQ device.

    Raises:
        :class:`ULException`
    """
    def __init__(self, daq_device_descriptor):
        self._handle = lib.ulCreateDaqDevice(daq_device_descriptor)
        if self._handle == 0:
            raise ULException(ULError.BAD_DESCRIPTOR)

        self.__dev_info = DaqDeviceInfo(self._handle)
        self.__dev_config = DaqDeviceConfig(self._handle)

        self.__ai_device = None
        if self.__dev_info._has_ai_device():
            self.__ai_device = AiDevice(self._handle)

        self.__ao_device = None
        if self.__dev_info._has_ao_device():
            self.__ao_device = AoDevice(self._handle)

        self.__dio_device = None
        if self.__dev_info._has_dio_device():
            self.__dio_device = DioDevice(self._handle)

        self.__ctr_device = None
        if self.__dev_info._has_ctr_device():
            self.__ctr_device = CtrDevice(self._handle)

        self.__tmr_device = None
        if self.__dev_info._has_tmr_device():
            self.__tmr_device = TmrDevice(self._handle)

        self.__daqi_device = None
        if self.__dev_info._has_daqi_device():
            self.__daqi_device = DaqiDevice(self._handle)

        self.__daqo_device = None
        if self.__dev_info._has_daqo_device():
            self.__daqo_device = DaqoDevice(self._handle)

        # create dictionaries to prevent garbage collection of the items stored
        # in the dictionary
        self.__event_params = {}
        self.__interface_callbacks = {}

    def __del__(self):
        if self._handle is not None:
            try:
                if self.is_connected():
                    self.disconnect()
            finally:
                self.release()

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exe_type, exe_value, exe_traceback):
        self.disconnect()
        self.release()

    def get_descriptor(self):
        # type: () -> DaqDeviceDescriptor
        """
        Returns the DaqDeviceDescriptor for an existing
        :class:`DaqDevice` object.

        Returns:
            DaqDeviceDescriptor: The object that describes the DAQ device.

        Raises:
            :class:`ULException`
        """
        descriptor = DaqDeviceDescriptor()
        err = lib.ulGetDaqDeviceDescriptor(self._handle, byref(descriptor))
        if err != 0:
            raise ULException(err)
        return descriptor

    def connect(self, connection_code=0):
        # type: () -> None
        """
        Establish a connection to a physical DAQ device referenced by
        the :class:`DaqDevice` object.

        Args:
            connection_code (Optional[int]): A code required to connect to
                Ethernet devices if the device's connection code has been
                previously set to something other than the default value of 0.

        Raises:
            :class:`ULException`
        """
        descriptor = self.get_descriptor()
        if descriptor.dev_interface == InterfaceType.ETHERNET:
            err = lib.ulDaqDeviceConnectionCode(self._handle, connection_code)
            if err != 0:
                raise ULException(err)

        err = lib.ulConnectDaqDevice(self._handle)
        if err != 0:
            raise ULException(err)

    def is_connected(self):
        # type: () -> bool
        """
        Gets the DAQ device connection status for the device
        referenced by the :class:`DaqDevice` object.

        Returns:
            bool: True if the DAQ device is connected, otherwise False.

        Raises:
            :class:`ULException`
        """
        connected = c_int()
        err = lib.ulIsDaqDeviceConnected(self._handle, byref(connected))
        if err != 0:
            raise ULException(err)
        return bool(connected)

    def disconnect(self):
        # type: () -> None
        """
        Disconnects from the DAQ device
        referenced by the :class:`DaqDevice` object.

        Raises:
            :class:`ULException`
        """
        err = lib.ulDisconnectDaqDevice(self._handle)
        if err != 0:
            raise ULException(err)

    def flash_led(self, number_of_flashes):
        # type: (int) -> None
        """
        Flashes the LED on the DAQ device for the device
        referenced by the :class:`DaqDevice` object.

        Args:
            number_of_flashes (int): The number of flashes; set to 0 for a
                continuous flash until the next call with a non-zero value.

        Raises:
            :class:`ULException`
        """
        err = lib.ulFlashLed(self._handle, number_of_flashes)
        if err != 0:
            raise ULException(err)

    def get_info(self):
        # type: () -> DaqDeviceInfo
        """
        Gets the DAQ device information object for the device
        referenced by the :class:`DaqDevice` object.

        Returns:
            DaqDeviceInfo: The object used for getting the capabilities of the
                DAQ device.
        """
        return self.__dev_info

    def get_config(self):
        # type: () -> DaqDeviceConfig
        """
        Gets the DAQ device configuration object for the device
        referenced by the :class:`DaqDevice` object.

        Returns:
            DaqDeviceConfig: The object used for getting the configuration of
                the DAQ device.
        """
        return self.__dev_config

    def get_ai_device(self):
        # type: () -> AiDevice
        """
        Gets the analog input subsystem object used to access the
        AI subsystem for the device
        referenced by the :class:`DaqDevice` object.

        Returns:
            AiDevice: The object used to access the AI subsystem.
        """
        return self.__ai_device

    def get_ao_device(self):
        # type: () -> AoDevice
        """
        Gets the analog output subsystem object used to access the
        AO subsystem for the device
        referenced by the :class:`DaqDevice` object.

        Returns:
           AoDevice: The object used to access the AO subsystem.
        """
        return self.__ao_device

    def get_dio_device(self):
        # type: () -> DioDevice
        """
        Gets the digital input/output subsystem object used to access the
        DIO subsystem for the device
        referenced by the :class:`DaqDevice` object.

        Returns:
            DioDevice: The object used to access the DIO subsystem.
        """
        return self.__dio_device

    def get_ctr_device(self):
        # type: () -> CtrDevice
        """
        Gets the counter subsystem object used to access the
        counter subsystem for the device
        referenced by the :class:`DaqDevice` object.

        Returns:
            CtrDevice: The object used to access the counter subsystem.
        """
        return self.__ctr_device

    def get_tmr_device(self):
        # type: () -> TmrDevice
        """
        Gets the timer subsystem object used to access the
        timer subsystem for the device
        referenced by the :class:`DaqDevice` object.

        Returns:
            TmrDevice: The object used to access the timer subsystem.
        """
        return self.__tmr_device

    def get_daqi_device(self):
        # type: () -> DaqiDevice
        """
        Gets the DAQ input subsystem object used to access the
        DAQ input subsystem for the device
        referenced by the :class:`DaqDevice` object.

        Returns:
            DaqiDevice: The object used to access the DAQ input subsystem.
        """
        return self.__daqi_device

    def get_daqo_device(self):
        # type: () -> DaqoDevice
        """
        Gets the DAQ output subsystem object used to access the
        DAQ output subsystem for the device
        referenced by the :class:`DaqDevice` object.

        Returns:
            DaqoDevice: The object used to access the DAQ output subsystem.
        """
        return self.__daqo_device

    def enable_event(self, event_types, event_parameter,
                     event_callback_function, user_data):
        # type: (DaqEventType, int, function, object) -> None
        """
        Binds one or more event conditions to a callback function for the device
        referenced by the :class:`DaqDevice` object.

        Args:
            event_types (DaqEventType): One or more attributes
                (suitable for bit-wise operations) specifying the conditions
                to bind to the callback function.
            event_parameter (int): A numeric value that specifies additional
                information for some event types, such as the number of samples
                for the ON_DATA_AVAILABLE event type.
            event_callback_function (function): The callback function to be
                executed on the event condition.
            user_data (object): Data (defined by the user) to be passed to the
                callback function.

        Raises:
            :class:`ULException`
        """
        event_parameter = c_ulonglong(event_parameter)
        event_list = enum_mask_to_list(DaqEventType, event_types)
        event_params = EventParams()
        event_params.user_data = py_object(user_data)
        event_params.user_callback = py_object(event_callback_function)
        interface_callback = InterfaceCallbackProcType(
            interface_event_callback_function)

        # This code has been added to prevent garbage collection and it should
        # not be removed
        for event in event_list:
            if event & event_types:
                self.__event_params[event] = event_params
                self.__interface_callbacks[event] = interface_callback

        err = lib.ulEnableEvent(c_longlong(self._handle),
                                event_types,
                                event_parameter,
                                interface_callback,
                                event_params)
        if err != 0:
            raise ULException(err)

    def disable_event(self, event_types):
        # type: (DaqEventType) -> None
        """
        Disables one or more event conditions and unbinds the associated
        callback function for the device referenced by the :class:`DaqDevice`
        object.

        Args:
            event_types (DaqEventType): One or more attributes
                (suitable for bit-wise operations) specifying the conditions to
                unbind from the callback function.

        Raises:
            :class:`ULException`
        """
        err = lib.ulDisableEvent(self._handle, event_types)
        if err != 0:
            raise ULException(err)

    def mem_read(self, mem_region_type, address, count):
        # type: (MemRegion, int, int) -> bytearray
        """
        Reads a value from a specified region in memory on the device referenced
        by the :class:`DaqDevice` object.

        Args:
            mem_region_type (MemRegion): The region in memory to read.
            address (int): The memory address.
            count (int): The number of bytes to read.

        Raises:
            :class:`ULException`
        """
        byte_array = c_byte * count  # type: type
        c_buffer = byte_array()
        err = lib.ulMemRead(self._handle, mem_region_type, address, c_buffer,
                            count)
        if err != 0:
            raise ULException(err)

        return bytearray(c_buffer)

    def mem_write(self, mem_region_type, address, mem_buffer,
                  mem_unlock_code=0):
        # type: (MemRegion, int, bytearray, int) -> None
        """
        Writes a block of data to the specified address in the reserve memory
        area on the device referenced by the :class:`DaqDevice` object.

        Args:
            mem_region_type (MemRegion): The region in reserve memory area to
                write to.
            address (int): The memory address .
            mem_buffer (bytearray): The data to write.
            mem_unlock_code (int): The memory unlock code required to write to
                the EEPROM for Ethernet devices.  The default value is 0.  See
                hardware documentation for more details.

        Raises:
            :class:`ULException`
        """
        # Unlock the memory for writes
        err = lib.ulDevSetConfig(self._handle, DevConfigItem.MEM_UNLOCK_CODE,
                                 0, mem_unlock_code)
        if err != 0:
            raise ULException(err)

        # Create array of c_bytes from Python bytearray type
        count = len(mem_buffer)
        byte_array = c_byte * count  # type: type
        c_buffer = byte_array()
        for i in range(count):
            c_buffer[i] = mem_buffer[i]

        err = lib.ulMemWrite(self._handle, mem_region_type, address, c_buffer,
                             count)
        if err != 0:
            raise ULException(err)
        # Lock the memory
        err = lib.ulDevSetConfig(self._handle, DevConfigItem.MEM_UNLOCK_CODE,
                                 0, 0)
        if err != 0:
            raise ULException(err)

    def release(self):
        """
        Removes the device referenced by the :class:`DaqDevice` object
        from the Universal Library, and releases all resources associated
        with that device.

        Raises:
            :class:`ULException`
        """
        err = lib.ulReleaseDaqDevice(self._handle)
        if err != 0:
            raise ULException(err)
        self._handle = None

    def reset(self):
        """
        Resets the DAQ device.  This causes the DAQ device to disconnect from
        the host. Invoke :func:`DaqDevice.connect` to re-establish the
        connection to the device.

        Raises:
            :class:`ULException`
        """
        err = lib.ulDevSetConfig(self._handle, DevConfigItem.RESET, 0, 0)
        if err != 0:
            raise ULException(err)

"""
Created on Feb 16 2018

@author: MCC
"""

from ctypes import c_bool, c_longlong, byref
from .ul_enums import DaqEventType
from .ul_structs import DaqDeviceDescriptor
from .ul_exception import ULException
from .dev_mem_info import DevMemInfo
from .ul_c_interface import lib, DevItemInfo


class DaqDeviceInfo:
    """
    An instance of the DaqDeviceInfo class is obtained by calling
    :func:`DaqDevice.get_info`.
    """

    def __init__(self, handle):
        self.__handle = handle
        self.__dev_mem_info = DevMemInfo(handle)

    def get_product_id(self):
        # type: () -> int
        """
        Gets the product type referenced by the :class:`DaqDevice` object.

        Returns:
            int:

            The product ID.

        Raises:
            :class:`ULException`
        """
        descriptor = DaqDeviceDescriptor()
        err = lib.ulGetDaqDeviceDescriptor(self.__handle, byref(descriptor))
        if err != 0:
            raise ULException(err)
        return descriptor.product_id

    def _has_ai_device(self):
        # type: () -> bool
        """
        Determines whether or not the DAQ device has an analog input subsystem.

        Returns:
            bool:

            True if the device has an analog input subsystem. False if the
            device does not have an analog input subsystem.

        Raises:
            :class:`ULException`
        """
        has_ai = c_longlong()
        err = lib.ulDevGetInfo(self.__handle, DevItemInfo.HAS_AI_DEV, 0,
                               byref(has_ai))
        if err != 0:
            raise ULException(err)
        return c_bool(has_ai).value

    def _has_ao_device(self):
        # type: () -> bool
        """
        Determines whether or not the DAQ device has an analog output subsystem.

        Returns:
            bool:

            True if the device has an analog output subsystem. False if the
            device does not have an analog output subsystem.

        Raises:
            :class:`ULException`
        """
        has_ao = c_longlong()
        err = lib.ulDevGetInfo(self.__handle, DevItemInfo.HAS_AO_DEV, 0,
                               byref(has_ao))
        if err != 0:
            raise ULException(err)
        return c_bool(has_ao).value

    def _has_dio_device(self):
        # type: () -> bool
        """
        Determines whether or not the DAQ device has a digital I/O subsystem.

        Returns:
            bool:

            True if the device has a digital I/O subsystem. False if the
            device does not have a digital I/O subsystem.

        Raises:
            :class:`ULException`
        """
        has_dio = c_longlong()
        err = lib.ulDevGetInfo(self.__handle, DevItemInfo.HAS_DIO_DEV, 0,
                               byref(has_dio))
        if err != 0:
            raise ULException(err)
        return c_bool(has_dio).value

    def _has_ctr_device(self):
        # type: () -> bool
        """
        Determines whether or not the DAQ device has a counter subsystem.

        Returns:
            bool:

            True if the device has a counter subsystem. False if the
            device does not have a counter subsystem.

        Raises:
            :class:`ULException`
        """
        has_ctr = c_longlong()
        err = lib.ulDevGetInfo(self.__handle, DevItemInfo.HAS_CTR_DEV, 0,
                               byref(has_ctr))
        if err != 0:
            raise ULException(err)
        return c_bool(has_ctr).value

    def _has_tmr_device(self):
        # type: () -> bool
        """
        Determines whether or not the DAQ device has a timer subsystem.

        Returns:
            bool:

            True if the device has a timer subsystem. False if the
            device does not have a timer subsystem.

        Raises:
            :class:`ULException`
        """
        has_tmr = c_longlong()
        err = lib.ulDevGetInfo(self.__handle, DevItemInfo.HAS_TMR_DEV, 0,
                               byref(has_tmr))
        if err != 0:
            raise ULException(err)
        return c_bool(has_tmr).value

    def _has_daqi_device(self):
        # type: () -> bool
        """
        Determines whether or not the DAQ device has a DAQ input subsystem.

        Returns:
            bool:

            True if the device has a DAQ input subsystem. False if the
            device does not have a DAQ input subsystem.

        Raises:
            :class:`ULException`
        """
        has_daqi = c_longlong()
        err = lib.ulDevGetInfo(self.__handle, DevItemInfo.HAS_DAQI_DEV, 0,
                               byref(has_daqi))
        if err != 0:
            raise ULException(err)
        return c_bool(has_daqi).value

    def _has_daqo_device(self):
        # type: () -> bool
        """
        Determines whether or not the DAQ device has a DAQ output subsystem.

        Returns:
            bool:

            True if the device has a DAQ output subsystem. False if the
            device does not have a DAQ output subsystem.

        Raises:
            :class:`ULException`
        """
        has_daqo = c_longlong()
        err = lib.ulDevGetInfo(self.__handle, DevItemInfo.HAS_DAQO_DEV, 0,
                               byref(has_daqo))
        if err != 0:
            raise ULException(err)
        return c_bool(has_daqo).value

    def get_event_types(self):
        # type: () -> list[DaqEventType]
        """
        Gets a list of :class:`DaqEventType` values containing the
        types supported by the device referenced by the
        :class:`DaqDevice` object.

        Returns:
            list[DaqEventType]:

            A list of values containing the types supported by the device.

        Raises:
            :class:`ULException`
        """
        event_type_mask = c_longlong()
        event_type_list = []
        err = lib.ulDevGetInfo(self.__handle, DevItemInfo.DAQ_EVENT_TYPES, 0,
                               byref(event_type_mask))
        if err != 0:
            raise ULException(err)

        if event_type_mask == 0:
            event_type_list.append(DaqEventType.NONE)

        else:
            for event_type in DaqEventType:
                if event_type_mask.value & event_type:
                    event_type_list.append(event_type)

        return event_type_list

    def get_mem_info(self):
        # type: () -> DevMemInfo
        """
        Gets the DAQ device memory information object used to retrieve
        information about the reserved memory regions on the DAQ device
        referenced by the :class:`DaqDevice` object.

        Returns:
            DevMemInfo:

            An instance of the object that contains information
            about the reserved memory regions on the DAQ device.

        Raises:
            :class:`ULException`
        """
        return self.__dev_mem_info

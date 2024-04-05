"""
Created on Feb 12 2018

@author: MCC
"""
from ctypes import c_uint, byref
from .ul_enums import InterfaceType
from .ul_structs import DaqDeviceDescriptor
from .ul_exception import ULException
from .ul_c_interface import lib


def _daq_device_descriptor_array(size):
    descriptors_array = DaqDeviceDescriptor * size  # type: type
    return descriptors_array()


def get_daq_device_inventory(interface_type, number_of_devices=100):
    # type: (InterfaceType, int) -> list[DaqDeviceDescriptor]
    """
    Gets a list of :class:`DaqDeviceDescriptor` objects that can be used
    as the :class:`DaqDevice` class parameter to create DaqDevice objects.

    Args:
        interface_type (InterfaceType): One or more of the
            :class:`InterfaceType` attributes (suitable for bit-wise operations)
            specifying which physical interfaces (such as USB) to search for
            MCC devices.
        number_of_devices (Optional[int]): Optional parameter indicating the
            maximum number of devices to return in the list; the default is 100.

    Returns:
        list[DaqDeviceDescriptor]:

        A list of :class:`DaqDeviceDescriptor` objects that describe each of the
        each of the MCC devices found on the specified interface.

    Raises:
        :class:`ULException`
    """
    device_descriptors = _daq_device_descriptor_array(number_of_devices)
    number_of_devices = c_uint(number_of_devices)
    err = lib.ulGetDaqDeviceInventory(interface_type, device_descriptors,
                                      byref(number_of_devices))
    if err != 0:
        raise ULException(err)

    devices_list = [device_descriptors[i] for i in range(
        number_of_devices.value)]
    return devices_list


def get_net_daq_device_descriptor(host, port, ifc_name, timeout=-1):
    # type: (str, int, str or None, float) -> DaqDeviceDescriptor
    """
    Gets a :class:`DaqDeviceDescriptor` object for an Ethernet DAQ device that
    can be used as the :class:`DaqDevice` class parameter to create DaqDevice
    object.

    Args:
        host (str): The remote device host name or IP address.
        port (int): The remote device port number.
        ifc_name (str or None): The network interface name to be used for
            communication with the DAQ device (e.g. eth0, wlan0, etc.);
            Set to None to select the default network interface.
        timeout (Optional[float]): Optional parameter to set the timeout value
            in seconds for the discovery operation to complete;
            Set to -1 (default) to wait indefinitely.

    Returns:
        DaqDeviceDescriptor:

        A :class:`DaqDeviceDescriptor` object for the specified remote device.

    Raises:
         :class:`ULException`
    """
    descriptor = DaqDeviceDescriptor()
    port = c_uint(port)
    if ifc_name is not None:
        ifc_name = ifc_name.encode('utf-8')

    err = lib.ulGetNetDaqDeviceDescriptor(host.encode('utf-8'), port, ifc_name,
                                          byref(descriptor), timeout)
    if err != 0:
        raise ULException(err)
    return descriptor

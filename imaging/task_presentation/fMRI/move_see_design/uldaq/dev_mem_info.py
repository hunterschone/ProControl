"""
Created on Feb 19, 2018

@author: MCC
"""

from ctypes import c_longlong, byref
from .ul_enums import MemRegion
from .ul_structs import MemDescriptor
from .ul_exception import ULException
from .ul_c_interface import lib, DevItemInfo
from .utils import enum_mask_to_list


class DevMemInfo:
    """
    An instance of the DevMemInfo class is obtained by calling
    :func:`DaqDeviceInfo.get_mem_info`.
    """

    def __init__(self, handle):
        self.__handle = handle

    def get_mem_regions(self):
        # type: () -> list[MemRegion]
        """
        Gets a list of memory regions on the device
        referenced by the :class:`DaqDevice` object.

        Returns:
            list[MemRegion]:

            A list of supported MemRegion objects.

        Raises:
            :class:`ULException`
        """
        memory_regions_mask = c_longlong()
        err = lib.ulDevGetInfo(self.__handle, DevItemInfo.MEM_REGIONS, 0,
                               byref(memory_regions_mask))
        if err != 0:
            raise ULException(err)
        return enum_mask_to_list(MemRegion, memory_regions_mask.value)

    def get_mem_descriptor(self, mem_region):
        # type: (MemRegion) -> MemDescriptor
        """
        Gets the memory descriptor object for the specified region of memory
        on the device referenced by the :class:`DaqDevice` object.

        Args:
            mem_region (MemRegion): The memory region.

        Returns:
            MemDescriptor:

            A MemDescriptor object for the specified memory region.

        Raises:
            :class:`ULException`
        """
        mem_descriptor = MemDescriptor()
        err = lib.ulMemGetInfo(self.__handle, mem_region, byref(mem_descriptor))
        if err != 0:
            raise ULException(err)

        return mem_descriptor

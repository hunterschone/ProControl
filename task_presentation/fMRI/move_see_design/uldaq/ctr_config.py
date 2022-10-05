"""
Created on Mar 14 2019

@author: MCC
"""

from ctypes import c_longlong, byref
from .ul_exception import ULException
from .ul_c_interface import lib, CtrConfigItem


class CtrConfig:
    """
    An instance of the CtrConfig class is obtained by calling
    :func:`CtrDevice.get_config`.
    """

    def __init__(self, handle):
        self.__handle = handle

    def set_register_val(self, reg_val):
        # type: (int) -> None
        """
        Configures the register value for the specified counter.

        Args:
            reg_val (int): The counter register value to be set.

        Raises:
            :class:`ULException`
        """
        err = lib.ulCtrSetConfig(self.__handle, CtrConfigItem.REG, 0, reg_val)
        if err != 0:
            raise ULException(err)

    def get_register_val(self):
        # type: () -> int
        """
        Gets the register value for the specified counter.

        Returns:
            int:

            The register value of the specified counter.

        Raises:
            :class:`ULException`
        """
        reg_val = c_longlong()
        err = lib.ulAIGetConfig(self.__handle, CtrConfigItem.REG, 0,
                                byref(reg_val))
        if err != 0:
            raise ULException(err)
        return reg_val.value

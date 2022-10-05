"""
Created on Sep 2018

@author: MCC
"""

from ctypes import c_longlong, byref
from .ul_exception import ULException
from .ul_c_interface import lib, AoConfigItem
from .ul_enums import AOutSyncMode, AOutSenseMode


class AoConfig:
    """
    An instance of the AoConfig class is obtained by calling
    :func:`AoDevice.get_config`.
    """

    def __init__(self, handle):
        self.__handle = handle

    def set_sync_mode(self, sync_mode):
        # type: (AOutSyncMode) -> None
        """
        Configures the synchronization mode for the Analog Output subsystem.

        Args:
            sync_mode (AOutSyncMode): The synchronization mode to be set.

        Raises:
            :class:`ULException`
        """
        err = lib.ulAOSetConfig(self.__handle, AoConfigItem.SYNC_MODE, 0,
                                sync_mode)
        if err != 0:
            raise ULException(err)

    def get_sync_mode(self):
        # type: () -> AOutSyncMode
        """
        Gets the synchronization mode for the Analog Output subsystem.

        Returns:
            AOutSyncMode:

            The synchronization mode.

        Raises:
            :class:`ULException`
        """
        mode = c_longlong()
        err = lib.ulAOGetConfig(self.__handle, AoConfigItem.SYNC_MODE, 0,
                                byref(mode))
        if err != 0:
            raise ULException(err)
        return AOutSyncMode(mode.value)

    def set_chan_sense_mode(self, channel, mode):
        # type: (int, AOutSenseMode) -> None
        """
        Configures the sense mode for the specified DAC channel.

        Args:
            channel (int): The DAC channel number whose sense mode is being set.
            mode (AOutSenseMode): The sense mode to set.

        Raises:
            :class:`ULException`
        """

        err = lib.ulAISetConfig(self.__handle, AoConfigItem.CHAN_SENSE_MODE,
                                channel, mode)
        if err != 0:
            raise ULException(err)

    def get_chan_sense_mode(self, channel):
        # type: (int) -> AOutSenseMode
        """
        Gets the sense mode for the specified DAC channel.

        Args:
            channel (int): The DAC channel number whose sense mode is being
                determined.

        Returns:
            AOutSenseMode:

            The sense mode of the specified channel.

        Raises:
            :class:`ULException`
        """

        mode = c_longlong()
        err = lib.ulAIGetConfig(self.__handle, AoConfigItem.CHAN_SENSE_MODE,
                                channel, byref(mode))
        if err != 0:
            raise ULException(err)
        return AOutSenseMode(mode.value)

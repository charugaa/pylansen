from .enapicommandwithsvn import ENAPICommandWithSvn
from .exceptions import ENAPILenException

import binascii

import logging
log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())

class ENAPIMbusData(ENAPICommandWithSvn):
    MIN_FARME_LEN = 4

    def __init__(self, buf):
        super().__init__(buf)
        if not self.is_frame_complete:
            log.debug("incomplete frame: %s", vars(self))
            raise ENAPILenException("data frame is not complete")
        self.MbusData = self.data[2:-3]
        self.MbusData[0] -= 1 # remove RSSI byte from L-field
        self.RSSI = int(self.data[-3])

        # FIXME: this frame comes from repeater? some unknown data needs to be removed
        if self.MbusData[0] < len(self.MbusData):
            log.info("L-field=%d but data len=%d, fixing..", self.MbusData[0], len(self.MbusData))
            log.debug("MbusData(%d): %s", len(self.MbusData), binascii.hexlify(self.MbusData))
            self._unknown_data = self.MbusData[self.MbusData[0]:]
            self.MbusData = self.MbusData[:self.MbusData[0]]

            log.debug("MbusData(%d): %s", len(self.MbusData), binascii.hexlify(self.MbusData))
            log.debug("remaining(%d): %s", len(self._unknown_data), binascii.hexlify(self._unknown_data))
    @property
    def MbusData(self):
        return self._MbusData

    @MbusData.setter
    def MbusData(self, value):
        self._MbusData = value

    @property
    def RSSI(self):
        return self._RSSI

    @RSSI.setter
    def RSSI(self, value):
        self._RSSI = value

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

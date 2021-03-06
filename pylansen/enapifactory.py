from .enapicommand import ENAPICommand
from .enapiversionlong import ENAPIVersionLong
from .enapimbusdata import ENAPIMbusData
from .enapiack import ENAPIAck
from .enapimbusmode import ENAPIMbusMode
from .exceptions import ENAPICommandTypeNotImplementedException

import logging
log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())

class ENAPIFactory(object):
    @staticmethod
    def factory(buf):
        enapi_command_type = ENAPICommand.get_command_type(buf)
        if (enapi_command_type == ENAPICommand.ENAPI_VERSION_LONG):
            log.debug("found ENAPICommand ENAPI_VERSION_LONG")
            return ENAPIVersionLong(buf)
        if (enapi_command_type == ENAPICommand.ENAPI_MBUS_DATA):
            log.debug("found ENAPICommand ENAPI_MBUS_DATA")
            return ENAPIMbusData(buf)
        if (enapi_command_type == ENAPICommand.ENAPI_ACK):
            log.debug("found ENAPICommand ENAPI_ACK")
            return ENAPIAck(buf)
        if (enapi_command_type == ENAPICommand.ENAPI_MBUS_MODE):
            log.debug("found ENAPICommand ENAPI_MBUS_MODE")
            return ENAPIMbusMode(buf)

        raise ENAPICommandTypeNotImplementedException("Unknown CommandType {:d}".format(enapi_command_type))

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

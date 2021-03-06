from ..message_class import *
from ..message_id import *
from ..payload import *
from ..message import *


config = Bitfield(4, entries=[
    BitfieldEntry("bbThreshold", slice(0, 4)),
    BitfieldEntry("cwThreshold", slice(4, 9)),
    BitfieldEntry("algorithmBits", slice(9, 32)),
    BitfieldEntry("enable", 31)
])

config2 = Bitfield(4, entries=[
    BitfieldEntry("generalBits", slice(0, 12)),
    BitfieldEntry("antSetting", slice(12, 14)),
    BitfieldEntry("enable2", 14)
])

payload_description0 = Fields(
    ("config", config),
    ("config2", config2),
)

description = MessageDescription(
    message_class=CFG,
    message_id=MessageId("ITFM", b"\x39"),
    payload_description=Options(
        Empty,
        payload_description0
    )
)

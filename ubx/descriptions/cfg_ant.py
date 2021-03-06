from ..message_class import *
from ..message_id import *
from ..payload import *
from ..message import *


flags = Bitfield(2, entries=[
    BitfieldEntry("scvs", 0),
    BitfieldEntry("scd", 1),
    BitfieldEntry("ocd", 2),
    BitfieldEntry("pdwnOnSCD", 3),
    BitfieldEntry("recovery", 4),
])

pins = Bitfield(2, entries=[
    BitfieldEntry("pinSwitch", slice(0, 5)),
    BitfieldEntry("pinSCD", slice(5, 10)),
    BitfieldEntry("pinOCD", slice(10, 15)),
    BitfieldEntry("reconfig", 15)
])

payload_description0 = Fields(
    ("flags", flags),
    ("pins", pins),
)

description = MessageDescription(
    message_class=CFG,
    message_id=MessageId("ANT", b"\x13"),
    payload_description=Options(
        Empty,
        payload_description0,
    )
)

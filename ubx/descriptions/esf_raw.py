from ..message_class import *
from ..message_id import *
from ..payload import *
from ..message import *


data = Bitfield(4, entries=[
    BitfieldEntry("dataField", slice(0, 24)),
    BitfieldEntry("dataType", slice(24, 32))
])

measurement = Fields(
    ("data", data),
    ("sTtag", U4)
)

payload_description0 = Fields(
    ("reserved1", 4*U1),
    ("measurements", MatchedLoop(measurement))
)

description = MessageDescription(
    message_class=ESF,
    message_id=MessageId("RAW", b"\x03"),
    payload_description=Options(
        Empty,
        payload_description0,
    )
)

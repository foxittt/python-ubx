from ..classid import *
from ..payload import *
from ..message import *


flags = Bitfield(1, entries=[
    BitfieldEntry("src", slice(0, 3)),
])

payload_description = Fields(
    ("itow", I4),
    ("frac", I4),
    ("deltaMs", I4),
    ("deltaNs", I4),
    ("wno", U2),
    ("flags", flags),
    ("reserved1", U1)
)

description = MessageDescription(
    name="TIM-VRFY",
    message_class=TIM,
    message_id=b"\x06",
    payload_description=Options(
        Empty,
        payload_description
    )
)

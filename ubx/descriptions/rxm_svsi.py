from ..payload import *
from ..message import *


svFlag = Bitfield(1, entries=[
    BitfieldEntry("ura", slice(0, 4)),
    BitfieldEntry("healthy", 4),
    BitfieldEntry("ephVal", 5),
    BitfieldEntry("almVal", 6),
    BitfieldEntry("notAvail", 7)
])

age = Bitfield(1, entries=[
    BitfieldEntry("almAge", slice(0, 4)),
    BitfieldEntry("ephAge", slice(4, 8)),
])

sv = Fields(
    ("svid", U1),
    ("svFlag", svFlag),
    ("azim", I2),
    ("elev", I1),
    ("age", age)
)

payload_description = Fields(
    ("iTOW", U4),
    ("week", I2),
    ("numVis", U1),
    ("numSV", U1),
    ("svs", KeyLoop("numSV", sv))
)

description = MessageDescription(
    name="RXM-SVSI",
    message_class=b"\x02",
    message_id=b"\x20",
    payload_description=Options(
        Empty,
        payload_description
    )
)

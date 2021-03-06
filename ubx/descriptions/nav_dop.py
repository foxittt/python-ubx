from ..message_class import *
from ..message_id import *
from ..payload import *
from ..message import *


payload_description0 = Fields(
    ("iTOW", U4),
    ("gDOP", U2),
    ("pDOP", U2),
    ("tDOP", U2),
    ("vDOP", U2),
    ("hDOP", U2),
    ("nDOP", U2),
    ("eDOP", U2),
)

description = MessageDescription(
    message_class=NAV,
    message_id=MessageId("DOP", b"\x04"),
    payload_description=Options(
        Empty,
        payload_description0,
    )
)

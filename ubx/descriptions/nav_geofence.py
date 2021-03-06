from ..message_class import *
from ..message_id import *
from ..payload import *
from ..message import *


fence = Fields(
    ("state", U1),
    ("reserved1", U1)
)

payload_description0 = Fields(
    ("iTOW", U4),
    ("version", U1),
    ("status", U1),
    ("numFences", U1),
    ("combState", U1),
    ("fences", KeyLoop("numFences", fence))
)

description = MessageDescription(
    message_class=NAV,
    message_id=MessageId("GEOFENCE", b"\x39"),
    payload_description=Options(
        Empty,
        payload_description0,
    )
)

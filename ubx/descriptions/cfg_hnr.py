from ..payload import *
from ..message import *


payload_description0 = Fields(
    ("highNavRate", U1),
    ("reserved1", List(3*[U1])),
)

description = MessageDescription(
    name="CFG-HNR",
    message_class=b"\x06",
    message_id=b"\x5c",
    payload_description=Options(
        Empty,
        payload_description0,
    )
)

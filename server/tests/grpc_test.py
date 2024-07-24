import grpc
from google.protobuf.json_format import MessageToDict
from google.protobuf.timestamp_pb2 import Timestamp
import time

import sys, os
sys.path.insert(0, os.path.abspath('..'))

from scripts.api.v2.attendance.mark_attendance_pb2 import AttendanceRequest
from scripts.api.v2.attendance.mark_attendance_pb2_grpc import AttendanceServiceStub

CHANNEL_OPTIONS = [
    ("grpc.http2.max_pings_without_data", 0),
    ("grpc.keepalive_permit_without_calls", 1),
    ("grpc.keepalive_timeout_ms", 10000),
]

channel = grpc.insecure_channel("localhost:50051", CHANNEL_OPTIONS)
channel.unary_stream("MarkAttendance")
client = AttendanceServiceStub(channel)

request = AttendanceRequest(
    embedding=[0 for x in range(128)],
    time={
        "nanos": 0,
        "seconds": int(time.time())
    }
)

for i in range(100):
    client.MarkAttendance(request)
    print(i)

from ...database.MainDataAPI import MainDataAPI
from ...database.models import ClassEntry
import datetime

from concurrent import futures

import grpc
from grpc_interceptor import ExceptionToStatusInterceptor

from .attendance.mark_attendance_pb2_grpc import \
    add_AttendanceServiceServicer_to_server
from .attendance.mark_attendance_pb2_grpc import AttendanceServiceServicer
from .attendance.mark_attendance_pb2 import AttendanceResponse


grpc_database: MainDataAPI = None


def getgrpcDatabase() -> MainDataAPI:
    global grpc_database
    if grpc_database is None:
        grpc_database = MainDataAPI()
    return grpc_database


def time_to_seconds(time_obj):
    if time_obj is None:
        return None
    total_seconds = \
        time_obj.hour * 3600 + time_obj.minute * 60 + time_obj.second
    return total_seconds


def seconds_to_datetime(seconds):
    if seconds is None:
        return None
    return datetime.datetime.fromtimestamp(seconds)


class AttendanceService(AttendanceServiceServicer):
    def MarkAttendance(self, request, context):
        res = getgrpcDatabase().getStudentFromFace(request.embedding)
        if res is not None:
            student_id = None
            class_entry: ClassEntry = None
            print(res)
            student_id, _ = res.id, res.face_embedding
            if type(student_id) is not None:
                if request.time:
                    class_entry = getgrpcDatabase() \
                        .markAttendance(
                            student_id,
                            seconds_to_datetime(request.time.seconds)
                        )
            if class_entry is False:
                return AttendanceResponse(
                    found=False,
                    student_id=-1,
                    end_time={}
                )
            else:
                return AttendanceResponse(
                    found=True,
                    student_id=student_id,
                    end_time={
                        "nanos": 0,
                        "seconds": time_to_seconds(class_entry.end_time)
                    })
        return AttendanceResponse(
            found=False,
            student_id=-1,
            end_time={}
        )


def serve_grpc():
    interceptors = [ExceptionToStatusInterceptor()]
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10), interceptors=interceptors
    )
    add_AttendanceServiceServicer_to_server(AttendanceService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve_grpc()

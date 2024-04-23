from . import ClassDataAPI, StudentDataAPI, AttendanceDataAPI, RegisterDataAPI


class MainDataAPI(ClassDataAPI.ClassDataAPI, StudentDataAPI.StudentDataAPI,
                  AttendanceDataAPI.AttendanceDataAPI,
                  RegisterDataAPI.RegisterDataAPI):
    def __init__(self):
        super().__init__()

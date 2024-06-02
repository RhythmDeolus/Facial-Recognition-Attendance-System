from . import ClassDataAPI, StudentDataAPI, AttendanceDataAPI,\
    RegisterDataAPI, ListDataAPI
from .models.Base import Base

class MainDataAPI(ClassDataAPI.ClassDataAPI, StudentDataAPI.StudentDataAPI,
                  AttendanceDataAPI.AttendanceDataAPI,
                  RegisterDataAPI.RegisterDataAPI,
                  ListDataAPI.ListDataAPI):
    def __init__(self):
        super().__init__()
        Base.metadata.create_all(self.engine, checkfirst=True)

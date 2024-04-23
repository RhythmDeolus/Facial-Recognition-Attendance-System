import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
import sqlalchemy as db
from scripts.database.FaceRecog import FaceRecog
from sqlalchemy.ext.declarative import declarative_base
from models import ClassEntry


class ClassDataAPI:
    def __init__(self):
        self.engine = db.create_engine(os.getenv('DB_URL'))
        self.Base = declarative_base()
        self.Base.metadata.create_all(self.engine, checkfirst=True)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()
        self.session.execute(text('CREATE EXTENSION IF NOT EXISTS vector'))
        self.session.commit()
        self.fr = FaceRecog()

    def registerClass(self, subject_id, date, start_time, end_time,
                      semester_id, course_id, academic_calendar_id,
                      timetable_id):
        class_entry = ClassEntry(subject_id=subject_id, date=date,
                                 start_time=start_time, end_time=end_time,
                                 semester_id=semester_id, course_id=course_id,
                                 academic_calendar_id=academic_calendar_id,
                                 timetable_id=timetable_id)
        self.session.add(class_entry)
        self.session.commit()

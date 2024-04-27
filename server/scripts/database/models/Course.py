from sqlalchemy import Column, Integer, String
from .Base import Base


class Course(Base):
    __tablename__ = 'course'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(20), nullable=False)
    description = Column(String(50), nullable=True)

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return f"<Course(name={self.name})>"

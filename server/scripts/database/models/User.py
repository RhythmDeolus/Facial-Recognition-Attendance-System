from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    email = Column(String(50), nullable=False)
    password = Column(String(20), nullable=False)
    student_id = Column(Integer, nullable=True)
    role = Column(String(20), nullable=False)

    def __init__(self, name, email, password, role):
        self.name = name
        self.email = email
        self.password = password
        self.role = role

    def __repr__(self):
        return f"<User(name={self.name}, \
                       email={self.email}, role={self.role})>"

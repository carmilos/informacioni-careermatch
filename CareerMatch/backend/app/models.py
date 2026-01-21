from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Text, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_hr = Column(Boolean, default=False)
    jobs = relationship('Job', back_populates='owner')

class Job(Base):
    __tablename__ = 'jobs'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    company = Column(String, index=True)
    location = Column(String, index=True)
    description = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    owner_id = Column(Integer, ForeignKey('users.id'))
    owner = relationship('User', back_populates='jobs')
    applicants = relationship('Applicant', back_populates='job')

class Applicant(Base):
    __tablename__ = 'applicants'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    cv_path = Column(String)
    applied_at = Column(DateTime, default=datetime.utcnow)
    job_id = Column(Integer, ForeignKey('jobs.id'))
    job = relationship('Job', back_populates='applicants')

from sqlalchemy import Column, Integer, String, Text, Float, TIMESTAMP, ForeignKey
from sqlalchemy.orm import declarative_base
from datetime import datetime, timezone

Base = declarative_base()

class Job(Base):
    __tablename__ = "jobs"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    company = Column(String)
    location = Column(String)
    description = Column(Text)
    url = Column(String, unique=True)
    posted_at = Column(TIMESTAMP(timezone=True),
    default=lambda: datetime.now(timezone.utc))


class Resume(Base):
    __tablename__ = "resume"
    id = Column(Integer, primary_key=True)
    full_name = Column(String)
    skills = Column(Text)
    experience = Column(Text)
    updated_at = Column(TIMESTAMP(timezone=True),
    default=lambda: datetime.now(timezone.utc))


class Match(Base):
    __tablename__ = "matches"
    id = Column(Integer, primary_key=True)
    job_id = Column(Integer, ForeignKey("jobs.id"))
    resume_id = Column(Integer, ForeignKey("resume.id"))
    score = Column(Float)
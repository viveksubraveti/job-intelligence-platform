# backend/schemas.py
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class JobBase(BaseModel):
    # What fields from your Job model should be in requests?
    # Hint: title, company, location, description, url
    title: str
    company: str
    location: str
    description: str
    url: str

class JobCreate(JobBase):
    # Inherits all fields from JobBase - no need to repeat them
    pass

class JobUpdate(BaseModel):
    # All fields optional for partial updates
    title: Optional[str] = None
    company: Optional[str] = None
    location: Optional[str] = None
    description: Optional[str] = None
    url: Optional[str] = None

class JobResponse(JobBase):
    # What additional fields should be in response?
    # Hint: id, posted_at from your model
    id: int
    posted_at: datetime
    class Config:
        # This tells Pydantic to work with SQLAlchemy models
        from_attributes = True

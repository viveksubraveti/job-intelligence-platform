from sqlalchemy.orm import Session
from . import models, schemas

# Think about:
# - How do you get a single job by ID?
# - How do you get all jobs with pagination?
# - How do you create a new job?
# - How do you update existing job?
# - How do you delete a job?

def get_job(db: Session, job_id: int):
    # How do you query by ID?
    return db.query(models.Job).filter(models.Job.id == job_id).first()

def get_jobs(db: Session, skip: int = 0, limit: int = 100):
    # How do you get multiple records with pagination?
    return db.query(models.Job).offset(skip).limit(limit).all()

def create_job(db: Session, job: schemas.JobCreate):
    # Step 1: Convert Pydantic to dict
    job_data = job.model_dump()
    
    # Step 2: Create SQLAlchemy model instance
    db_job = models.Job(**job_data)
    
    # Step 3: Add to database session
    db.add(db_job)
    
    # Step 4: Commit to save in database
    db.commit()
    
    # Step 5: Refresh to get ID and timestamps from DB
    db.refresh(db_job)
    
    # Step 6: Return the created job
    return db_job

def update_job(db: Session, job_id: int, job_update: schemas.JobUpdate):
    # Find existing job
    job = get_job(db, job_id)
    if not job:
        return None
    
    # Get only the fields that were provided
    job_update_data = job_update.model_dump(exclude_unset=True)
    
    # Update each provided field
    for key, value in job_update_data.items():
        setattr(job, key, value)
    
    # Save changes
    db.commit()
    db.refresh(job)
    return job

def delete_job(db: Session, job_id: int):
    job = get_job(db, job_id)
    if not job:
        return None
    db.delete(job)
    db.commit()
    return job
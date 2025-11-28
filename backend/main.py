# backend/main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas, database

app = FastAPI()

# Import the get_db from database module
from .database import get_db

# Jobs endpoints
@app.post("/jobs/", response_model=schemas.JobResponse)
def create_job(job: schemas.JobCreate, db: Session = Depends(get_db)):
    # How do you call your crud function and handle errors?
    return crud.create_job(db=db, job=job)

@app.get("/jobs/", response_model=list[schemas.JobResponse])
def read_jobs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    # How do you return a list of jobs?
    return crud.get_jobs(db=db, skip=skip, limit=limit)

@app.get("/jobs/{job_id}", response_model=schemas.JobResponse)
def read_job(job_id: int, db: Session = Depends(get_db)):
    job = crud.get_job(db=db, job_id=job_id)
    if job is None:
        raise HTTPException(status_code=404, detail="Job not found")
    return job

@app.put("/jobs/{job_id}", response_model=schemas.JobResponse)
def update_job(job_id: int, job_update: schemas.JobUpdate, db: Session = Depends(get_db)):
    updated_job = crud.update_job(db=db, job_id=job_id, job_update=job_update)
    if updated_job is None:
        raise HTTPException(status_code=404, detail="Job not found")
    return updated_job

@app.delete("/jobs/{job_id}", status_code=204)
def delete_job(job_id: int, db: Session = Depends(get_db)):
    deleted_job = crud.delete_job(db=db, job_id=job_id)
    if deleted_job is None:
        raise HTTPException(status_code=404, detail="Job not found")
    return None  # 204 No Content - successful deletion
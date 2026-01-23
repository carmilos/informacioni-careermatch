import hashlib
from sqlalchemy.orm import Session
from . import models, schemas
from passlib.context import CryptContext
from typing import List

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
def hash_password(password: str) -> str:
    pw = password.encode("utf-8")[:72]
    return pwd_context.hash(pw)

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed = hash_password(user.password)
    db_user = models.User(email=user.email, hashed_password=hashed, is_hr=user.is_hr)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def authenticate_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)
    if not user:
        return None
    if not pwd_context.verify(password, user.hashed_password):
        return None
    return user

def create_job(db: Session, job: schemas.JobCreate, owner_id: int):
    db_job = models.Job(**job.dict(), owner_id=owner_id)
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job

def list_jobs(db: Session, skip: int = 0, limit: int = 100) -> List[models.Job]:
    return db.query(models.Job).offset(skip).limit(limit).all()

def get_job(db: Session, job_id: int):
    return db.query(models.Job).filter(models.Job.id == job_id).first()

def create_applicant(db: Session, job_id: int, applicant: schemas.ApplicantCreate, cv_path: str):
    db_app = models.Applicant(name=applicant.name, email=applicant.email, cv_path=cv_path, job_id=job_id)
    db.add(db_app)
    db.commit()
    db.refresh(db_app)
    return db_app

def get_applicants_for_job(db: Session, job_id: int):
    return db.query(models.Applicant).filter(models.Applicant.job_id == job_id).all()

def update_job(db: Session, job_id: int, job_update: schemas.JobUpdate):
    job = db.query(models.Job).filter(models.Job.id == job_id).first()
    if not job:
        return None
    for field, value in job_update.dict(exclude_unset=True).items():
        setattr(job, field, value)
    db.commit()
    db.refresh(job)
    return job

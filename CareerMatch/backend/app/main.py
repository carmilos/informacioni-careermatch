import os
from fastapi import FastAPI, Depends, HTTPException, UploadFile, File, Form, Path
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from typing import List

from . import models, schemas, crud, auth
from .database import engine, get_db
from .config import UPLOAD_DIR

models.Base.metadata.create_all(bind=engine)

os.makedirs(UPLOAD_DIR, exist_ok=True)

app = FastAPI(title='CareerMatch API')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post('/auth/register', response_model=schemas.UserOut)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail='Email already registered')
    created = crud.create_user(db, user)
    return created


@app.post('/auth/login', response_model=schemas.Token)
def login(form_data: dict, db: Session = Depends(get_db)):
    # form_data expects {"username":..., "password":...} from OAuth2PasswordRequestForm
    email = form_data.get('username') or form_data.get('email')
    password = form_data.get('password')
    user = crud.authenticate_user(db, email, password)
    if not user:
        raise HTTPException(status_code=401, detail='Incorrect credentials')
    access_token = auth.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}


@app.get('/auth/me', response_model=schemas.UserOut)
def read_current_user(current_user: models.User = Depends(auth.get_current_user)):
    return current_user


@app.get('/jobs', response_model=List[schemas.JobOut])
def list_jobs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.list_jobs(db, skip=skip, limit=limit)


@app.post('/jobs', response_model=schemas.JobOut)
def create_job(job: schemas.JobCreate, current_user: models.User = Depends(auth.get_current_user), db: Session = Depends(get_db)):
    if not current_user.is_hr:
        raise HTTPException(status_code=403, detail='HR users only')
    return crud.create_job(db, job, owner_id=current_user.id)


@app.get('/jobs/{job_id}', response_model=schemas.JobOut)
def get_job(job_id: int, db: Session = Depends(get_db)):
    db_job = crud.get_job(db, job_id)
    if not db_job:
        raise HTTPException(status_code=404, detail='Job not found')
    return db_job


@app.post('/jobs/{job_id}/apply', response_model=schemas.ApplicantOut)
def apply_job(
    job_id: int,
    name: str = Form(...),
    email: str = Form(...),
    cv: UploadFile = File(None),
    cv_text: str = Form(None),
    db: Session = Depends(get_db),
):
    job = crud.get_job(db, job_id)
    if not job:
        raise HTTPException(status_code=404, detail='Job not found')
    filename = None
    if cv is not None:
        filename = f"{job_id}_{int(__import__('time').time())}_{cv.filename}"
        dest = os.path.join(UPLOAD_DIR, filename)
        with open(dest, 'wb') as f:
            f.write(cv.file.read())
    elif cv_text and cv_text.strip():
        filename = f"{job_id}_{int(__import__('time').time())}_cv_text.txt"
        dest = os.path.join(UPLOAD_DIR, filename)
        with open(dest, 'w', encoding='utf-8') as f:
            f.write(cv_text)
    else:
        raise HTTPException(status_code=400, detail='CV file or text required')
    applicant = schemas.ApplicantCreate(name=name, email=email)
    created = crud.create_applicant(db, job_id, applicant, cv_path=filename)
    return created


@app.get('/jobs/{job_id}/applicants', response_model=List[schemas.ApplicantOut])
def get_applicants(job_id: int, current_user: models.User = Depends(auth.get_current_user), db: Session = Depends(get_db)):
    job = crud.get_job(db, job_id)
    if not job:
        raise HTTPException(status_code=404, detail='Job not found')
    if job.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail='Only poster can view applicants')
    applicants = crud.get_applicants_for_job(db, job_id)
    # Učitaj tekstove CV-jeva
    cvs = []
    for a in applicants:
        cv_text = ''
        if a.cv_path:
            file_path = os.path.join(UPLOAD_DIR, a.cv_path)
            if os.path.exists(file_path):
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        cv_text = f.read()
                except Exception:
                    cv_text = ''
        cvs.append({'name': a.name, 'email': a.email, 'text': cv_text})
    # Provera da li ima bar jedan validan CV tekst
    has_valid_cv = any(cv['text'].strip() for cv in cvs)
    result = []
    if has_valid_cv:
        from .ai_cv_analyzer_sr import CVAnalyzer, srpski_stop_reci
        analyzer = CVAnalyzer(stop_words=srpski_stop_reci)
        ranked = analyzer.rank_applicants(job.description or '', cvs)
        for a in applicants:
            score = next((r['similarity'] for r in ranked if r['email'] == a.email), None)
            result.append({
                'id': a.id,
                'name': a.name,
                'email': a.email,
                'cv_path': a.cv_path,
                'applied_at': a.applied_at,
                'score': score
            })
    else:
        for a in applicants:
            result.append({
                'id': a.id,
                'name': a.name,
                'email': a.email,
                'cv_path': a.cv_path,
                'applied_at': a.applied_at,
                'score': None
            })
    return result


@app.get('/uploads/{filename}')
def get_upload(filename: str):
    path = os.path.join(UPLOAD_DIR, filename)
    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail='File not found')
    return FileResponse(path)

@app.put('/jobs/{job_id}', response_model=schemas.JobOut)
def update_job(job_id: int = Path(...), job: schemas.JobUpdate = None, current_user: models.User = Depends(auth.get_current_user), db: Session = Depends(get_db)):
    db_job = crud.get_job(db, job_id)
    if not db_job:
        raise HTTPException(status_code=404, detail='Job not found')
    if not current_user.is_hr or db_job.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail='Not authorized')
    updated = crud.update_job(db, job_id, job)
    return updated
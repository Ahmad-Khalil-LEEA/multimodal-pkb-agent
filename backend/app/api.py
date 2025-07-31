from fastapi import APIRouter, UploadFile, File, Form, Depends
from sqlalchemy.orm import Session
from .db import SessionLocal
from .models import File as DBFile, Note, Project
import shutil
import os

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

UPLOAD_DIR = "/app/uploads"

@router.post("/upload/")
async def upload_file(file: UploadFile = File(...), db: Session = Depends(get_db)):
    file_location = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    db_file = DBFile(filename=file.filename, filetype=file.content_type)
    db.add(db_file)
    db.commit()
    return {"filename": file.filename}

@router.get("/projects/")
def list_projects(db: Session = Depends(get_db)):
    return db.query(Project).all()

@router.post("/projects/")
def create_project(name: str = Form(...), description: str = Form(""), db: Session = Depends(get_db)):
    project = Project(name=name, description=description)
    db.add(project)
    db.commit()
    return project

@router.post("/notes/")
def add_note(content: str = Form(...), project_id: int = Form(...), db: Session = Depends(get_db)):
    note = Note(content=content, project_id=project_id)
    db.add(note)
    db.commit()
    return note

@router.get("/query/")
def semantic_query(q: str, db: Session = Depends(get_db)):
    # Dummy response, see main.py for actual implementation
    return {"answer": "This endpoint is coming soon"}

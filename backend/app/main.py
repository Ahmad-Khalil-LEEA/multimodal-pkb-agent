from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import api, models, db
from sqlalchemy.orm import Session
import os

app = FastAPI()
app.include_router(api.router)

origins = [
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# DB init
@app.on_event("startup")
def startup():
    models.Base.metadata.create_all(bind=db.engine)

from fastapi import APIRouter
from app.core.database import Base, engine

router = APIRouter()

@router.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

@router.get("/")
def root():
    return {"message": "API funcionando correctamente"}
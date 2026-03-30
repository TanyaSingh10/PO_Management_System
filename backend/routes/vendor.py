from dependencies import get_current_user
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import crud, schemas
from database import get_db

router = APIRouter()

@router.post("/")
def create_vendor(
    vendor: schemas.VendorCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    return crud.create_vendor(db, vendor)

@router.get("/")
def get_all_vendors(db: Session = Depends(get_db)):
    return crud.get_vendors(db)

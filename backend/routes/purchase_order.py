from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import crud, schemas
from database import get_db
from dependencies import get_current_user

router = APIRouter()

@router.post("/")
def create_po(
    po: schemas.PurchaseOrderCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)   # ✅ ADD THIS LINE
):
    return crud.create_po(db, po)

@router.get("/")
def get_all_po(db: Session = Depends(get_db)):
    return crud.get_pos(db)

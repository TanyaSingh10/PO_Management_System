from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import crud, schemas
from database import get_db
from dependencies import get_current_user

router = APIRouter()

@router.post("/")
def create_product(
    product: schemas.ProductCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    return crud.create_product(db, product)

@router.get("/")
def get_all_products(db: Session = Depends(get_db)):
    return crud.get_products(db)

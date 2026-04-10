from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import models

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/auctions")
def get_auctions(db: Session = Depends(get_db)):
    return db.query(models.AuctionItem).all()


@router.get("/auctions/{auction_id}")
def get_auction(auction_id: int, db: Session = Depends(get_db)):
    return db.query(models.AuctionItem).filter(models.AuctionItem.id == auction_id).first()
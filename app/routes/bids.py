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


@router.get("/auctions/{auction_id}/bids")
def get_bids(auction_id: int, db: Session = Depends(get_db)):
    return (
        db.query(models.Bid)
        .filter(models.Bid.auction_id == auction_id)
        .order_by(models.Bid.amount.desc())
        .limit(10)
        .all()
    )


@router.post("/auctions/{auction_id}/bid")
def place_bid(auction_id: int, amount: float, user_name: str, db: Session = Depends(get_db)):
    bid = models.Bid(
        auction_id=auction_id,
        amount=amount,
        user_name=user_name
    )

    db.add(bid)

    auction = db.query(models.AuctionItem).filter(models.AuctionItem.id == auction_id).first()
    if auction and amount > auction.current_price:
        auction.current_price = amount

    db.commit()
    return {"message": "Bid placed"}
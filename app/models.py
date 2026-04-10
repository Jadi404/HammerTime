from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from datetime import datetime
from .database import Base

class AuctionItem(Base):
    __tablename__ = "auction_items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    category = Column(String)
    description = Column(String)
    image = Column(String)
    starting_price = Column(Float)
    current_price = Column(Float)


class Bid(Base):
    __tablename__ = "bids"

    id = Column(Integer, primary_key=True, index=True)
    auction_id = Column(Integer, ForeignKey("auction_items.id"))
    user_name = Column(String)
    amount = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)
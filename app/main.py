from fastapi import FastAPI
from .database import Base, engine
from .routes import auctions, bids

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auctions.router)
app.include_router(bids.router)
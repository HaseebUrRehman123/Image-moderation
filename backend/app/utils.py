from fastapi import Header, HTTPException
from .database import tokens_collection

def verify_token(x_token: str = Header(...)):
    if not tokens_collection.find_one({"token": x_token}):
        raise HTTPException(status_code=401, detail="Invalid or missing token")

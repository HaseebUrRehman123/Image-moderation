from fastapi import APIRouter, HTTPException, Depends
from uuid import uuid4
from .database import tokens_collection

router = APIRouter(prefix="/auth", tags=["auth"])

# Simulate admin authentication
def admin_auth():
    # For demo, allow all; replace with real admin check
    return True

@router.post("/tokens")
def create_token(admin: bool = Depends(admin_auth)):
    token = str(uuid4())
    tokens_collection.insert_one({"token": token})
    return {"token": token}

@router.get("/tokens")
def list_tokens(admin: bool = Depends(admin_auth)):
    tokens = list(tokens_collection.find({}, {"_id": 0}))
    return {"tokens": tokens}

@router.delete("/tokens/{token}")
def delete_token(token: str, admin: bool = Depends(admin_auth)):
    result = tokens_collection.delete_one({"token": token})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Token not found")
    return {"message": "Token deleted"}

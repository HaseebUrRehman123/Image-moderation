from fastapi import APIRouter, UploadFile, File, Depends
from app.utils import verify_token
from app.model import analyze_with_sightengine

router = APIRouter(tags=["moderation"])

@router.post("/moderate")
async def moderate_image(file: UploadFile = File(...), token: str = Depends(verify_token)):
    contents = await file.read()
    try:
        result = analyze_with_sightengine(contents)
    except Exception as e:
        return {"error": str(e)}

    return {
        "filename": file.filename,
        "moderation_result": result
    }

from fastapi import APIRouter

router = APIRouter()


@router.get("/apistatus", status_code=200)
async def api_status():
    return {"detail": "API is already running. 🚀"}

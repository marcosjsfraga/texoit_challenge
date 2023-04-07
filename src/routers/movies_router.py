from fastapi import APIRouter

router = APIRouter()

@router.get('/movies', status_code=200)
async def api_status():
    return { 'detail': 'Movies route.' }

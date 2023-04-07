from fastapi import APIRouter
from repositories.movies_repository import MoviesRepository

router = APIRouter()

@router.get('/producers_by_prize_ranges', status_code=200)
async def api_status():
    moviesRepository = MoviesRepository()
    return moviesRepository.get_producers_by_prize_ranges()
    

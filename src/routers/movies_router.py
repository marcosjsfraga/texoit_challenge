from fastapi import APIRouter
from repositories.movies_repository import MoviesRepository


router = APIRouter()
moviesRepository = MoviesRepository()

@router.get('/movies', status_code=200)
async def get_movies():
    return moviesRepository.get_movies()


@router.get('/producers_by_prize_ranges', status_code=200)
async def get_producers_by_prize_ranges():
    return moviesRepository.get_producers_by_prize_ranges()
    

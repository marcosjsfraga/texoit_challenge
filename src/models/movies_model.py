from pydantic import BaseModel

class Movies(BaseModel):
    id: int
    year: int
    title: str
    studios: str
    producers: str
    winner: bool
from pydantic import BaseModel, create_model

query_params = {"row_number": (int, 0)}
query_model = create_model("Query", **query_params) 

class Movies(BaseModel):
    id: int
    year: int
    title: str
    studios: str
    producers: str
    winner: bool
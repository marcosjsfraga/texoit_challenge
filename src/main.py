import uvicorn
from fastapi import FastAPI

from configs.database import Database
from routers.main_router import router as main_router
from routers.movies_router import router as movies_router
from services.csv_service import CSVService

app = FastAPI()
app.include_router(main_router)
app.include_router(movies_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", reload=True)


@app.on_event("startup")
def initialize():
    database = Database()
    csvService = CSVService()

    database.initialize_db()
    csvService.import_movielist()

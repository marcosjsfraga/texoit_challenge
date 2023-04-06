import uvicorn
import pandas as pd
from fastapi import FastAPI
from database import get_or_create_db
from movies.model import Movies
from services import import_csv

app = FastAPI()

if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', reload=True)

@app.on_event('startup')
def initialize():
    get_or_create_db()
    import_csv()

@app.get('/status')
async def api_status():
    return { 'detail': 'API is already running! 🚀' }

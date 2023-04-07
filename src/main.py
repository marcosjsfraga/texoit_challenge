import uvicorn
from fastapi import FastAPI

from configs.database import Database
from services.csv_service import CSVService


app = FastAPI()

if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', reload=True)

@app.on_event('startup')
def initialize():
    database = Database()
    csvService = CSVService()
    
    database.initialize_db()
    csvService.import_file('movielist.csv')

@app.get('/status', status_code=200)
async def api_status():
    return { 'detail': 'API is already running! 🚀' }

from fastapi import FastAPI

app = FastAPI()

# @app.on_event('startup')
# def initialize():
#     # get_or_create_db()
#     # import_csv()

@app.get('/status')
async def api_status():
    return { 'detail': 'API is already running! 🚀' }

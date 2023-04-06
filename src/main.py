from fastapi import FastAPI
import uvicorn
import csv

app = FastAPI()


def import_csv():
    # print('Importando CSV...')
    with open('movielist.csv', 'r') as external_file:
        csv_file = csv.reader(external_file, delimiter=';')
        for i, line in enumerate(csv_file):
            print(str(line))


if __name__ == '__main__':
    import_csv()
    
    uvicorn.run('main:app', host='127.0.0.1', reload=True)


@app.get('/status')
async def api_status():
    return { 'detail': 'API is already running! 🚀' }



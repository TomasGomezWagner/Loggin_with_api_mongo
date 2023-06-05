from fastapi import FastAPI
from dotenv import dotenv_values
from pymongo import MongoClient

from routers.routers import router as book_router
from routers.user_router import user_router

config =  dotenv_values('.env')


app = FastAPI()


@app.on_event('startup')
def startup_db_client():
    app.mongodb_client = MongoClient(config['ATLAS_URI'])
    app.database = app.mongodb_client[config['DB_NAME']]
    print('connected to the MongoDB database!')


@app.on_event('shutdown')
def shutdown_db_client():
    app.mongo_client.close()


app.include_router(book_router, tags=['books'], prefix='/book')
app.include_router(user_router, tags=['users'], prefix='/user')
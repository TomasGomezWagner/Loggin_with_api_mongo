from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import List
from bson.objectid import ObjectId
import bcrypt

from models.user_model import User, UserUpdate
from models.user_model import UserFull, ResponseFullUser, UserIndb


def hash_passw(passw=str):
    salt = bcrypt.gensalt()
    password = passw.encode('utf-8')
    password = bcrypt.hashpw(password, salt)
    return password


def validate_passw(passw_input:str, passw_db):
    passw_input = passw_input.encode('utf-8')
    return bcrypt.checkpw(passw_input, passw_db)


user_router = APIRouter()


@user_router.post("/", response_description="Create a new User", status_code=status.HTTP_201_CREATED, response_model=ResponseFullUser)
def create_user_new(request: Request, user: UserFull = Body(...)):
    user = jsonable_encoder(user)
    user['passw'] = hash_passw(user['passw'])
    new_user = request.app.database["users"].insert_one(user)
    created_user = request.app.database["users"].find_one(
        {"_id": new_user.inserted_id}
    )

    return created_user


@user_router.get("/listar", response_description="List all users", response_model=List[ResponseFullUser])
def list_users(request: Request):
    users = list(request.app.database["users"].find(limit=100))
    return users


@user_router.put('/{id}', response_description='Update a user', response_model=ResponseFullUser)
def update_user(id, request:Request, user:UserUpdate=Body(...)):
    user = {k: v for k, v in user.dict().items() if v is not None}
    if len(user) >= 1:
        id = ObjectId(id)
        update_result = request.app.database['users'].update_one(
            {'_id':id},{'$set':user}
        )
        if update_result.modified_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'user with ID {id} not found')
    
    if (
        existing_user := request.app.database['users'].find_one({'_id':id})
    ) is not None:
        return existing_user
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'user with ID {id} not found')


@user_router.get('/validar', response_model=UserIndb) #mandar los parametros por query en la ruta (?username=...&&passw=...)
def search_and_validate(request:Request, username, passw):
    user = request.app.database['users'].find_one({'username':username})
    if user and (validate_passw(passw, user['passw'])):
        return JSONResponse(status_code=status.HTTP_202_ACCEPTED, content={'id':f'{user["_id"]}','detail':'user authenticated'})
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='user and password doesnt match')
    

@user_router.get('/{id}', description='Get user info by id', response_model=ResponseFullUser)
def get_user_info(request:Request, id):
    id = ObjectId(id)
    user = request.app.database['users'].find_one({'_id':id})
    return user



###################################################################################################################################


# @user_router.post("/", response_description="Create a new User", status_code=status.HTTP_201_CREATED, response_model=User)
# def create_user(request: Request, user: User = Body(...)):
#     user = jsonable_encoder(user)
#     new_user = request.app.database["users"].insert_one(user)
#     created_user = request.app.database["users"].find_one(
#         {"_id": new_user.inserted_id}
#     )

#     return created_user


# @user_router.get("/", response_description="List all users", response_model=List[User])
# def list_users(request: Request):
#     users = list(request.app.database["users"].find(limit=100))
#     return users


# @user_router.put('/{id}', response_description='Update a user', response_model=User)
# def update_user(id, request:Request, user:UserUpdate=Body(...)):
#     user = {k: v for k, v in user.dict().items() if v is not None}
#     if len(user) >= 1:
#         id = ObjectId(id)
#         update_result = request.app.database['users'].update_one(
#             {'_id':id},{'$set':user}
#         )
#         if update_result.modified_count == 0:
#             raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'user with ID {id} not found')
    
#     if (
#         existing_user := request.app.database['users'].find_one({'_id':id})
#     ) is not None:
#         return existing_user
    
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'user with ID {id} not found')

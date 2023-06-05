import uuid
from typing import Optional, Union
from pydantic import BaseModel, Field


class User(BaseModel):

    username: str = Field(...)
    passw: str = Field(...)
    info: dict = Field()
    rol: dict = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            'example':{
                
                "username": "DonQuixote",
                "passw": "MigueldeCervantes",
                "info":{
                    'name':'Tomas',
                    'last_name': 'Gomez Wagner',
                    'email':'twagner@cecaitra.org.ar'
                },
                'rol':{
                    'type':'sector_admin',
                    'sector':'cecasit',
                }
            }
        }




class UserUpdate(BaseModel):
    username: Optional[str]
    passw: Optional[str]
    info: Optional[dict]
    rol: Optional[dict]

    class Config:
        schema_extra = {
            'example':{
                "username": "DonQuixote",
                "passw": "MigueldeCervantes",
                "info":{
                    'name':'Tomas',
                    'last_name': 'Gomez Wagner',
                    'email':'twagner@cecaitra.org.ar'
                },
                'rol':{
                    'type':'sector_admin',
                    'sector':'cecasit',
                }
            }
        }



######################################################################################################################


class UserBase(BaseModel):
    username: str = Field(...)


class UserIndb(UserBase):
    passw: str = Field(...)


class UserFull(UserIndb):
    info: Optional[dict] = Field()
    rol: dict = Field(...)


    class Config:
        schema_extra = {
            'example':{
                "username": "DonQuixote",
                "info":{
                    'name':'Tomas',
                    'last_name': 'Gomez Wagner',
                    'email':'twagner@cecaitra.org.ar'
                },
                'rol':{
                    'type':'sector_admin',
                    'sector':'cecasit',
                }
            }
        }



class ResponseFullUser(BaseModel):
    username: str = None
    info: dict = None
    rol: dict = None

    class Config:
        schema_extra = {
            'example':{
                "username": "twagner",
                "info":{
                    'name':'Tomas',
                    'last_name': 'Gomez Wagner',
                    'email':'twagner@cecaitra.org.ar'
                },
                'rol':{
                    'type':'sector_admin',
                    'sector':'cecasit',
                }
            }
        }







# from settings import USUARIOS
import requests

# class User:
#     def __init__(self, user, psswd) -> None:
#         self.user = user
#         self.psswd = psswd


#     def verificar(self,):
#         if self.user in USUARIOS and self.psswd == USUARIOS[self.user]['psswd']:
#             return True
#         else:
#             print('datos erroneos')
#             return False


class User:
    username: str = None
    passw: str  = None
    name: str = None
    last_name: str = None
    email: str = None
    type: str = None
    sector: str = None
    # is_verificado:bool =None

    def __init__(self, username, passwd) -> None:

        self.username = username
        self.passw = passwd

        self.is_verificado = self.verificar()


    def verificar(self,):
        
        validacion = requests.get(f'http://127.0.0.1:8000/user/validar/?username={self.username}&&passw={self.passw}')

        if validacion:

            if validacion.status_code == 202:
            
                user_id = validacion.json()['id']
                info = requests.get(f'http://127.0.0.1:8000/user/{user_id}').json()
        
                for k,v in info.items():
                    if k == 'username':
                        pass
                    if type(v) is dict:
                        for k2,v2 in v.items():
                            setattr(self, k2, v2)
                    else:
                        setattr(self, k,v)

                return True
            
            else:

                return False
            
        else:
            print(validacion.json())
            return False


if __name__ == '__main__':

    asd = User(username='twagner', passwd='cecaitra123')
    
    print(asd.is_verificado)
    
    if asd.is_verificado:
        print(asd.type)
        print(asd.sector)

